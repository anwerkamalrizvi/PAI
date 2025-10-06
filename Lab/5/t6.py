def saveQuestion():
    try:
        sentence = input("Enter a sentence: ")  
        if sentence.strip().endswith("?"):
            with open("questions.txt", "a") as file:
                file.write(sentence + "\n")
            print("Question has been added to questions.txt")
        else:
            print("Absolutely NOT a question!")
    except Exception as e:
        print(f"Error 404: {e}")

saveQuestion()