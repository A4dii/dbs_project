import tkinter as tk
from tkinter import messagebox
from sqlalchemy.orm import sessionmaker
from database import engine
from model.user import User
from sqlModel import Game
from sqlModel import UserLibrary
from utils import generate_game_data

class GameShopWindow:
    def __init__(self, master, user_id):
        self.master = master
        self.user_id = user_id
        self.session = sessionmaker(bind=engine)()

        # Create a listbox to display available games
        self.listbox_games = tk.Listbox(master, width=50, height=10)
        self.listbox_games.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        self.populate_game_list()

        # Create a button to purchase selected game
        self.button_purchase = tk.Button(master, text="Purchase", command=self.purchase_game)
        self.button_purchase.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Create a button to close the window
        self.button_close = tk.Button(master, text="Close", command=self.close_window)
        self.button_close.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    def populate_game_list(self):
        # Check if games exist in the database, if not, generate sample game data
        #if not self.session.query(Game).count():
        generate_game_data()  # Generate sample game data if database is empty

        # Retrieve available games from the database and populate the listbox
        games = self.session.query(Game).all()
        for game in games:
            self.listbox_games.insert(tk.END, f"{game.title} - ${game.price:.2f}")

    def purchase_game(self):
        selected_game_index = self.listbox_games.curselection()
        if selected_game_index:
            selected_game = self.session.query(Game).all()[selected_game_index[0]]
            user = self.session.query(User).get(self.user_id)
            
            user_library = self.session.query(UserLibrary).filter_by(user_id=self.user_id, game_id=selected_game.id).first()
            
            if user_library:
                tk.messagebox.showerror("Already Owned", f"You already own {selected_game.title}.")
            elif user.balance >= selected_game.price:
                # Deduct game price from user's balance
                user.balance -= selected_game.price

                # Add the purchased game to the user's library
                user_library = UserLibrary(user_id=self.user_id, game_id=selected_game.id)
                self.session.add(user_library)
                self.session.commit()

                # Refresh the list of available games
                self.listbox_games.delete(0, tk.END)
                games = self.session.query(Game).all()
                for game in games:
                    self.listbox_games.insert(tk.END, f"{game.title} - ${game.price:.2f}")

                # Inform the user about the purchase
                messagebox.showinfo("Purchase Successful", f"Congratulations! You have purchased {selected_game.title}.")
            else:
                messagebox.showerror("Insufficient Funds", "You don't have enough balance to purchase this game.")
        else:
            messagebox.showerror("No Game Selected", "Please select a game to purchase.")

    def close_window(self):
        self.session.close()
        self.master.destroy()

def main():
    root = tk.Tk()
    user_id = 1  # Assuming the user ID is known
    app = GameShopWindow(root, user_id)
    root.mainloop()

if __name__ == "__main__":
    main()
