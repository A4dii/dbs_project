import tkinter as tk
from sqlalchemy.orm import sessionmaker
from database import engine
from model.user import User
from sqlModel import Friendship
from model.chatlog import ChatLog

class ChatlogWindow:
    def __init__(self, master, user_id):
        self.master = master
        self.user_id = user_id
        self.friends = []  # Store friends list
        self.selected_friend_id = None  # Store ID of selected friend
        self.session = sessionmaker(bind=engine)()

        # Create a listbox to display friends
        self.listbox_friends = tk.Listbox(master, width=50, height=10)
        self.listbox_friends.grid(row=0, column=0, padx=10, pady=5)

        # Create a text widget to display chat history
        self.text_chat_history = tk.Text(master, width=50, height=20)
        self.text_chat_history.grid(row=0, column=1, padx=10, pady=5)

        # Create an entry widget for typing messages
        self.entry_message = tk.Entry(master, width=50)
        self.entry_message.grid(row=1, column=1, padx=10, pady=5)

        # Create a button to send messages
        self.button_send = tk.Button(master, text="Send", command=self.send_message)
        self.button_send.grid(row=1, column=2, padx=10, pady=5)

        # Bind selection event to update chat history
        self.listbox_friends.bind('<<ListboxSelect>>', self.update_chat_history)

        # Update friends list initially
        self.update_friends_list()

    def update_friends_list(self):
        # Clear current friends list
        self.listbox_friends.delete(0, tk.END)
        # Query the database for all friends of the user
        friendships = self.session.query(Friendship).filter(Friendship.user_id1 == self.user_id).all()
        for friendship in friendships:
            friend = self.session.query(User).filter(User.id == friendship.user_id2).first()
            self.friends.append((friendship.user_id2, friend.username))
            self.listbox_friends.insert(tk.END, friend.username)

    def update_chat_history(self, event):
        # Clear current chat history
        self.text_chat_history.delete(1.0, tk.END)
        # Get the selected friend index
        selected_friend_index = self.listbox_friends.curselection()
        if selected_friend_index:
            # Retrieve the friend ID from the friends list
            self.selected_friend_id = self.friends[selected_friend_index[0]][0]
            # Query the database for chat history between the user and the selected friend
            chatlogs = self.session.query(ChatLog).filter(
                ((ChatLog.sender_id == self.user_id) & (ChatLog.receiver_id == self.selected_friend_id)) |
                ((ChatLog.sender_id == self.selected_friend_id) & (ChatLog.receiver_id == self.user_id))
            ).order_by(ChatLog.sent_at).all()
            # Display chat history in the text widget
            for chatlog in chatlogs:
                sender_name = self.session.query(User).filter(User.id == chatlog.sender_id).first().username
                if chatlog.sender_id == self.user_id:
                    self.text_chat_history.insert(tk.END, f"You: {chatlog.message}\n")
                else:
                    self.text_chat_history.insert(tk.END, f"{sender_name}: {chatlog.message}\n")
        else:
            self.selected_friend_id = None

    def send_message(self):
        # Get the message from the entry widget
        message = self.entry_message.get()
        if self.selected_friend_id and message:
            # Create a new chatlog object
            chatlog = ChatLog(sender_id=self.user_id, receiver_id=self.selected_friend_id, message=message)
            # Add the chatlog to the database
            self.session.add(chatlog)
            self.session.commit()
            # Update chat history to display the new message
            self.update_chat_history(None)
            # Clear the entry widget after sending the message
            self.entry_message.delete(0, tk.END)

def main():
    root = tk.Tk()
    user_id = 1  # Assuming the user ID is known
    app = ChatlogWindow(root, user_id)
    root.mainloop()

if __name__ == "__main__":
    main()
