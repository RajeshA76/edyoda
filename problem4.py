#!/usr/bin/python3
arr = list(map(int, input().split()))
# Write your code here
arr1 = arr[0:]
pos = 1
position = 0
while position < len(arr) - 1:
    if (arr[position] + arr[position + 1]) % 2 == 0:
        position += 1
    else:
        if arr[position + 1] % 2 == 0:
        	arr.remove(arr[position + 1])
        else:
        	arr.remove(arr[position])


while pos < len(arr1) :
    if (arr1[pos] + arr1[pos - 1]) % 2 == 0:
        pos += 1
    else:
    	if arr1[pos] % 2 != 0:
    		arr1.remove(arr1[pos])
    	else:
    		arr1.remove(arr1[pos - 1])
    		if pos != 1:
    			pos -= 1
        

print(arr)
print(arr1)
if len(arr1) > len(arr):
    print(arr1)
else:
    print(arr)

