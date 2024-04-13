import tkinter as tk
from gui.login_gui import LoginWindow
from gui.register_gui import RegisterWindow

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")

        login_button = tk.Button(self, text="Login", command=self.open_login_window)
        login_button.pack()

        register_button = tk.Button(self, text="Register", command=self.open_register_window)
        register_button.pack()

    def open_login_window(self):
        self.withdraw()  # Hide the main menu window
        login_window = LoginWindow(self)  # Open the login window
        login_window.protocol("WM_DELETE_WINDOW", self.show_main_menu)

    def open_register_window(self):
        self.withdraw()  # Hide the main menu window
        register_window = RegisterWindow(self)  # Open the register window
        register_window.protocol("WM_DELETE_WINDOW", self.show_main_menu)

    def show_main_menu(self):
        self.deiconify()  # Show the main menu window when a child window is closed


def main():
    root = MainMenu()
    root.mainloop()

if __name__ == "__main__":
    main()
