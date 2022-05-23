import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
flag = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_work():
    global flag
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_label.config(text="no record")
    canvas.itemconfig(show_time, text="00:00")
    flag = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

#  常量不是变量  不需要传入函数中
def start_work():
    global flag
    flag += 1
    # 25 5 25 5 25 5 25 20

    if flag % 2 == 0:
        # 如果是 第二次 第四次 第六次
        # 完成一次专注 出现一个 √
        check_label.config(text="✔" * math.floor(flag / 2))
        timer_label.config(text="SHORT BREAK", fg=PINK)

        short_break_sec = SHORT_BREAK_MIN * 60
        count_down(short_break_sec)
    elif flag % 8 == 0:
        # 如果是 第八次  flag
        timer_label.config(text="LONG RELAX", fg=RED)
        check_label.config(text="✔" * math.floor(flag / 2))
        long_break_sec = LONG_BREAK_MIN * 60
        count_down(long_break_sec)
    else:
        # 如果是 第一次 第三次 第五次  第七次 到 flag  1234 1357
        timer_label.config(text="FOCUS WORK")
        work_sec = WORK_MIN * 60
        count_down(work_sec)


def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(show_time, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_work()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
timer_label.grid(column=1, row=0)

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
show_time = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

# 点击 start 按钮 计时开始
start_button = Button(text="start", highlightthickness=0, command=start_work)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0, command=reset_work)
reset_button.grid(column=2, row=2)

check_label = Label(text="no record", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=4)

window.mainloop()
