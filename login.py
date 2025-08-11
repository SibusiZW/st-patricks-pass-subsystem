# Login Form
# Importing of necessary libraries
import customtkinter as ctk
import pymysql

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

    def login(self):
        pass

    def register_user(self):
        pass