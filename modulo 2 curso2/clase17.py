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

precios = list(map(lambda item: item["precio"], items))
print(precios)

def add_impuestos(item):
    item["impuestos"] = item["precio"] * .19
    return item

nuevos_items = list(map(add_impuestos, items))
print(nuevos_items)