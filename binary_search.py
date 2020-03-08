#Important to note that binary search works on sorted list
#Binary search using iterative methods - returns the index of the number while recursive tell if its present

def IterativeBinarySearch(arr, key):
    low = 0
    high = len(arr)-1
    
    while (low <= high):
        mid = (low + high)//2

        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return "Key not found"

print(IterativeBinarySearch([2,3,4,5], 5))

def RecursiveBinarySearch(arr, key):
    low, high = (0, len(arr)-1)
    if low == high:
        if arr[low] == key:
            return key 
        else:
            return "Key not found"
    else:
        mid = (low+high)//2

        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return RecursiveBinarySearch(arr[:mid], key)
        else:
            return RecursiveBinarySearch(arr[mid+1:], key)

print(RecursiveBinarySearch([2,3,4,5,6,7,8,9],10))
print(IterativeBinarySearch([2,3,4,5,6,7,8,9],10))

