with open("file1.txt", "r") as num1:
    data1 = num1.readlines()
with open("file2.txt", "r") as num2:
    data2 = num2.readlines()

new_num1 = [int(num.strip()) for num in data1]
new_num2 = [int(num.strip()) for num in data2]
# new_num3 = [x for x in new_num1 for y in new_num2 if x == y]
new_num3 = [num for num in new_num1 if num in new_num2]


print(new_num3)
