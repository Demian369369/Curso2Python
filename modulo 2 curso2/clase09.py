def suma_con_rango(min, max):
 print(min, max)
 suma = 0
 for x in range(min, max):
   suma += x
 return suma
    #1,2,3,4,5,6
resultado = suma_con_rango(1, 10)
print(resultado)
resultado_2 = suma_con_rango(resultado, resultado + 10)
print(resultado_2)


