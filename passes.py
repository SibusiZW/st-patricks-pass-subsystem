# import necessary libraries
import customtkinter as ctk
import pymysql
from tkinter import ttk, messagebox

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.title("Passes")
        self.geometry('800x300')
        self.iconbitmap('assets/clover.ico')
        self.resizable(False, False)

        self.tree = ttk.Treeview(self, show='headings')
        self.scrollbar = ctk.CTkScrollbar(self, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.bind_data() # loads data into tree view

        self.scrollbar.pack(side='right')
        self.tree.pack(side='left', fill='x', expand=False)

    def bind_data(self):
        try:
            conn = self.connection()
            cx = conn.cursor()

            cx.execute("SELECT * FROM pass;")
            columns = [desc[0] for desc in cx.description]
            self.tree.configure(columns=columns)

            for col in columns:
                self.tree.column(col, anchor=ctk.CENTER)
                self.tree.heading(col, text=col)

            rows = cx.fetchall()

            for item in self.tree.get_children():
                self.tree.delete(item)

            for row in rows:
                self.tree.insert("", 0, values=row)
        except pymysql.MySQLError as err:
            messagebox.showerror('Error', f"Error: {err}")

    def connection(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', passwd='', database='school', autocommit=True)
            return conn
        except pymysql.MySQLError as err:
            messagebox.showerror('Error', f"Error {err}")
