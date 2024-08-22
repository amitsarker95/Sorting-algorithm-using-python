'''
Selection Sort Algorithm using min()

'''

arr = [7,3,5,2,1,6]

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_value = min(arr[i:])
        min_index = arr.index(min_value, i)
        if arr[i] != arr[min_index]:
            tmp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = tmp
    return arr

print(selection_sort(arr))


