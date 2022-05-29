from tkinter import *
import requests


def get_quotes():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    print(data)
    canvas.itemconfig(word, text=quote)


window = Tk()
window.title("Ken Say")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414, highlightthickness=0)
back_image = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=back_image)
word = canvas.create_text(150, 207, width=250, text="", font=("Ariel", 20, "bold"))
canvas.grid(row=0, column=0)
person_image = PhotoImage(file="kanye.png")
person_button = Button(image=person_image, highlightthickness=0, command=get_quotes)
person_button.grid(row=1, column=0)
get_quotes()

window.mainloop()
