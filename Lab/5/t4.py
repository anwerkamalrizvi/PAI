def employeeBiodata():
    try:
        name = input("Your OWN Name: ")
        cnic = input("Your OWN CNIC: ")
        age = input("Your Age :> : ")
        salary = input("--> Salary Likh! : ")

        with open("employee.txt", "w") as file:
            file.write(f"Name: {name}\nCNIC: {cnic}\nAge: {age}\nSalary: {salary}\n")

        print("Employee data saved successfully!")

        contact = input("Enter Contact to append: ")
        with open("employee.txt", "a") as file:
            file.write(f"Contact: {contact}\n")

        print("Contact added")

        with open("employee.txt", "r") as file:
            print("\nFinal File Content:\n" + file.read())

    except Exception as e:
        print(f"Error occurred: {e}\nCheck file and code mr")

employeeBiodata()
