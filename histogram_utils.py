# Q: Write an import statement that imports the function pyplot from the module matplotlib and renames it to plt.

def build_histogram(data):
    def build_histogram(data):
  dic = {}
  for i in data:
    if i in dic:
      dic[i] += 1
    else:
      dic[i] = 1
  return dic

def plot_histogram(histogram):
    x_values = list(histogram.keys())
    y_values = list(histogram.values())

    plt.bar(x_values, y_values)
    plt.xlabel('Items')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()


