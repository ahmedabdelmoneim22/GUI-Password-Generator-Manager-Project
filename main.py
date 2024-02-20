"""Access to All of Tkinter Classes, functions, constants"""
from tkinter import *
""" displaying various types of message boxes, 
Such as Information , Warning , Error, Question boxes"""
from tkinter import messagebox
"""RN Library"""
from random import choice, randint, shuffle
"""Copy text to the Clipboard"""
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'
             , 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    """>>Choice Randomly from the List<<"""
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    print(password_letters)
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    print(password_symbols)
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    print(password_numbers)
    password_list = password_letters + password_symbols + password_numbers
    print(password_list)
    shuffle(password_list) # Random Placement;
    password = "".join(password_list) # Convert to String;
    print("The PassWord:-",password)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
"""Tkinter Main Window"""
window = Tk()
"""Tkinter Title Window"""
window.title("Password Manager Project")
"""Window Padding"""
window.config(padx=50, pady=50)
"""Create Canvas to input Image"""
canvas = Canvas(height=200, width=200)
"""Input Image to Tkinter"""
logo_img = PhotoImage(file="logo.png")
"""Create-Image in the-Canvas"""
canvas.create_image(100, 100, image=logo_img)
"""Canvas-Placement"""
canvas.grid(row=0, column=1)
#Text Labels;
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
# Entries;
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "AhmedElMohandes@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
# Buttons;
generate_password_button = Button(text="Generate Password",
                                  command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop() # Keep-The-Program-Running;
