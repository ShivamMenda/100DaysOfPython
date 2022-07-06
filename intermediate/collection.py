#collections: Counter,namedTuple,OrderedDict,defaultdict,deque

from collections import Counter
a="aaaabbbccc"
c=Counter(a)
print(c.items()) #list of keys and values
print(c.most_common(1)) #List of tuples with the no most common element
print(c.most_common(1)[0][0]) #to extract from tuple
print(list(c.elements()))

from collections import namedtuple
#Structs from C in python
point=namedtuple('point','x,y')
pt=point(1,-4)
print(pt)

#remembers the order the elements were inserted in the dict
from collections import OrderedDict
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4 
print((od))

#same as dict but gives default value if key not present
from collections import defaultdict
d=defaultdict(int)
d['a']=1
d['b']=2
d['c']=3
print(d['d'])

from collections import deque
#double ended queue
d=deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.pop()
d.popleft()
d.clear()
d.extend([4,5,6])
d.extendleft([1,2,3])
d.rotate(1)
d.rotate(-1) #rotate left
print(d)