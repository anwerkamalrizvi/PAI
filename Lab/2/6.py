countries = {"China": 1440000000,"India": 1390000000,"USA": 331000000,"Indonesia": 273000000,"Pakistan": 220000000}

TOP3 = []

for _ in range(3):
    maxCountry = max(countries, key=countries.get)
    TOP3.append((maxCountry, countries[maxCountry]))
    del countries[maxCountry]

print("Top 3 most populated countries:", TOP3)
