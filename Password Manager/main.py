from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    generated_password = " ".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    web = website_entry.get()
    email = email_entry.get()
    key = password_entry.get()

    if len(web) <= 0 or len(email) <= 0 or len(key) <= 0:
        messagebox.showerror(
            title="Data Entry Error",
            message="One of the fields is empty, please try again.",
        )
    else:
        is_ok = messagebox.askokcancel(
            title=web,
            message=f"These are the details entered: \nEmail: {email} \nPassword: {key} \nIs it ok to save",
        )

        if is_ok:
            with open("saved_password.txt", "a+") as previous_passwords:
                previous_passwords.write(f"{web} | {email} | {key}\n")
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# UI
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# labels
website = Label(text="Website:")
website.grid(column=0, row=1)
email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "mbuso.mgobhozi@icloud.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
