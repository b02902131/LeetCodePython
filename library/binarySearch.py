def binarySearch(list, target):
    left, right = 0, len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        middleValue = list[middle]
        if target == middleValue:
            return middle
        elif target > middleValue:
            left = middle + 1
        else:
            right = middle - 1
    return False

print (binarySearch([1,2,3,9,10,11,35,79], 3))