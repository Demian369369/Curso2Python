import csv
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
#ejercicio final de la clase:
  
#   import csv

# def read_csv(path):
#    # Tu código aquí 👇
#    with open(path, 'r') as csvfile:
#       reader = csv.reader(csvfile, delimiter = ',')
#       total = 0
#       for row in reader:
#          total += int(row[1])
#       return total

# response = read_csv('./data.csv')
# print(response)