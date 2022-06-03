from tkinter import *
from weather import Weather


class ForecastUi:
    def __init__(self):
        self.window = Tk()
        self.window.title("forecast 7 days")
        self.window.config(padx=100, pady=100)
        self.location_label = Label(text="请输入要查询的位置，可填写至区或县")
        self.location_label.grid(row=0, column=0)
        self.location_entry = Entry()
        self.location_entry.grid(row=0, column=1)
        self.location_button = Button(text="查询", width=15, command=self.set_weather)
        self.location_button.grid(row=0, column=2)

    def get_location(self):
        return self.location_entry.get()

    def get_weather(self):
        return Weather(self.get_location()).get_weather()

    def set_weather(self):
        for index in range(0, 7):
            date_label = Label(text=f"{self.get_weather()[index]['date']}")
            date_label.config(pady=10)
            date_label.grid(row=index + 1, column=0)
            weather_info_entry = Entry(width=40)
            weather_info_entry.grid(row=index + 1, column=1, columnspan=2)
            weather_info_entry.insert(0, self.get_weather()[index]['weather_info'])

    def ui_run(self):
        self.window.mainloop()