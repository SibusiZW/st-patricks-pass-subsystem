# import necessary modules
import customtkinter as ctk
import passes
import confirm

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Window properties
        self.geometry('600x500') # Size
        self.title('Dashboard') # Title of the window
        self.resizable(False, False) # Resizing probability
        self.iconbitmap('assets/clover.ico') # Window icon

        self.heading = ctk.CTkLabel(self, text="Welcome To St Patrick's Pass Subsystem!", font=ctk.CTkFont('Cascadia Code', 24, 'bold')) # heading label for the window
        self.heading.pack(pady=5)

        # Frame to hold buttons which display options
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.pack(pady=20)

        # Options buttons
        self.view_passes_button = ctk.CTkButton(self.buttons_frame, text='View Pending Passes', corner_radius=10, hover_color='green', font=ctk.CTkFont('Cascadia Code', 14, 'bold'), command=self.view_passes)
        self.view_passes_button.grid(row=0, column=0, padx=20, pady=20)

        self.verify_pass_button = ctk.CTkButton(self.buttons_frame, text='Confirm Pass', corner_radius=10, hover_color='green', font=ctk.CTkFont('Cascadia Code', 14, 'bold'), command=self.verify_passes)
        self.verify_pass_button.grid(row=1, column=0, padx=20, pady=20)

        self.view_recent_button = ctk.CTkButton(self.buttons_frame, text='View Recently Confirmed Passes', corner_radius=10, hover_color='green', font=ctk.CTkFont('Cascadia Code', 14, 'bold'))
        self.view_recent_button.grid(row=2, column=0, padx=20, pady=20)

    def view_passes(self):
        app = passes.App()
        app.mainloop()

    def verify_passes(self):
        app = confirm.App()
        app.mainloop()

    def view_recent(self):
        pass

