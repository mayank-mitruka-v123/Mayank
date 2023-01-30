'''
2) Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a
list [odd,even], where odd is the sum of squares of all the odd numbers in l and even is the
sum of squares of all the even numbers in l.
'''

def sumsquare(l):
    os=0 #4
    es=0 #1
    a=[]
    for i in l:
        if i%2==0:
            es+=i**2
        else:
            os+=i**2
    a.append(os)
    a.append(es)
    return a # a= [1,4]

# Main Segment 
n=int(input("Enter number of integers : "))
a=[]
for i in range(n):
    a.append(int(input("Enter a integer : ")))
print(a,"is the original list.")
s=sumsquare(a)
print(s)
