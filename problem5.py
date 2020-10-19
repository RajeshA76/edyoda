#!/usr/bin/python3

arr = list(map(int, input().split()))
value = int(input())
# Write your code here
length = len(arr)
stop = value
start = 0
lis  = []
while stop < length + 1:
	temp = []
	for i in range(start,stop):
		temp.append(arr[i])
	lis.append(temp)
	stop = stop + 1
	start = start + 1
lis.sort()
print(lis[-1])


