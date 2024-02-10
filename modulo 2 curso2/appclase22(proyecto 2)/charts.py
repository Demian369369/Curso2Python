import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()
  
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis("equal")
  plt.show()
  
if __name__ == '__main__':
  labels = ["a","b","c"]
  values = [10, 40, 800]
  generate_bar_chart(labels=labels, values=values)
#hola, para el lector de este codigo, recuerde usar la libreria solicitada en la clase
# en Terminal python3 app/ python app/charts.py