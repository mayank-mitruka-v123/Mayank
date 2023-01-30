def smallernumberthancurrent(l):
    count=[0]*len(l)
    for i in range(len(l)):
        for j in range(len(l)):
            if l[j]<l[i]:
                count[i]+=1
    return count
n=int(input("Enter number of elements : "))
l=[]
for i in range(n):
    l.append(input("Enter an element : "))

print(smallernumberthancurrent(l))
