n1=int(input("Enter number 1 : "))
n2=int(input("Enter number 2 : "))
s=0
p=0
for i in range(1,min(n1,n2)):
    if n1%1==0 and n2%i==0:
        s=n1+n2
        p=n1*n2
if s>0:
    if p%s==0:
        print("Yeah")
    else:
        print("Nah")
