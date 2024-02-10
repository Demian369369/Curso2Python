with open('./texs.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('Estoy Programando\n')
  file.write('otra linea\n')
  file.write('x3\n')