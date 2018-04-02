#!/usr/bin/env python

arr = [1, 2, 3, 4, 5]
a = arr
a[3] = 2
print(arr) #[1, 2, 3, 2, 5]

arr = [1, 2, 3, 4, 5]
b = arr[3:8] #notice, in python3, even index 8 does not exist, it can still run
b[0] = 1
print()

