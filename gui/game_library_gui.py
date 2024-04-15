import tkinter as tk
from sqlalchemy.orm import sessionmaker
from database import engine
from sqlModel import UserLibrary
from sqlModel import Game

class GameLibraryWindow:
    def __init__(self, master, user_id):
        self.master = master
        self.user_id = user_id

        self.listbox_games = tk.Listbox(master, width=50, height=10)
        self.listbox_games.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        self.button_close = tk.Button(master, text="Close", command=self.close_window)
        self.button_close.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        self.populate_library()

    def populate_library(self):
        session = sessionmaker(bind=engine)()
        user_library = session.query(UserLibrary).filter_by(user_id=self.user_id).all()
        session.close()

        if user_library:
            for entry in user_library:
                game_id = entry.game_id
                session = sessionmaker(bind=engine)()
                game = session.query(Game).get(game_id)
                session.close()
                if game:
                    self.listbox_games.insert(tk.END, game.title)

    def close_window(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    user_id = 1  # Assuming the user ID is known
    app = GameLibraryWindow(root, user_id)
    root.mainloop()

if __name__ == "__main__":
    main()
