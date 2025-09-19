name = input("Enter your name: ")
birth_year = input("Enter your birth year: ")
first_three = name[:3].upper()
last_two = birth_year[-2:]
first_letter_ascii = ord(name[0].upper())
symbols = "@#%&*"
special_symbol = symbols[first_letter_ascii % len(symbols)]
password = first_three + last_two + special_symbol
print("Generated password:", password)