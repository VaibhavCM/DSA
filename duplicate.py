# Brute Force
# def duplicate(arr,k):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i] == arr[j] and abs(i-j) <= k:
#                 return True

#     return False 


def duplicate(arr,k):
    window = set()
    left = 0

    for num in arr:
        if num in window:
            return True

        window.add(num)

        if len(window) > k:
            window.remove(arr[left])
            left += 1

    return False
arr = [1, 2, 3, 1]
k = 3
print(duplicate(arr,k))