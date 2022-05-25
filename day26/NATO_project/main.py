# 1 transfer dataFrame to dict

import pandas
nato_data = pandas.read_csv("nato.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict)

# 2 accept the user input(letter) and tell them the code

ask = input("what do you say: ").upper()

# 根据key 找到值  在转换成list

ask_list = [letter for letter in ask]
# print(ask_list)
# result = []
# for letter in ask_list:
#     for (key, value) in nato_dict.items():
#         if letter == key:
#             result.append(value)

# result = [code for word in ask_list for (letter, code) in nato_dict.items() if word == letter]
try:
    result = [nato_dict[letter] for letter in ask_list]
except KeyError:
    print("sorry, we just accept string, please type strings not contain numbers")
else:
    print(result)