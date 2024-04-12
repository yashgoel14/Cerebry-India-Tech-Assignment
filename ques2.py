def LongSubarrSum(arr, N, k):
    d = {}  
    maximum_length = 0
    sum = 0

    for i in range(N):
        sum += arr[i]

        if sum == k:  
            maximum_length = i + 1
            
        if sum - k in d:
            maximum_length = max(maximum_length, i - d[sum - k])

        if sum not in d:
            d[sum] = i

    return maximum_length

arr = list(map(int,input().split()))
n = len(arr)
k = int(input())
print(LongSubarrSum(arr, n, k))

# time complexity : O(n)
# space complexity : O(n)