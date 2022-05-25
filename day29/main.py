import random
from tkinter import *
import pyperclip
from tkinter import messagebox
import json

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
    account = account_entry.get()
    website = website_entry.get()

    if len(account) == 0 or len(website) == 0:
        messagebox.showinfo(title="information", message="不可以为空")
    else:
        password = [random.choice(ALPHABET) for _ in range(10)]
        text = "".join(password)
        password_text.config(state="normal")
        password_text.insert(INSERT, text)
        password_text.config(state="disabled")

        is_ok = messagebox.askokcancel(title="info", message=f"{website} | {account} | {text} is ok to save? ")
        if is_ok:

            # 网站的账号密码信息 以字典形式给出
            new_data = {
                website: {
                    "email": account,
                    "password": text,
                }
            }
            # 以 json 文件的格式 将信息写入到文件 data.json 中
            # 先读取 在更新 再写入
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                messagebox.showinfo(title="具体信息", message=f"网站是:{website}\n账号是: {account} \n密码是: {text}")
            # 将密码 复制到剪贴板中
            pyperclip.copy(text)
        else:
            password_text.config(state="normal")
            password_text.delete(1.0, END)


def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="error", message="没有暂存的文件,请先生成密码文件")
    else:
        info = website_entry.get()
        # 这里data.keys() 生成的是 list
        if info in data.keys():
            messagebox.showinfo(title="website_account_password", message=f"网站是:{info}\n"
                                                                          f"账号是: {data[info]['email']} \n"
                                                                          f"密码是: {data[info]['password']}")
        else:
            messagebox.showerror(title="error", message="你可能还没有设置这个网站的密码，请你设置")


def clear():
    password_text.config(state="normal")
    password_text.delete(1.0, END)
    account_entry.delete(0, END)
    account_entry.insert(0, "example@example.com")
    website_entry.delete(0, END)


def on_click(event):
    event.widget.delete(0, END)


# UI
window = Tk()
window.title("随机密码生成器")
window.config(padx=20, pady=30)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(bg=YELLOW, width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=(FONT_NAME, 15, "bold"), fg="black")
website_label.grid(row=1, column=0)

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1)

search_button = Button(text="查询", command=search)
search_button.grid(row=1, column=2)

account_label = Label(text="Account:", font=(FONT_NAME, 15, "bold"), fg="black")
account_label.grid(row=2, column=0)

account_entry = Entry(width=40)
account_entry.insert(0, "example@example.com")
account_entry.bind("<Button-1>", on_click)
account_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", font=(FONT_NAME, 15, "bold"), fg="black")
password_label.grid(row=3, column=0)

password_text = Text(width=30, height=1, state="disabled")
password_text.grid(column=1, row=3)

generator_button = Button(text="生成", fg=RED, font=(FONT_NAME, 10, "bold"), command=generate_password)
generator_button.grid(column=2, row=3)

clear_button = Button(text="清除", fg=RED, font=(FONT_NAME, 10, "bold"), command=clear, width=35)
clear_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
