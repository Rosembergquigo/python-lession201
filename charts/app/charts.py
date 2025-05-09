import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [10, 20, 15]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)