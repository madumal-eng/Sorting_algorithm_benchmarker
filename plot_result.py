import matplotlib.pyplot as plt


def plot(numbers, bubble, bubble_basic, selection, insertion, python_sort):

    plt.plot(numbers, bubble, marker=".", label="Optimized Bubble Sort")
    plt.plot(numbers, bubble_basic, marker=".", label="Basic Bubble Sort")
    plt.plot(numbers, selection, marker=".", label="Selection Sort")
    plt.plot(numbers, insertion, marker=".", label="Insertion Sort")
    plt.plot(numbers, python_sort, marker=".", label="Python Sort")

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time")
    plt.title("Sorting Algorithm Benchmark")
    plt.legend()
    plt.grid(True)

    plt.show()