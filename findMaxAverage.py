def findMaxAverage(arr,k):
    win_sum = sum(arr[:k])
    max_sum = win_sum

    for right in range(k,len(arr)):
        win_sum -= arr[right-k]
        win_sum += arr[right]

        max_sum = max(max_sum,win_sum)

    return max_sum/k
arr = [1,12,-5,-6,50,3]

k = 4

print(findMaxAverage(arr,k))