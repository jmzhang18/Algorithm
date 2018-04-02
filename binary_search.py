#!/usr/bin/env python

def binary_search(data, target):
	right = len(data)-1
	left = 0
	medium = (right+left)//2
	it = 0
	while (left!=right and data[medium]!=target):
		if (data[medium] < target):
			left = medium
		else:
			right = medium
		medium = (right+left)//2
		it+=1
	return medium, it

print(binary_search([1,3,4,5,6,7,8,9], 8))

