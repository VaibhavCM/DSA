def swap(arr,k):
    start = 0
    n = len(arr)
    while start < n:
        left = start
        right = min(start+k-1,n-1)

        while left < right :
            arr[left], arr[right] = arr[right] , arr[left]

            left += 1
            right -= 1
        start += k
        
    return arr

print(swap([1,2,3,4,5],3))