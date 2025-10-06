def replaceWord():
    try:
        fileName = input("file name? : ")
        oldWord = input("Enter word for search: ")
        newWord = input("Enter replacement word: ")

        with open(fileName, 'r', encoding='utf-8') as file:
            content = file.read()

        modifyIt = content.replace(oldWord, newWord)

        with open(fileName, 'w', encoding='utf-8') as file:
            file.write(modifyIt)

        print("replaced successfully!")

    except FileNotFoundError:
        print("ERROR 404. FILE NOT FOUND? ")
replaceWord()
