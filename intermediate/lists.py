#lists basics
mylist=["cherry","banana"]
print(mylist)
mylist2=list()
print(mylist2)

#indexes start from 0
item=mylist[0]
print(mylist[-1])
print(item)

#To iterate
for i in mylist:
    print(i)

if "banana" in mylist:
    print("yes")
else:
    print("no")

# append and len insert
print(len(mylist))
mylist.append("lemon")
print(mylist)
print(len(mylist))
mylist.insert(1,"test")
print(mylist)

#pop and remove
mylist.pop()
print(mylist)
mylist.remove("test")
print(mylist)

#reverse and sort
mylist.reverse()
print(mylist)
l=[4,5,1,2]
l.sort()
print(l)

#tricks
l=[0]*5
print(l)
l1=[1,2,3]
print(l+l1)

#slicing
l=[1,2,3,4,5,6,7,8,9]
a=l[1:5]
a=l[:5]
a=l[::-1]
print(a)

#one liners
l2=[1,2,3]
l3=[i*i for i in l2]
print(l3)

