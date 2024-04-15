import tkinter as tk
from sqlalchemy.orm import sessionmaker
from database import engine
from sqlModel import User
from sqlModel import Friendship

class SocialWindow:
    def __init__(self, master, user_id):
        self.master = master
        self.user_id = user_id
        self.session = sessionmaker(bind=engine)()

        # Frame to display other users
        self.frame_users = tk.Frame(master)
        self.frame_users.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Populate the frame with other users
        self.display_other_users()

    def display_other_users(self):
        users = self.session.query(User).filter(User.id != self.user_id).all()
        for user in users:
            user_frame = tk.Frame(self.frame_users)
            user_frame.pack(fill=tk.X, padx=5, pady=5)

            user_label = tk.Label(user_frame, text=user.username)
            user_label.pack(side=tk.LEFT)

            add_friend_button = tk.Button(user_frame, text="Add Friend", command=lambda user_id=user.id: self.add_friend(user_id))
            add_friend_button.pack(side=tk.RIGHT)

            remove_friend_button = tk.Button(user_frame, text="Remove Friend", command=lambda user_id=user.id: self.remove_friend(user_id))
            remove_friend_button.pack(side=tk.RIGHT)

    def add_friend(self, friend_id):
        existing_request = self.session.query(Friendship).filter_by(user_id1=self.user_id, user_id2=friend_id).first()
        if existing_request:
            tk.messagebox.showerror("Add Friend", "Friend request already sent.")
        else:
            friendship = Friendship(user_id1=self.user_id, user_id2=friend_id)
            self.session.add(friendship)
            self.session.commit()
            tk.messagebox.showinfo("Add Friend", "Friend added successfully.")

    def remove_friend(self, friend_id):
        friendship = self.session.query(Friendship).filter_by(user_id1=self.user_id, user_id2=friend_id).first()
        if friendship:
            self.session.delete(friendship)
            self.session.commit()
            tk.messagebox.showinfo("Remove Friend", "Friend removed successfully.")
        else:
            tk.messagebox.showerror("Remove Friend", "Friend not found.")

def main():
    root = tk.Tk()
    user_id = 1  # Assuming the user ID is known
    app = SocialWindow(root, user_id)
    root.mainloop()

if __name__ == "__main__":
    main()
