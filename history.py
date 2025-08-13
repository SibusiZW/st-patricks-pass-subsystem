import customtkinter as ctk
from tkinter import ttk, messagebox
import json

RECORD_FILE = 'assets/records.json'

class App(ctk.CTk):
    def __init__(self):

        super().__init__()

        self.title("History of confirmed passes")
        self.geometry('800x300')
        self.iconbitmap('assets/clover.ico')
        self.resizable(False, False)

        self.tree = ttk.Treeview(self, show='headings')
        self.scrollbar = ctk.CTkScrollbar(self, command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side='right')
        self.tree.pack(side='left', fill='x', expand=True)
        self.bind_data()

    def bind_data(self):
        try:
            columns = ["ID", "Name", "Date"]

            self.tree.configure(columns=columns)

            for col in columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, anchor=ctk.CENTER)

            for item in self.tree.get_children():
                self.tree.delete(item)

            with open(RECORD_FILE, 'r') as f:
                data = json.load(f)

            for record in data:
                self.tree.insert('', 0, values=(record['id'], record['name'], record['date']))
        except json.decoder.JSONDecodeError:
            messagebox.showerror('Error', "Failure in loading information")
