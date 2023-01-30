 # 9) Create a dictionary and print the key value pairs.
d={}
n=int(input("enter no. of students : "))
for i in range(n):
    d['Name']=input("Enter name : ")
    d['Roll no.']=int(input("Enter roll no. : "))
for i in d.items():
    for j in i:
        print(j,sep='-')
