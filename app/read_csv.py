import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',') # iterable
    header = next(reader) # primer linea del archivo csv
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

def run():
  data = read_csv('./project/data.csv')
  print(data[0])

if __name__ == '__main__':
  run()