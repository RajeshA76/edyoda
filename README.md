#Edyoda Assignment 1

Problem 1: Find Sequence of travel

==================================================================================================================================================================
You will be given an integer number of elements and for next n lines space separeted key value pairs. make a dict from strings of tickets("to":"from"). find out the sequence of travel. Assuming that there will be only one starting point for the journey.

Input Format:

You will be given an integer number of elements and for next n lines space separeted key value pairs

Output Format:

Print The dictionary fro the sequence of travel.

Sample Input 0:

{"Chennai":"Bangalore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}

Sample Output 0:

{'Bombay':'Delhi','Delhi':'Goa','Goa':'Chennai','Chennai':'Banglore'}
******************************************************************************************************************************************************************
Problem 2: Count number of line inside a code

==================================================================================================================================================================
You will be given a code in string format. 

Write a program utility that counts the number of lines of actual python code in a. For the purpose of this exercise, a line is counted if it contains something other than whitespace or text in a comment.

remember that comment start sequences that appear inside python strings should be ignored.

Input Format:

The first line containe total number of line and for next n line there will be code strings either comment or code or blank line

Output Format:

print number of lines for code only

Sample Input 0:

#Linear search implementation
#Takes list and a key as input and returns True or False as answer
def linear_search(l,key):
    for value in l:
        if key == value:
            return True #Return True is key exist
    else:
        return False #Return False if key does not exist

l = [100,200,300,400,500,600]
key = 500
result = linear_search(l,key)
print(result)

Sample Output 0:
10
******************************************************************************************************************************************************************
Problem 3: Password Validation
==================================================================================================================================================================
You will be given a string. Write a program to check the strength of a supplied password.

Feebacks:

1. The length of the password must be at least 8 characters in length
2. The password must contain at least 1 capital letter
3. The password must contain at least 1 digit
4. The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)

We need to provide feedback to the user about the strength of their password

Provide the user with a list of reasons why their password is 'weak'      

 Note: Order for feedback should be same as given.                                                    

Input Format:

THe first line contains string password
Output Format:

print the status weeak or strong in wst line in next few lines print feedback

Sample Input 0:
abc12

Sample Output 0:
Weak
The length of the password must be at least 8 characters in length
The password must contain at least 1 capital letter
The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)   
******************************************************************************************************************************************************************Problem 4: Find list where adjacent values sum is even

==================================================================================================================================================================
Given a list of N integers. The task is to eliminate the minimum number of elements such that in the resulting list the sum of any two adjacent values is even.

Numbers = [1, 3, 5, 4, 2]
Output = [1, 3, 5]
Total elements removed 2
Elements to be removed [4,2]

Input Format:

One line containe space separated list elements

Output Format:

print the result list

Sample Input 0:
1 3 5 4 2

Sample Output 0:
[1, 3, 5]
******************************************************************************************************************************************************************Problem 5: Find sub array

==================================================================================================================================================================
Given an array arr[] of integers and an integer K, the task is to find the greatest contiguous sub-array of size K. 

Sub-array X is said to be greater than sub-array Y if the first non-matching element in both the sub-arrays has a greater value in X than in Y.

For example :
Input: arr[] = [1, 4, 3, 2, 5], K = 4
Output: 4 3 2 5
Two subarrays are [1, 4, 3, 2] and [4, 3, 2, 5]. First non-matching element from array1 and array 2 : 1 and 4 as 4 is greater
Hence, the greater one is [4, 3, 2, 5]

Input Format:

First line will have space separated elements of list. Second line contains value.

Output Format:

print the required list

Sample Input 0:

1 4 3 2 5
3

Sample Output 0:
[4,3,2]
******************************************************************************************************************************************************************
