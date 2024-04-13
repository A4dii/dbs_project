import tkinter as tk
from sqlalchemy.orm import sessionmaker
from model.user import User
from database import Session

class RegisterWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Register")

        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack(padx=10, pady=5)

        self.entry_username = tk.Entry(self)
        self.entry_username.pack(padx=10, pady=5)

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack(padx=10, pady=5)

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(padx=10, pady=5)

        self.label_email = tk.Label(self, text="Email:")
        self.label_email.pack(padx=10, pady=5)

        self.entry_email = tk.Entry(self)
        self.entry_email.pack(padx=10, pady=5)

        self.button_register = tk.Button(self, text="Register", command=self.register_user)
        self.button_register.pack(padx=10, pady=5)

    def register_user(self):
        # Get the user input
        username = self.entry_username.get()
        password = self.entry_password.get()
        email = self.entry_email.get()

        # Create a new user object
        new_user = User(username=username, password=password, email=email)

        # Create a session to interact with the database
        session = Session()

        # Add the new user to the session
        session.add(new_user)

        # Commit the changes to save the new user to the database
        session.commit()

        # Close the session
        session.close()

        # Optionally, you can provide feedback to the user that registration was successful
        print("User registered successfully!")
