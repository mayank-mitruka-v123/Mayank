#2) Find the sum of all the numbers present in the list.

l=[]
n=int(input("Enter number of elements : "))
for i in range(n):
    e=int(input("Enter an element : "))
    l.append(e)
print("The original list is",l)
s=0
for i in l:
   s=s+i
print("The sum of all integers present in", l , " is " , s) 
