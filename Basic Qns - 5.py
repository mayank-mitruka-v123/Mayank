#5) Create a tuple with 'n' integers.

t=()
n=int(input("Enter number of elements : "))
for i in range(n):
    e=int(input("Enter an element : "))
    t+=(e,)
print("The tuple is",t)
