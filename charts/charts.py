import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['a','b','c','d']
    values = [15, 30, 45, 10]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie_chart.png')
    plt.close(fig)

