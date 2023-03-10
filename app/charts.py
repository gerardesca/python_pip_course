import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

def run():
  labels = ['a', 'b', 'c']
  values = [10, 20, 30]
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
  
if __name__ == '__main__':
  run()