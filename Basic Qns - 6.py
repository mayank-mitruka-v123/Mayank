#6) Add elements in the given tuple t=(3,54,6)
t=(3,54,6)
n=int(input("Enter number of elements to be added : "))
for i in range(n):
    e=int(input("Enter an element : "))
    t+=(e,)
print(t,"is the new tuple")
