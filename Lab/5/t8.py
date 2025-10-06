def safeDivision():
    try:
        a = int(input("Enter 1st no: "))
        b = int(input("Enter 2nd no: "))
        r = a/b
        #print(undefined)  --> try this out! it is used to display the unexpected error! woo
        print(f"Result: {r}")
    except ZeroDivisionError:
        print("WHY ARE YOU DIVIDING WITH INNOCENT ZERO?")
    except ValueError:
        print("INVALID INPUT!\nCHECK YOUR INPUT BEFORE DIVIDING!")
    except Exception as e:
        print(f"Unluckily, an unexpected error came.\ncheck and find out: {e}")
safeDivision()