import pandas

# learn DataFrame  Series Rows

data = pandas.read_csv("./data.csv")
print(data)
# print(data.to_dict())
# dataList = data.temp.to_list()
# print(type(dataList[0]))
# data_dict = data.temp.to_dict()
# print(data_dict)

average = data.temp.mean()
print(average)
maxTemp = data.temp.max()
print(maxTemp)

rowOhio = data[data.location == "ohio"]
print(rowOhio)
maxTempInfo = data[data.temp == data.temp.max()]
print(maxTempInfo)
maxTempCity = maxTempInfo.location
print(maxTempCity)

# make a file to DataFrame then transfer it to any other forms
data_dict = {
    "students": ["lebron", "anthony", "wade"],
    "scores": [23, 15, 9],
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_csv.csv")
