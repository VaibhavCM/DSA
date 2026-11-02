def consecutiveave(arr,k):

    n= len(arr)
    if k<= 0 or k>n:
        return None

    win_avg = sum(arr[:k])
    every_value = [win_avg/k]

    for right in range(k,n):

        win_avg -= arr[right-k]

        win_avg += arr[right]

        every_value.append(win_avg/k)
    return every_value

arr = [2,1,5,1,3,2]
k = 2

print(consecutiveave(arr,k))