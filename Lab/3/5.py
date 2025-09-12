def isPalindrome(txt):
    txt = txt.lower()
    if txt == txt[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

word = input("Enter any word: ")
isPalindrome(word)