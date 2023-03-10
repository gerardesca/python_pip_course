import utils
import read_csv
import charts
import pandas as pd

def run():

  # esta es una forma de leer un archivo csv y filtrar con map
  '''
  # leer la data del archivo csv
  data = read_csv.read_csv('./data.csv')

  # filtrar por continente America del sur
  data = list(filter(lambda item : item['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''

  # aqui se utiliza la libreria pandas para realizar lo anterior
  data = read_csv.read_csv('./data.csv')
  df = pd.read_csv('./data.csv')
  df = df[df['Continent'] == 'Africa']
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  # filtrar data de acuerdo a un país
  country = input('Type Country => ')

  # retorna una lista con un diccionario
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    # se utiliza el item 0, es decir, el primer diccionario
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  else:
    print('The country does not exists')

  # graficar pporcentaje de poblacion por pais
  '''
  # no se utiliza con el modulo de pandas
  countries, percentages = utils.percent_by_country(data)
  '''
  charts.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
  run()