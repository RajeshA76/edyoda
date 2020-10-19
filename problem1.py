#!/usr/bin/python3

n = int(input())
# Write your code here
keys = []
values = []
for i in range(n):
	inp = input().split(" ")
	keys.append(inp[0])
	values.append(inp[1])

dict = {}
for i in range(n):
	dict[keys[i]] = values[i]




same = []
for i in keys:
   if i not in values:
        same.append(i)
for i in values:
    if i not in keys:
        same.append(i)
sequence = []
for i in same:
    if  i not in values:
        sequence.append(i)

f = dict[sequence[0]]
for i in range(n):
    if f in keys:
        sequence.append(f)
        f = dict[sequence[i + 1]]
s_dict = {}
for i in sequence:
    s_dict[i] = dict[i]


print(s_dict)
