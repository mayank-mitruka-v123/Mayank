#1) Create a dictionary by keeping the keys as names of your class members and values as their roll number.
d={}
n=int(input("enter no. of students : "))
for i in range(n):
    d[input("Enter name : ")]=int(input("Enter roll no. : "))
print(d)
