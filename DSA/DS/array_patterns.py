#Sum of Subarray within a range of indices(Partial sum trick)
inp=[]
n=int(input("Enter len of list"))
for i in range(n):
    inp.append(int(input(f"enter inp[{i}]")))
s=[]
s.append(inp[0])
for i in range(1,n):
    s.append(s[i-1]+inp[i])
print(s)
a=int(input(("Enter first index:")))
b=int(input(("Enter second index:")))
print(f"The sum between index {a} and index {b} is {s[b]-s[a-1]}")

#Frequency Array(2 Methods)
inp=list(map(int,input("Enter list:").split()))
fr=[]
cnt=0
for i in range(max(inp)+1):
    fr.append(0)
for i in range(len(inp)):
    if(fr[inp[i]]==0):
        cnt+=1
    fr[inp[i]]+=1
print(cnt)
print(len(set(inp))) 

#Max Subarray Sum
a=list(map(int,input("Enter list:").split()))
s=[]
m=0
s.append(a[0])
for i in range(1,len(a)):
    if(s[i-1]+a[i]>0):
        s.append(s[i-1]+a[i])
    else:
        s.append(0)
print(s)
print(max(s))



