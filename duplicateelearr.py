def duplicate(arr):
    arr.sort()
    result = []
        
    left = 0
    right = left+1
    last = len(arr)
        
    while right < last:
        if arr[left] == arr[right]:
            result.append(arr[left])
            left += 1
            right += 1
        else:
            left += 1
            right += 1
    return result

print(duplicate([2, 3, 1, 2, 3]))



