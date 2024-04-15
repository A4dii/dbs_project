import tkinter as tk
from sqlalchemy.orm import sessionmaker
from model.user import User
from gui.main_gui import MainWindow
from database import Session

class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Login")
        self.user_id = None

        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack(padx=10, pady=5)

        self.entry_username = tk.Entry(self)
        self.entry_username.pack(padx=10, pady=5)

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack(padx=10, pady=5)

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(padx=10, pady=5)

        self.button_login = tk.Button(self, text="Login", command=self.login_user)
        self.button_login.pack(padx=10, pady=5)

    def login_user(self):
        # Get the user input
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Create a session to interact with the database
        session = Session()

        # Query the database for the user with the entered username
        user = session.query(User).filter_by(username=username).first()

        # Check if a user with the entered username exists and if the password matches
        if user and user.password == password:
            self.user_id = user.id
            # Close the session
            session.close()

            # Open the main window
            self.open_main_window()
        else:
            # Display an error message for invalid credentials
            tk.messagebox.showerror("Error", "Invalid username or password")

            # Close the session
            session.close()

    def open_main_window(self):
        root = tk.Tk()
        app = MainWindow(root, self.user_id)
        root.mainloop()
        pass
