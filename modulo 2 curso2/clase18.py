items = [
 {
    "producto": "camisa",
    "precio": 100,
 },
 {
    "producto": "pantalones",
    "precio": 300,
 },
 {
    "producto": "pantalones 2",
    "precio": 200,
 }
]

def add_impuestos(item):
    nuevo_item = item.copy()
    item["impuestos"] = nuevo_item["precio"] * .19
    return item

nuevos_items = list(map(add_impuestos, items))
print("nueva_lista")
print(nuevos_items)
print("vieja lista")
print(items)

#ejercicio de final de clase:
# def multiply_numbers(numbers):
#     return list(map(lambda numero : numero * 2, numbers))

# numbers = [1, 2, 3, 4]
# response = multiply_numbers(numbers)
# print(response)