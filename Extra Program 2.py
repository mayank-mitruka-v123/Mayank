# 2) Python program to demonstrate Addition of elements in a List
# Creating a List
List = []
print(List)

# Addition of Elements in the List using Function
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)
List.insert(2, 12)
List.pop()

# Adding elements to the List using Iterator
for i in range(1, 4):

    List.append(i)
print(List)

# Addition of List to a List
List2 = ['For', 'Sample']
List.append(List2)
print(List)
