import arrays
import random

def range_array(start, stop, step=1):
    a_range = range(start, stop, step)
    length = len(a_range)
    an_array = arrays.Array(length, 0)
    for index in range(length):
        an_array[index] = a_range[index]
    return an_array

def array_cat(array1, array2):
    length = len(array1) + len(array2)
    combined = arrays.Array(length)
    # for i in range(length // 2):
    #     combined[i] = array1[i]

    # for i in range(length // 2, length):
    #     combined[i] = array2[i - length // 2]
    for i in range(len(array1)):
        combined[i] = array1[i]

    i2 = len(array1)
    for i in range(0, len(array2)):
        combined[i2] = array2[i]
        i2 += 1
    return combined

def random_array(size, min_value=0, max_value=None):
    an_array = arrays.Array(size, 0)
    if max_value is None:
        max_value = size

    for index in range(size):
        an_array[index] = random.randint(min_value, max_value)
    
    return an_array

def main():
    random.seed(1)
    rand_array = random_array(10)
    print(rand_array)


if __name__ == "__main__":
    main()