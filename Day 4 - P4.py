s=input("Enter a string : ")
s1=''
for i in s:
    if i.isalpha():
        s1+=i
if s1[::1].lower()==s1.lower():
    print(s,'is a palindrome.')
else:
    print(s,'is not a palindrome.')
