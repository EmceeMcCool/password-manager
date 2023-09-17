from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")
        if is_okay:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    character = [choice(letters) for char in range(randint(8, 10))]
    symbol = [choice(symbols) for char in range(randint(2, 4))]
    number = [choice(numbers) for char in range(randint(2, 4))]

    password_list = character + symbol + number
    shuffle(password_list)

    password = "".join(password_list)
    print(type(password))
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# MyPass logo
canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.config()
canvas.grid(column=1, row=0)

# Website label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

# Website entry
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

# Email/Username label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Email entry
email_entry = Entry(width=35)
email_entry.insert(0, "mccoolkurt@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Generate password button
password_button = Button(text="Generate Password", command=generate, width=10)
password_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()

