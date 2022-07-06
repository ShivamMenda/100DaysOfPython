#sets: Unordered, mutable no duplicates

myset={1,2,3} #Created with curly braces
myset=set([1,2,3,1]) #to elimate duplocates
myset.add(4) #to add the elements in a set
myset.remove(4) #to remove ele
myset.discard(3) #another way to remove
myset.pop() #Remove first ele
print(myset)

for i in myset: 
    print(i)

setA={1,2,3,4,5}
setB={1,2,3}
print(setB.issubset(setA)) #To check subsets

#frozen sets

a=frozenset([1,2,3,4]) #immutable
