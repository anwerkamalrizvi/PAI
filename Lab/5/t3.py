def makeDictFromList():
    try:
        n = int(input("Number of elements in each list: "))
        list1 = []
        list2 = []

        print("Enter elements for first list ~keys:")
        for i in range(n):
            list1.append(input(f"Key {i+1}: "))

        print("Enter elements for second list ~values:")
        for i in range(n):
            list2.append(input(f"Value {i+1}: "))

        if len(list1) != len(list2):
            raise ValueError("SAME NUMBER OF ELEMENTS MUST BE IN LIST.")

        my_dict = {}
        for i in range(len(list1)):
            my_dict[list1[i]] = list2[i]

        with open("dictOutput.txt", 'w') as file:
            for k, v in my_dict.items():
                file.write(f"{k}:{v}\n")

        print("Dictionary saved in dictOutput.txt")

    except ValueError as ve:
        print("Value error detected. Check code", ve)
    except Exception as e:
        print(f"Unexpected error: {e}")

makeDictFromList()
