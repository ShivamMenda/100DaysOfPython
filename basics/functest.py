# def greet():
#     print("hey there")
#     print("How you doing")
#     print("this is test")

# greet()

#with input

# def greet1(name):
#     print(f"hello {name}")
#     print(f"test {name}")

# print("Enter name")
# name1=str(input())
# greet1(name1)

#Function with more than one input

from unicodedata import name


def greet_with(name,location):
    print(f"Hello {name}")
    print(f"How is it at {location}")

print("Enter name and loc")
name=str(input())
loc=str(input())
greet_with(name,loc)

