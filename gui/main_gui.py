import tkinter as tk
from gui.game_shop_gui import GameShopWindow
from gui.social_gui import SocialWindow
from gui.community_gui import CommunityWindow
from gui.wallet_gui import WalletWindow
from gui.game_library_gui import GameLibraryWindow
from gui.chatlog_gui import ChatlogWindow

class MainWindow:
    def __init__(self, master, user_id):
        self.master = master
        self.master.title("Main Menu")
        self.user_id = user_id 

        # Create a frame for the sidebar menu
        self.menu_frame = tk.Frame(master, bg="lightgrey", width=200)
        self.menu_frame.grid(row=0, column=0, sticky="ns")

        # Create buttons in the sidebar menu for navigation
        self.button_game_shop = tk.Button(self.menu_frame, text="Game Shop", command=self.open_game_shop_window)
        self.button_game_shop.pack(side="top", fill="x", padx=10, pady=5)

        self.button_social = tk.Button(self.menu_frame, text="Social", command=self.open_social_window)
        self.button_social.pack(side="top", fill="x", padx=10, pady=5)

        self.button_community = tk.Button(self.menu_frame, text="Community", command=self.open_community_window)
        self.button_community.pack(side="top", fill="x", padx=10, pady=5)

        self.button_wallet = tk.Button(self.menu_frame, text="Wallet", command=self.open_wallet_window)
        self.button_wallet.pack(side="top", fill="x", padx=10, pady=5)

        self.button_library = tk.Button(self.menu_frame, text = "Library", command = self.open_library_window)
        self.button_library.pack(side = "top", fill = "x", padx =10, pady=5)

        self.button_chatlog = tk.Button(self.menu_frame, text = "Chatlog", command = self.open_chatlog_window)
        self.button_chatlog.pack(side = "top", fill = "x", padx = 10, pady = 5)

        # Create a frame for the main content area
        self.content_frame = tk.Frame(master)
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        self.game_shop_window = None
        self.social_window = None
        self.community_window = None
        self.wallet_window = None
        self.library_window = None
        self.chatlog_window = None 
        # Start with the Game Shop window open by default
        self.open_game_shop_window()

    def open_game_shop_window(self):
        # Clear the content frame and open the Game Shop window
        self.clear_content_frame()
        game_shop_window = GameShopWindow(self.content_frame, user_id=self.user_id)
    
    def open_social_window(self):
        # Clear the content frame and open the Social window
        self.clear_content_frame()
        social_window = SocialWindow(self.content_frame, user_id = self.user_id)
    
    def open_community_window(self):
        # Clear the content frame and open the Community window
        self.clear_content_frame()
        community_window = CommunityWindow(self.content_frame)

    def open_wallet_window(self):
        # Clear the content frame and open the Wallet window
        self.clear_content_frame()
        wallet_window = WalletWindow(self.content_frame, user_id = self.user_id)
    
    def open_library_window(self):
        self.clear_content_frame()
        library_window = GameLibraryWindow(self.content_frame, user_id=self.user_id)

    def open_chatlog_window(self):
        self.clear_content_frame()
        chatlog_window = ChatlogWindow(self.content_frame, user_id=self.user_id)

    def clear_content_frame(self):
        # Clear all widgets from the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    user_id = 1
    app = MainWindow(root, user_id)
    root.mainloop()

if __name__ == "__main__":
    main()
