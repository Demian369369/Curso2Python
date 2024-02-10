numbers = [1,2,3,4,5]
nuevos_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(nuevos_numbers)
print(numbers)