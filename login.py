# Login Form
# Importing of necessary libraries
import customtkinter as ctk
import pymysql
from tkinter import messagebox

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuring theme of the application
        ctk.set_appearance_mode('system')

        # Configure window properties
        self.title('Log In') # Title
        self.geometry('500x300') # Size
        self.resizable(False, False) # Resizing capability
        self.iconbitmap('clover.ico') # Icon

        self.heading = ctk.CTkLabel(self, text="Login", font=('Segoe UI', 24, 'bold'))
        self.heading.pack(pady=5)

        # Frame to hold labels and entries which are entered user information
        self.entries_frame = ctk.CTkFrame(self)
        self.entries_frame.pack(pady=5)

        # Username label and entry
        self.user_label = ctk.CTkLabel(self.entries_frame, text="Username:\t")
        self.user_label.grid(row=0, column=0, padx=10, pady=20)
        self.user_entry = ctk.CTkEntry(self.entries_frame, placeholder_text='Enter username')
        self.user_entry.grid(row=0, column=1, padx=10, pady=20)

        # Password label and entry
        self.passwd_label = ctk.CTkLabel(self.entries_frame, text="Password:\t")
        self.passwd_label.grid(row=1, column=0, padx=10, pady=20)
        self.passwd_entry = ctk.CTkEntry(self.entries_frame, placeholder_text='Enter password')
        self.passwd_entry.grid(row=1, column=1, padx=10, pady=20)

        # Frame to hold Log In & Register buttons
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.pack(pady=5)

        #Log In Button
        self.login_button = ctk.CTkButton(self.buttons_frame, corner_radius=5, text="Log In", hover_color='yellow', command=self.login)
        self.login_button.grid(row=0, column=0, padx=10, pady=20)

        #Register Button
        self.register_button = ctk.CTkButton(self.buttons_frame, corner_radius=5, text="Register", fg_color='green', hover_color='red', command=self.register_user)
        self.register_button.grid(row=0, column=1, padx=10, pady=20)

    def connection(self):
        # Function which stores connecto
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', database='school', autocommit=True)
            return conn
        except pymysql.MySQLError as err:
            messagebox.showerror('Error', err)

    def verify_user_credentials(self, username: str, password: str):
        # Function that verifies user information in the database
        try:
            conn = self.connection()
            cx = conn.cursor()

            cx.execute("SELECT * FROM passsubsys WHERE user=%s AND password=%s;", (username, password))

            results = cx.fetchone()

            return results
        except pymysql.MySQLError as err:
            messagebox.showerror('Error' ,err)
            
    def login(self):
        if self.verify_user_credentials(self.user_entry.get(), self.passwd_entry.get()):
            messagebox.showinfo('Success', "Login succesfull!!")
        else:
            messagebox.showerror('Error', "User not found!")

        self.user_entry.delete(0, ctk.END)
        self.passwd_entry.delete(0, ctk.END)

    def register_user(self):
        try:
            # Variables to store entry values
            username = self.user_entry.get()
            password = self.passwd_entry.get()

            conn = self.connection()
            cx = conn.cursor()

            # command to insert values into database table
            cx.execute("INSERT INTO passsubsys (user, password) VALUES (%s, %s);", (username, password))
            messagebox.showinfo('Success', "Registered succesfully!")
        except pymysql.MySQLError as err:
            messagebox.showerror("Error", f"{err}: Maybe you entered a taken username or the Database server isn't running")
        self.user_entry.delete(0, ctk.END)
        self.passwd_entry.delete(0, ctk.END)
