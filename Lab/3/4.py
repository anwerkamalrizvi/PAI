list1 = input("Enter first list: ").split()
list2 = input("Enter second list: ").split()

if len(list1) != len(list2):
    print("Must be the same number of elements in list")
else:
    my_dict = {}
    for i in range(len(list1)):
        my_dict[list1[i]] = list2[i]
    print(my_dict)
    with open("output.txt", "w") as f:
        f.write(str(my_dict))
        f.close()               
    