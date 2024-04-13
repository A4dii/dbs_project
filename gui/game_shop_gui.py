import tkinter as tk

class GameShopWindow:
    def __init__(self, master):
        self.master = master

        # Create a listbox to display available games
        self.listbox_games = tk.Listbox(master, width=50, height=10)
        self.listbox_games.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        # Populate the listbox with sample game titles
        sample_games = ["Game 1", "Game 2", "Game 3", "Game 4", "Game 5"]
        for game in sample_games:
            self.listbox_games.insert(tk.END, game)

        # Create a button to purchase selected game
        self.button_purchase = tk.Button(master, text="Purchase", command=self.purchase_game)
        self.button_purchase.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Create a button to close the window
        self.button_close = tk.Button(master, text="Close", command=self.close_window)
        self.button_close.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    def purchase_game(self):
        # Implement purchase logic here
        selected_game_index = self.listbox_games.curselection()
        if selected_game_index:
            selected_game = self.listbox_games.get(selected_game_index)
            # Call function to handle game purchase
            print(f"Purchased: {selected_game}")
        else:
            print("No game selected.")

    def close_window(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = GameShopWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
