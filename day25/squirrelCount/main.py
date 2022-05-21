import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# all_color = data["Primary Fur Color"].unique()
# print(all_color)

# 形成新的 DataFrame
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

new_squirrel_dict = {
    "Primary Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

new_data = pandas.DataFrame(new_squirrel_dict)
new_data.to_csv("new_data.csv")