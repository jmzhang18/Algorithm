#!/usr/bin/env python

def rotateMatrix(mat=[[]]):
	result = [[0 for j in range(len(mat[i]))] for i in range(len(mat))]
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			result[j][len(mat[i])-1-i] = mat[i][j]
	return result

print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))
