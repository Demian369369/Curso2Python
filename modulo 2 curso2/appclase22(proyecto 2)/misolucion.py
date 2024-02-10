import matplotlib.pyplot as mp
import re
import read_csv as read_files
def datos_continentes(data, country, capital, contine, world_population_by_percentage ): 
  anual = {}
  try:
    lista = list(filter(lambda x: x["Country"] == country, data))[0]
    for key, value in list(lista.items()):
      remover_letras = re.findall("[0-9]+", key)
      if len(remover_letras) == 0 or int(remover_letras[0]) < 1960:
        del lista[key]
      else:
        anual[remover_letras[0]] = int( value )
    return lista
  except IndexError:
    return f'Lo sentimos el dato {country} no esta en la lista o archivo'
  
def generar_barchat(info_country, country,):
  labels = info_country.keys()
  values = info_country.values()
  colors = ["#40563F", "#F00E32", "#C0C0C0", "#7A1A8B", "#00FF00"]
  mp.bar(labels, values, color = colors)
  mp.title(f"Pais {country}")
  mp.show()

if __name__ == "__main__":
  country = input("Ingrese el pais que desea buscar: ")
  arreglo_doc = read_files.read_csv("./data.csv")
  info = datos_continentes(arreglo_doc, country)
  print(info)
  generar_barchat( info, country )