class User:
    def __init__(self,user_id,username): #Constructors
        self.user_id=user_id
        self.username=username
        self.followers=0 #default without passing
        self.following=0
    
    def follow(self,user):
        user.followers+=1
        self.following+=1


        
user_1=User("001","Shivam")#Pass in inital values
user_2=User("002","test")
print(user_1.user_id,user_1.username)
print(user_1.followers) # 0 default value
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

