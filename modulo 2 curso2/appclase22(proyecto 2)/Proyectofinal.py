import csv
import matplotlib.pyplot as plt
def open_csv():
    with open('./world_population.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        result = []
        for row in reader:
            response = list(zip(header, row))
            response = dict(response)
            result.append(response)
        return result
def get_populations():
    data = open_csv()
    population = []        
    for raw in data:
        population.append(
            [
                raw['Country/Territory'], float(raw['World Population Percentage']),
            ]
        )
    return population
def generate_pie_chart(population):
    labels = []
    values = []
    for country, value in population:
        labels.append(country)
        values.append(value)
    print(labels)
    print(values)
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    plt.show()
if __name__ == '__main__':
    generate_pie_chart(get_populations())