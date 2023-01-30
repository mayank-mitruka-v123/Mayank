n=int(input("Enter number of elements : "))
l=[]
for i in range(n):
    l.append(int(input("Enter an element : ")))
print(l,'is the original list')
mx=0
for i in l:
    if i>mx:
        mx=i
pos=0
for i in range(n):
    if l[i]==mx:
        pos=i
print(mx,'is the largest number present at index',pos)
