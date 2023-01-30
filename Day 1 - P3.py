'''
3. Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
 Starting with any positive integer, replace the number by the sum of the squares of its
digits.
 Repeat the process until the number equals 1 (where it will stay), or it loops endlessly
in a cycle which does not include 1.
 Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''

def happynumber(num):
   sum=0
   rem=0
   while(num>0):
       rem=num%10
       sum=sum+(rem*rem)
       num=num//10
   return sum
num=int(input("Enter a number : "))
result=num
while(result!=1 and result!=4):
    result=happynumber(result)
if(result==1):
    print(str(num)+" is a happy number.")
elif(result==4):
    print(str(num)+" is not a happy number.")
