def json():
    try:
        data = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}
        with open("ages.json", "w") as file:
            file.write(str(data))
        with open("ages.json", "r") as file:
            content = file.read()
        loaded = eval(content)
        max_age = max(loaded.values())
        print(f"Person(s) with maximum age ({max_age}):")
        for name, age in loaded.items():
            if age == max_age:
                print(name)
        print("\nPeople with same age:")
        checked = []
        for k1, v1 in loaded.items():
            for k2, v2 in loaded.items():
                if k1 != k2 and v1 == v2 and k1 not in checked:
                    print(f"{k1} and {k2} both have age {v1}")
                    checked.append(k1)
                    checked.append(k2)

    except Exception as e:
        print(f"Error occurred: {e}\n Check ur code!")

json()
