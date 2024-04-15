import tkinter as tk
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from database import engine
from model.user import User

class WalletWindow:
    def __init__(self, master, user_id):
        self.master = master
        self.user_id = user_id

        # Label to display current balance
        self.label_balance = tk.Label(master, text="Current Balance: $0.00")  
        self.label_balance.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        # Entry widget for entering deposit/withdraw amount
        self.entry_amount = tk.Entry(master)
        self.entry_amount.grid(row=1, column=0, padx=10, pady=5)

        # Button to deposit funds
        self.button_deposit = tk.Button(master, text="Deposit", command=self.deposit_funds)
        self.button_deposit.grid(row=1, column=1, padx=10, pady=5)

        # Button to withdraw funds
        self.button_withdraw = tk.Button(master, text="Withdraw", command=self.withdraw_funds)
        self.button_withdraw.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Create a button to close the window
        self.button_close = tk.Button(master, text="Close", command=self.close_window)
        self.button_close.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Initialize balance label
        self.update_balance_label()

    def deposit_funds(self):
        try:
            amount = float(self.entry_amount.get())
            session = sessionmaker(bind=engine)()
            user = session.query(User).get(self.user_id)
            if user:
                user.balance += amount
                session.commit()
                session.close()
                self.update_balance_label()
        except Exception as e:
            print(f"Error depositing funds: {e}")

    def withdraw_funds(self):
        try:
            amount = float(self.entry_amount.get())
            session = sessionmaker(bind=engine)()
            user = session.query(User).get(self.user_id)
            if user and user.balance >= amount:
                user.balance -= amount
                session.commit()
                session.close()
                self.update_balance_label()
            else:
                print("Insufficient balance")
        except Exception as e:
            print(f"Error withdrawing funds: {e}")

    def update_balance_label(self):
        try:
            session = sessionmaker(bind=engine)()
            user = session.query(User).get(self.user_id)
            session.close()
            if user:
                self.label_balance.config(text=f"Current Balance: ${user.balance:.2f}")
        except SQLAlchemyError as e:
            print(f"Error updating balance label: {e}")

    def close_window(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    user_id = 1  # Assuming the user ID is known
    app = WalletWindow(root, user_id)
    root.mainloop()

if __name__ == "__main__":
    main()
