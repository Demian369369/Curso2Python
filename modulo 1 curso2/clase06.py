import random
countries = ["Col","Mex","Bol", "Pe"]
population_v2 = { country: random.randint(1,100) for country in countries}
print(population_v2)

result = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result)

text = "Hola soy Demian"
unique = { c: c.upper() for c in text if c in "aeiou"}
print(unique)
