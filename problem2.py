#!/usr/bin/python3

n  = int(input())
code =''
lines=[]
for _ in range(n):
    line = input()
    lines.append(line)
code= '\n'.join(lines)
# Write your code here
code_split = code.split("\n")
for i in range(len(code_split)):
	code_split[i].replace("\t","")

appending = []
for i in code_split:
	if i[0:1] == "#" or i == "" or i[0:5] == "    #" or i[0:10] == "        #":
		appending.append(i)

final = []
for x in code_split:
	if x not in appending:
		final.append(x)

print(len(final))
