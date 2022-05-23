from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    miles_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km")
window.config(padx=20, pady=20)
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
miles_result_label = Label(text="0")
miles_result_label.grid(column=1, row=1)
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)
calculator_button = Button(text="Calculator", command=miles_to_km)
calculator_button.grid(column=1, row=2)
# r = Radiobutton(text="op")
# r.grid(column=2, row=2)
# c = Checkbutton(text="man")
# c.grid(column=2, row=2)
# f = Frame(borderwidth=2, background="black", border=1)
# f.grid(column=2, row=3)
window.mainloop()
