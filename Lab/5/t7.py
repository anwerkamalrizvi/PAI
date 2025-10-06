def fixTheLetter():
    try:
        with open("replacementNeeded.txt", "r") as file:
            text = file.read()

        print("Original txt:", text)
        fixed = ""
        for ch in text:
            if ch == 'z':
                fixed += 's'
            else:
                fixed += ch

        with open("replacementNeeded.txt", "w") as file:
            file.write(fixed)

        print("Replacement done\nModified txt:", fixed)
        
    except FileNotFoundError:
        print("NO SUCH FILE found!!")
    except Exception as e:
        print(f"An unexpected Error occured, now find: {e}")

fixTheLetter()