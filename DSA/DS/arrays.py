#1-D array

# print("enter n")
# n=int(input())
# arr=[]
# print(f"Enter {n} elements")
# for i in range(n):
#     arr.append(int(input()))

# print("The elements are")
# for i in range(n):
#     print(arr[i],end=" ")

#2-D array
# r=int(input())
# c=int(input())
# arr=[[0 for col in range(c)] for row in range(r)]

# for row in range(r):
#     for col in range(c):
#         arr[row][col]=row*col
# print(arr)

#Delete an element


n=int(input())
arr=[]
print(f"Enter {n} elements")
for i in range(n):
    arr.append(int(input()))

val=int(input("Enter ele to delete:"))
try:
    arr.remove(val)
except:
    print("Element not found")
print(arr)

ind=int(input("Enter index"))
try:
    arr.pop(ind)
except:
    print("Index not found")
print(arr)

print("After Sorting")
arr.sort()
print(arr)

#to search an ele
ele=int(input("Enter ele to find:"))
try:
    print(arr.index(ele))
except:
    print("Does not exist")




