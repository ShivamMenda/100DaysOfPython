#tuples immutable and ordered
#Multiple items recognized if not put , to create tuple
t=("test","test1")
t=tuple(["test","1"])
#print(t)

#access elements
item=t[0]
item=t[-1]
#print(item)

#iteration
for i in t:
    print(i)

#len,count,index
print(len(t))
print(t.count('1'))
print(t.index('1'))

#convert to list
l=list(t)
print(l)

#slicing
t1=(1,2,3,4,5,6,7,8,9,10)
res=t1[2:5] #Last index not included
print(res)

#Unpacking
t="Max",28,"Boston"
name,age,city=t
print(name,age,city)

#Unpacking with numbers
t=(0,1,2,3,4)
i1,*i2,i3=t
print(i1) #First ele
print(i3) #last ele
print(i2) #everything else in between because of the *

#As Tuples are immutable python optimizes it and makes it more efficient than lists.