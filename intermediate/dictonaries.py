#Dictionary: Key value pairs,Unordered,Mutable

mydict={"name":"Shivam","age":28}
print(mydict)

value=mydict["name"] #To print values use key name
print(value)

mydict["email"]="s@test.com" #mutable
print(mydict)

mydict.pop("age") #remove by key name
print(mydict)

#To check wether key present 
try:
    print(mydict["lastname"])
except:
    print("Error")

for key,value in mydict.items(): #to loop over values and for keys
    print(key,value)

mydict2=mydict.copy() #copy
print(mydict2)