def maxSum(arr, n, k):
    window_sum = sum(arr[i] for i in range(k))
    print(window_sum)
    max_sum = window_sum

    for i in range(0, n-k):
        print("time {}".format(i), arr[i], arr[i+k], window_sum)
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)

    return max_sum


arr = [80, -50, 90, 100]
n = len(arr)
k = 2

rs = maxSum(arr, n, k)
print(rs)
