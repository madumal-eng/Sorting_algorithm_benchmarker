import time
from sorting_algorithms import *
import plot_result


def measure(func, arr):
    start = time.perf_counter()
    func(arr)
    end = time.perf_counter()
    return end - start


def run_benchmark(end):

    numbers = []
    bubble_time = []
    bubble_basic_time = []
    selection_time = []
    insertion_time = []
    python_sort_time = []

    for i in range(2, end+1):

        arr = randarr(i)

        bubble_time.append(measure(bubble_sort, arr))
        bubble_basic_time.append(measure(bubble_sort_basic, arr))
        selection_time.append(measure(selection_sort, arr))
        insertion_time.append(measure(insertion_sort, arr))
        python_sort_time.append(measure(sorted, arr))

        numbers.append(i)

    plot_result.plot(numbers,
                      bubble_time,
                      bubble_basic_time,
                      selection_time,
                      insertion_time,
                      python_sort_time)


if __name__ == "__main__":
    end = int(input("Enter range: "))
    run_benchmark(end)
