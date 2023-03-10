import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

def run():
  labels = ['a', 'b', 'c']
  values = [10, 20, 30]
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
  
if __name__ == '__main__':
  run()