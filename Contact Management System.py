import tkinter as tk
from tkinter import messagebox
import re
import sqlite3

class Contacts:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def validate(self):
        if not self.name or not self.email or not self.phone:
            return False
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            return False
        if not re.match(r"^\d{10}$", self.phone):
            return False
        return True

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.open_add_contact)
        self.add_button.pack(side=tk.LEFT)

        self.update_button = tk.Button(self.frame, text="Update Contact", command=self.open_update_contact)
        self.update_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side=tk.LEFT)

    def open_add_contact(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add Contact")

        self.name_label = tk.Label(self.add_window, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.add_window)
        self.name_entry.grid(row=0, column=1)

        self.email_label = tk.Label(self.add_window, text="Email:")
        self.email_label.grid(row=1, column=0)
        self.email_entry = tk.Entry(self.add_window)
        self.email_entry.grid(row=1, column=1)

        self.phone_label = tk.Label(self.add_window, text="Phone:")
        self.phone_label.grid(row=2, column=0)
        self.phone_entry = tk.Entry(self.add_window)
        self.phone_entry.grid(row=2, column=1)

        self.save_button = tk.Button(self.add_window, text="Save", command=self.save_contact)
        self.save_button.grid(row=3, columnspan=2)

    def save_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        new_contact = Contacts(name, email, phone)
        if new_contact.validate():
            conn = sqlite3.connect('contacts.db')
            c = conn.cursor()
            c.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Contact added successfully.")
            self.add_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid contact details.")

    def open_update_contact(self):
        # Similar to open_add_contact but for updating a contact
        pass

    def delete_contact(self):
        # Popup window for deleting a contact
        pass

# Create the SQLite database if not exists
conn = sqlite3.connect('contacts.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS contacts 
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT)''')
conn.commit()
conn.close()

root = tk.Tk()
app = ContactManagerApp(root)
root.mainloop()
