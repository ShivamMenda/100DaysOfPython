# Strings: ordered, immutable, text representation

s="Hello world" #use "" or ''
print(s)

char=s[-1] #like list put index
print(char)

#slicing
sub=s[1:5] # slicing [start:stop:step] last index not included
sub=s[:5] # Default start 0
sub=s[1:] # default end len(string)
sub=s[0::2] #Every even occurence using step factor
sub=s[::-1] #trick to reverse
#print(sub)

# #concat
# s1="test"
# res=s+" "+s1
# print(res)

# #iterate
# for i in s:
#     print(i)

# String methods
s='    Hello     '
s=s.strip()
s=s.upper()
s=s.lower()
# print(s.startswith("h"))
# print(s.endswith('o'))
# print(s.find("o"))
# print(s.find("ll"))
# print(s.count("l"))
# print(s.replace("hello","hell")) #Does not change original
# print(s)

#Strings and lists
s='how,are,you,doing'
l=s.split(",") # Default is "" (string to list)
s1=" ".join(l) #list to string
print(l)
print(s1)

my_list=["a"]* 6
print(my_list)
# add
s=""
# for i in my_list:
#     s+=i
# print(s)
s="".join(my_list)
print(s)

#format
