#3)Find the number of odd and even numbers present in the list.


l=[]
n=int(input("Enter number of elements : "))
for i in range(n):
    e=int(input("Enter an element : "))
    l.append(e)
print("The original list is",l)
odd=0
even=0
for i in l:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("The number of odd numbers in the list are",odd)
print("The number of even numbers in the list are",even)
