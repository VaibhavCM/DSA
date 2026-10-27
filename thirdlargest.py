def thirdlargest(arr):
    arr.sort(reverse = True)
    for i in range(len(arr)):
        if len(arr) > 2:
            return arr[2]
        else:
            return -1
    return arr

print(thirdlargest([1,5,6,9,7]))