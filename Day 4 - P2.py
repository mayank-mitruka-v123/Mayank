ch='yes'
while  ch=='yes':
    t=int(input("Enter total number of users : "))
    if t==0 or t<0:
        print("Invalid input.Try again.")
        continue
    
    s=int(input("Enter number of staff users : "))
    n=s//3
    if t<s:
        print("Invalid input.")
    if t==s:
        print("Number of student users are : ",t-(s-n))
    else:
        print("Number of student users are : ",t-s-n)
    ch=input("Do you want to continue? (yes/no) : ")
    print()
else:
    print("End of program.")
