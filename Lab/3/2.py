def check_last_letter():
    text = input("Enter a sentence: ").strip() 

    if text == "":
        print("Wah shahkaar, Text tou likhh??\nDobara Run karo (ctrl+alt+n)")
        return

    last_char = text[-1].lower()  
    vowels = "aeiouAEIOU"
    
    if last_char.isalpha(): 
        if last_char in vowels:
            print(f"The last letter '{last_char}' --> vowel.")
        else:
            print(f"The last letter '{last_char}' --> consonant.")
    else:
        print(f"The last character '{last_char}' --> letter.")
check_last_letter()
