import random
from tkinter import *

import requests

correct_answer = None


def get_question():
    global correct_answer
    response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
    response.raise_for_status()
    data = response.json()
    results = data["results"]
    our_test = random.choice(results)
    question = our_test["question"]
    correct_answer = our_test["correct_answer"]
    canvas.itemconfig(questions_asked, text=question)
    canvas.itemconfig(show_image, image=card_front)


def is_true():
    answer = "True"
    if answer == correct_answer:
        canvas.itemconfig(show_image, image=card_back_right)
    else:
        canvas.itemconfig(show_image, image=card_back_wrong)
    # get_question()


def is_false():
    answer = "False"
    if answer == correct_answer:
        canvas.itemconfig(show_image, image=card_back_right)
    else:
        canvas.itemconfig(show_image, image=card_back_wrong)
    # get_question()


# set the game UI
window = Tk()
window.title("GUESS GAME")
window.config(padx=50, pady=50)

# create the canvas
canvas = Canvas(width=800, height=526)
# set the image
card_front = PhotoImage(file="images/card_front.png")
card_back_right = PhotoImage(file="images/card_back_right.png")
card_back_wrong = PhotoImage(file="images/card_back_wrong.png")
show_image = canvas.create_image(400, 263, image=card_front)
# set the score
canvas.create_text(400, 50, text="Score: 0, Highest Score: 0", font=("Arial", 15, "bold"))
# set the text of question
questions_asked = canvas.create_text(400, 130, text="The questions will be here", width=600, font=("Arial", 20, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# set the true or false button
wrong_choice = PhotoImage(file="images/wrong.png")
right_choice = PhotoImage(file="images/right.png")
wrong = Button(image=wrong_choice, highlightthickness=0, command=is_false)
right = Button(image=right_choice, highlightthickness=0, command=is_true)
wrong.grid(row=1, column=0)
right.grid(row=1, column=1)

get_question()
window.mainloop()
