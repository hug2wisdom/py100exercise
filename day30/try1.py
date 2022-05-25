fruits = ["apple", "orange", "juice", "banana"]


def make_pie(index):
    fruit = fruits[index]
    print(fruit + "pie")


try:
    make_pie(4)
except IndexError as error_message:
    print(f"{error_message}, please give another index")
