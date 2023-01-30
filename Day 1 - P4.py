'''
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
'''
n=int(input("Enter a number : "))
tn=n
rev=0
while tn>0:
    rem=tn%10
    rev=rev*10+rem
    tn=tn//10
    
if n==rev:
    print(n,'is a palindrome.')
else:
    print(n,'is not a palindrome.')
