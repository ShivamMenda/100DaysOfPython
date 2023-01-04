#Cracking the Coding Interview
#Arrays and Strings

#1.1 IsUnique

def isUnique(a):
    for i in a:
        if(a.count(i)==1):
            return True
        else:
            return False

# s=str(input("Enter String to check:"))
# print(isUnique(s))

#1.3 URLify
def urlify(a):
    return a.strip().replace(" ","%20")

# a=str(input("Enter"))
# print(urlify(a))








