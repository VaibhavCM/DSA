def alterarray(arr):
    result = []
    for i in range(len(arr)):
        if i%2 == 0:
            result.append(arr[i])
    return result

print(alterarray([1,2,3,5,6,7,5,6,9]))