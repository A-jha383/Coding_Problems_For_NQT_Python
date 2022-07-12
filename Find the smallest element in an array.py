arr = [13, 14, 16, 10, -111]


def find_smallest_number():
    temp = arr[0]
    x = len(arr)
    i = 1
    while i < x:
        if temp > arr[i]:
            temp = arr[i]
        i = i + 1
    return temp


def find_largest_number():
    temp = arr[0]
    x = len(arr)
    i = 1
    while i < x:
        if temp < arr[i]:
            temp = arr[i]
        i += 1
    return temp


print(f'smallest number is :{find_smallest_number()}.')
print(f'Largest Number is : {find_largest_number()}')
