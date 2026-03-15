import random as r

def randarr(num):
    return r.sample(range(1, num+1), num)


def bubble_sort(arr):
    array = arr[:]
    for j in range(len(array)-1):
        swapped = False
        for i in range(len(array)-j-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        if not swapped:
            break
    return array


def bubble_sort_basic(arr):
    array = arr[:]
    for j in range(len(array)-1):
        for i in range(len(array)-j-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array


def selection_sort(arr):
    array = arr[:]
    k = len(array)
    for count in range(k):
        least = array[count]
        ind = count

        for i in range(count, k):
            if array[i] < least:
                least = array[i]
                ind = i

        array[count], array[ind] = array[ind], array[count]

    return array


def insertion_sort(arr):
    array = arr[:]
    l = len(array)

    for i in range(1, l):
        current_value = array[i]
        current_index = i

        for j in range(i-1, -1, -1):
            if array[j] > current_value:
                array[j+1] = array[j]
                current_index = j
            else:
                break

        array[current_index] = current_value

    return array
