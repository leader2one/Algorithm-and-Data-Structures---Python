def binary(arr, target):
	iterations = 0
	left = 0
	right = len(arr)-1
	while (left <= right):
		iterations += 1 # number of steps
		mid = (left+right)//2
		if arr[mid]==target:
			return mid
		elif arr[mid]<= target:
			left = mid + 1
		else :
			right = mid - 1
	retrun -1