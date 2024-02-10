#operaciones de conjuntos


set_a = {"col", "mex", "bol"}
set_b = {"pe", "bol"}
#union
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_a)
#interseccion
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)
#diferencia
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)
#diferencia simetrica en la interseccion
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)


#ejercicio de clase extra: 
countries = {"MX", "COL", "ARG", "USA"} 
northAm = {"USA", "CANADA"} 
centralAm = {"MX", "GT", "BZ"} 
southAm = {"COL", "BZ", "ARG"} 
new_set = countries | northAm | centralAm | southAm 
print(new_set)
