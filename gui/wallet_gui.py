import tkinter as tk

class WalletWindow:
    def __init__(self, master):
        self.master = master

        # Label to display current balance
        self.label_balance = tk.Label(master, text="Current Balance: 0")  # Example initial balance
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

        # Text widget to display transaction history
        self.text_transactions = tk.Text(master, width=50, height=10)
        self.text_transactions.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

        # Populate the text widget with sample transaction history
        sample_transactions = "Transaction 1\nTransaction 2\nTransaction 3\nTransaction 4\nTransaction 5"
        self.text_transactions.insert(tk.END, sample_transactions)

        # Create a button to close the window
        self.button_close = tk.Button(master, text="Close", command=self.close_window)
        self.button_close.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def deposit_funds(self):
        # Implement deposit funds logic here
        amount = self.entry_amount.get()
        # Call function to handle depositing funds
        print(f"Deposited: ${amount}")

    def withdraw_funds(self):
        # Implement withdraw funds logic here
        amount = self.entry_amount.get()
        # Call function to handle withdrawing funds
        print(f"Withdrawn: ${amount}")

    def close_window(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = WalletWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
