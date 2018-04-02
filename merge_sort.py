#!/usr/bin/env python
import copy
def merge(arr, left, median, right):
	n1 = median - left +1 
	n2 = right - median
	print("arr: ", arr)
	print("merging: {},{},{}".format(left, median, right))
	left_array = list()
	right_array = list()
	if (left==median):
		left_array.append(arr[left])
	else:
		left_array = arr[left:(median+1)]

	if (right==(median+1)):
		right_array.append(arr[right])
	else:
		right_array = arr[(median+1):(right+1)]

	print("left_array: ", left_array)
	print("right_array: ", right_array)

	i = 0
	j = 0
	k = left
	while (i<n1 and j < n2):
		if (left_array[i] < right_array[j]):
			arr[k] = left_array[i]
			i += 1
		else:
			arr[k] = right_array[j]
			j += 1
		k+=1
	while (i < n1):
		arr[k] = left_array[i]
		i+=1
		k+=1

	while(j < n2):
		arr[k] = right_array[j]
		j+=1
		k+=1

def merge_sort(arr, left, right):
	if (left<right):
		median = (left+right)//2
		# print("merging: {},{},{}".format(left, median, right))
		merge_sort(arr, left, median)
		merge_sort(arr, median+1, right)
		# print("merging: {},{},{}".format(left, median, right))
		merge(arr, left, median, right)


arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr, 0, len(arr)-1)
print(arr)
