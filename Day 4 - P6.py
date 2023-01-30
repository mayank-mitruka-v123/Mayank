def delchar(s,c):
    if len(c)!=1:
        return s
    else:
        return s.replace(c,'')

s=input("Enter a string : ")
c=input("Enter the letter to be deleted : ")
print(delchar(s,c))

