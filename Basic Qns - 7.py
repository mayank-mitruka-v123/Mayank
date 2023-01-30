#3) Replace the 3rd number in the tuple t=(1,76,63,7,3) to 8.
t=(1,76,63,7,3)
print(t,"is the original tuple\n")

#Creating a temporary tuple (will be used to pack the elements)
temp=()

#unpacking the tuple
a,b,c,d,e=t[0],t[1],t[2],t[3],t[4]

#Type casting the tuple into a list in a new variable
l=list(t)

l[2]=8

#Packing the tuple
for i in l:
    temp+=(i,)
print(temp,"is the temporary variable.\n")

#Equating the temporary tuple to the original tuple
t=temp

#Printing the tuple
print(t,'is the altered tuple.')
