import random
from tkinter import *
import pyperclip
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
            '@', '#', '$', '%', '^', '&', '*', '_']


# generate pass and save it to a text
def generate_password():
    password = [random.choice(ALPHABET) for _ in range(10)]
    # password = []
    # for _ in range(10):
    #     new_pass = random.choice(ALPHABET)
    #     password.append(new_pass)
    text = "".join(password)
    password_text.config(state="normal")
    password_text.insert(INSERT, text)
    password_text.config(state="disabled")
    account = account_entry.get()
    with open("password.txt", "a") as pf:
        pf.write(f"{account}: {text} \n")
    success_window()
    # 将密码 复制到剪贴板中
    pyperclip.copy(text)


def success_window():
    success_info = Toplevel(window)
    success_info.minsize(200, 100)
    success_info.title("Your password is ok")
    success_label = Label(success_info, text="Congratulations, your password is stored password.txt successful", fg=RED)
    success_label.pack()


def clear():
    password_text.config(state="normal")
    password_text.delete(1.0, END)
    account_entry.delete(0, END)
    account_entry.insert(0, "example@example.com")


def on_click(event):
    event.widget.delete(0, END)


# UI
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=30)
product_label = Label(text="Password Generator", fg=PINK, font=(FONT_NAME, 20, "bold"))
product_label.grid(column=1, row=0)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(bg=YELLOW, width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)

account_label = Label(text="Account:", font=(FONT_NAME, 15, "bold"), fg="black")
account_label.grid(column=0, row=2)

account_entry = Entry(width=40)
account_entry.insert(0, "example@example.com")
account_entry.bind("<Button-1>", on_click)
account_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", font=(FONT_NAME, 15, "bold"), fg="black")
password_label.grid(column=0, row=3)

password_text = Text(width=30, height=1, state="disabled")
password_text.grid(column=1, row=3)

generator_button = Button(text="Generator", fg=RED, font=(FONT_NAME, 10, "bold"), command=generate_password)
generator_button.grid(column=2, row=3)

generator_button = Button(text="Clear", fg=RED, font=(FONT_NAME, 10, "bold"), command=clear, width=35)
generator_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
