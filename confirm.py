# import necessary libraries
import customtkinter as ctk
import datetime
import pymysql
import json
from tkinter import messagebox

RECORD_FILE = 'assets/records.json'

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.records = []

        self.title("Confirm pass")
        self.geometry('300x400')
        self.iconbitmap('assets/clover.ico')
        self.resizable(False, False)

        self.heading = ctk.CTkLabel(self, text="Verify Passes", font=ctk.CTkFont('Cascadia Code', 20, 'bold'))
        self.heading.pack(pady=5)

        self.container = ctk.CTkFrame(self)
        self.container.pack(pady=10)

        self.pass_id_entry = ctk.CTkEntry(self.container, placeholder_text="Enter Pass ID", width=200)
        self.pass_name_entry = ctk.CTkEntry(self.container, placeholder_text="Enter name of holder of pass", width=200)
        self.verify_btn = ctk.CTkButton(self.container, text="Confirm Pass", corner_radius=10, font=ctk.CTkFont('Cascadia Code', 14, 'bold'), command=self.confirm_pass)

        self.pass_id_entry.grid(row=0, column=0, padx=20, pady=20)
        self.pass_name_entry.grid(row=1, column=0, padx=20, pady=20)
        self.verify_btn.grid(row=2, column=0, padx=20, pady=20)

    def confirm_pass(self):
        self.verify(self.pass_id_entry.get(), self.pass_name_entry.get())

    def verify(self, pid: str, pname: str):
        try:
            conn = self.connection()
            cx = conn.cursor()

            cmd = cx.execute("DELETE FROM pass WHERE id=%s AND givenTo=%s;", (pid, pname))

            if cmd > 0:
                messagebox.showinfo('Success', "Pass confirmed succesfully!")
                date = datetime.date.today().isoformat()
                record = {'id': pid, 'name': pname, 'date': date}
                self.records.append(record)
                self.save_record()
            else:
                messagebox.showerror('Error', "Pass not found!!")
        except pymysql.MySQLError as err:
            messagebox.showerror('Failure', f"Error: {err}")

        self.pass_id_entry.delete(0, ctk.END)
        self.pass_name_entry.delete(0, ctk.END)

    def connection(self):
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='school',
                autocommit=True
            )

            return conn
        except pymysql.MySQLError as err:
            messagebox.showerror("Failure", f"Error: {err}")

    def save_record(self):
        with open(RECORD_FILE, 'w') as f:
            data = self.records
            json.dump(data, f, indent=4)

a = App()
a.mainloop()