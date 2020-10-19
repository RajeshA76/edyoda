#!/usr/bin/python3
password=input()
# Write your code here
sp_c = ["!","@","#","$","&"]
numbers = []
for i in range(10):
	numbers.append(str(i))
for i in password:
	if i in sp_c:
		sp = "True"
		break
	else:
		sp = "False"
		
	
for i in password:
	if i in numbers:
		num = "True"
		break
	else:
		num = "False"
	
for i in password:
	if i.isupper():
		upr = "True"
		break
	else:
		upr = "False"
	
	
if len(password) < 8 or upr == "False" or num == "False" or sp == "False":
	print("Weak")
elif not(len(password) < 8 or upr == "False" or num == "False" or sp == "False"):
	print("Strong")
	
if len(password) < 8:
	print("The length of the password must be at least 8 characters in length")
if upr == "False":
	print("The password must contain at least 1 capital letter")
if num == "False":
	print("The password must contain at least 1 digit")
if sp == "False":
	print("The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)")
