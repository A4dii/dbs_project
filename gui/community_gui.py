import tkinter as tk

class CommunityWindow:
    def __init__(self, master):
        self.master = master

        # Create a listbox to display available communities
        self.listbox_communities = tk.Listbox(master, width=50, height=10)
        self.listbox_communities.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        # Populate the listbox with sample community names
        sample_communities = ["Community 1", "Community 2", "Community 3", "Community 4", "Community 5"]
        for community in sample_communities:
            self.listbox_communities.insert(tk.END, community)

        # Create a button to join selected community
        self.button_join = tk.Button(master, text="Join", command=self.join_community)
        self.button_join.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Create a button to leave selected community
        self.button_leave = tk.Button(master, text="Leave", command=self.leave_community)
        self.button_leave.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Create a button to close the window
        self.button_close = tk.Button(master, text="Close", command=self.close_window)
        self.button_close.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    def join_community(self):
        # Implement join community logic here
        selected_community_index = self.listbox_communities.curselection()
        if selected_community_index:
            selected_community = self.listbox_communities.get(selected_community_index)
            # Call function to handle joining the community
            print(f"Joined: {selected_community}")
        else:
            print("No community selected.")

    def leave_community(self):
        # Implement leave community logic here
        selected_community_index = self.listbox_communities.curselection()
        if selected_community_index:
            selected_community = self.listbox_communities.get(selected_community_index)
            # Call function to handle leaving the community
            print(f"Left: {selected_community}")
        else:
            print("No community selected.")

    def close_window(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = CommunityWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
