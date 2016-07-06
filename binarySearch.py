
def binarySearch(array, item):
    low = 0
    high = len(array)-1
    mid = (high + low) // 2
    found = False
    while not found and high>=low:
        midItem = array[mid]
        if midItem == item:
            found = True
            return mid
        elif midItem < item:
            low = mid + 1
        elif midItem > item:
            high = mid - 1
        mid = (high + low) // 2
    return -1 #not found


