from tkinter import *
import pandas
import random

# read from the to_learn csv
try:
    to_learn = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data = data.to_dict(orient="records")
else:
    data = to_learn.to_dict(orient="records")
current_card = {}
remain_to_learn_number = len(data)


# let the known delete and the unknown to to_learn.csv
def remain_to_learn():
    global current_card, data, remain_to_learn_number
    data.remove(current_card)
    remain_to_learn_number = len(data)
    canvas.itemconfig(remain_number, text=f"Remain To Learn: {remain_to_learn_number}")
    remain_data = pandas.DataFrame(data)
    # not generate index
    remain_data.to_csv("data/to_learn.csv", index=False)
    next_card()


# change the card and word
def flip_card():
    global current_card
    # set the back image
    canvas.itemconfig(image_shown, image=card_back)
    # get the language and the word
    language = "English"
    word = current_card[language]
    canvas.itemconfig(language_shown, text=language)
    canvas.itemconfig(word_shown, text=word)


# get the next card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    language = "French"
    word = current_card[language]
    canvas.itemconfig(language_shown, text=language)
    canvas.itemconfig(word_shown, text=word)
    canvas.itemconfig(image_shown, image=card_front)
    flip_timer = window.after(3000, flip_card)


# create the ui

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50)

# set the canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
# set the image
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
image_shown = canvas.create_image(400, 270, image=card_front)
# set the word
remain_number = canvas.create_text(400, 50, text=f"Remain To Learn: {remain_to_learn_number}",
                                   font=("Arial", 20, "bold"), fill="red")
language_shown = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_shown = canvas.create_text(400, 270, text="", font=("Arial", 50, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# set the button
wrong = PhotoImage(file="images/wrong.png")
right = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
right_button = Button(image=right, highlightthickness=0, command=remain_to_learn)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)
# after 3 seconds , change the word to english and change to back image
flip_timer = window.after(3000, flip_card)
# set the default card
next_card()

window.mainloop()
