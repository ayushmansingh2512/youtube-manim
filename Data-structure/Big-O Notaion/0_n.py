def linear_search(arr,k):
	for i in range(len(arr)):
		if arr[i] != k:
			print(f"{arr[i]} not equal to {k}")
		if arr[i] == k:
			return True
			break
		
	return False
arr = [1,2,3,4,5,6,7,8,9]
target = 9
print(linear_search(arr,target))

arr.insert(8,100)
print(arr)