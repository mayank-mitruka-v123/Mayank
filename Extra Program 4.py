#4) Python 3 code to demonstrate removing duplicates from list with SET
a=()
n=int(input("Enter the number of elements : "))
for x in range(0,n):
    element=int(input("Enter element” + str(x+1) "))
    a+=(element,)
print(a,'is the original tuple')
b=set()
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("List with Non-duplicate elements:")
print(unique)
print(b)
