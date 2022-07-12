arr=[12,65,22,34,18,17]
def find_2nd_smallest_number():
    if arr[0] > arr[1]:
        temp = arr[1]
        val = arr[0]
    else:
        temp = arr[0]
        val = arr[1]

    x = len(arr)
    i = 2
    while i < x:
        if temp > arr[i]:
            val = temp
            temp = arr[i]
        elif val > arr[i]:
            val = arr[i]
        i = i + 1
    return val


def find_2nd_largest_number():
    if arr[0] < arr[1]:
        temp = arr[1]
        val = arr[0]
    else:
        temp = arr[0]
        val = arr[1]

    x = len(arr)
    i = 2
    while i < x:
        if temp < arr[i]:
            val = temp
            temp = arr[i]
        elif val<arr[i]:
            val =arr[i]
        i = i + 1
    return val

print(f'smallest number is :{find_2nd_smallest_number()}.')
print(f'Largest Number is : {find_2nd_largest_number()}')