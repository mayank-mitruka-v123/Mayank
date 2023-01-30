def solve(nums):
   count=0
   n=len(nums)
   for i in range(n):
      for j in range(i+1,n):
         if nums[i] == nums[j]:
            count+=1
   return count

l=[]
n=int(input("Enter number of elements : "))
for i in range(n):
    l.append(int(input("Enter value"+str(i+1)+":")))
print(solve(l))
