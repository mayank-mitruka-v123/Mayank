# 9. SWAPPING
a=[]
n= int(input("Enter the number of elements in list : "))
for i in range(0,n):
    element = int(input("enter element" + str(i+1) +":"))
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("New list is:",a)
