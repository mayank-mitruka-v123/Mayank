#PALINDROME
n=int(input("Enter number:"))
temp=n
rev=0
while(temp>0):
    rem=temp%10;
    rev=rev* 10+rem
    temp=temp//10
if n==rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
