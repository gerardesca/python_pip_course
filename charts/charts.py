import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['Argentina', 'Mexico', 'Spain']
    values = [3,0,1]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()