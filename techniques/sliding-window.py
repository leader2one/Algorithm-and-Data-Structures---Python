#  Given a array and integer k.
# task : to find the largest sum of consecutive k 
# elements in array using the technique sliding window
def maxsum(arr, k):
	n = len(arr)
	window_sum = sum([arr[i] for i in range(k)])
	max_sum = window_sum
	for i in range(n-k):
		window_sum = window_sum-arr[i]+arr[i+k]
		max_sum = max(window_sum, max_sum)
	return max_sum

arr = [1,10,3,2]
k = 2
print(maxsum(arr,k))
