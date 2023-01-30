def groupAnagrams(l):
    anagrams = []
    if not l:
        return anagrams
    nums = [''.join(sorted(word)) for word in l]
    d = {}
    for i, e in enumerate(nums):
        d.setdefault(e,[]).append(i)
 
    for index in d.values():
        collection = list(l[i] for i in index)
        if len(collection) > 1:
            anagrams.append(collection)
 
    return anagrams ,collection

l=[]
n=int(input("Enter number of elements : "))
for i in range(n):
    l.append(input("Enter value"+str(i+1)+":"))
print(l,'is the list containing values.')
 
anagrams = list(groupAnagrams(l))
print(anagrams)
