'''
1) Given two strings “s” and “t”, determine if they are isomorphic. Two
strings “s” and “t” are isomorphic if the characters in “s” can be replaced to get “t”. All
occurrences of a character must be replaced with another character while preserving the order
of characters. No two characters may map to the same character, but a character may map to
itself.

'''

s=input("Enter string 1 : ")
t=input("Enter string 2 : ")
if len(s)!= len(t):
    print("False, the given strings",s,"and",t,"are not isomorphic.")
else:
    a,b={},{}
    for i in range(len(s)):
        ch1,ch2=s[i],t[i]
        if ch1 not in a:
            a[ch1]=ch2
        if ch2 not in b:
            b[ch2]=ch1
        if a[ch1]!=ch2 or b[ch2]!= ch1:
             print("False, the given strings are not insomorphic.")
             break
    else:
        print("True , the given strings",s,"and",t,"are isomorphic.")
