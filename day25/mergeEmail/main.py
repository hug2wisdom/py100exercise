with open("./Input/Names/Invited_names.txt", "r") as nameFile:
    namesList = nameFile.readlines()
    newNameList = []
    for name in namesList:
        newName = name.strip()
        newNameList.append(newName)

for name in newNameList:
    with open("./Input/Letters/WelcomeLetters.txt", "r") as ContentFile:
        content = ContentFile.read()
        newContent = content.replace("[name]", name)

for name in newNameList:
    with open(f"./Output/{name}.txt", "w") as sendFile:
        sendFile.write(newContent)
