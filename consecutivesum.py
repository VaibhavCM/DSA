def slide_sum(arr,k):
    n = len(arr)

    if k<=0 or k>n :
        return None

    Window_sum = sum(arr[:k])
    max_sum = Window_sum

    for right in range(k,n):

        Window_sum -= arr[right-k]

        Window_sum += arr[right]

        max_sum = max(max_sum,Window_sum)

    return max_sum

arr = [8819, 674, 8816, 7705, 5699, 5383, 6177, 2113, 1992]
k = 1

print(slide_sum(arr,k))