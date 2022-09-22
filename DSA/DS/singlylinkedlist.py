# create nodes
# create LL all insertion methods
# Add nodes
# Print LL


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def lenlist(self):
        cur=self.head
        count=0
        while True:
            if cur is not None:
                count+=1
                cur=cur.next
            return count
    
    def insertend(self,newNode):
        if(self.head is None):
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode=lastNode.next 
            lastNode.next=newNode
    def insertbeg(self,newNode):
        if(self.head is None):
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    # def insertpos(self,newNode,pos):
    #     if pos==0:
    #         self.insertbeg(newNode)
    #     elif pos<0 or pos>self.lenlist():
    #         print("Invalid pos")
    #         return
    #     else:
    #         curnode=self.head
    #         curpos=0
    #         while(True):
    #             if(curpos==pos):
    #                 prevnode.next=newNode
    #                 newNode.next=curnode
    #                 break
    #             prevnode=curnode
    #             curnode=curnode.next
    #             curpos+=1
        
    def printList(self):
        header=self.head
        if header is None:
            print("List empty")
            return
        while header is not None:
            if header is None:
                break
            print(header.data)
            header=header.next


#Node=> data,next
firstNode=Node(10)
sll=LinkedList()
sll.insertend(firstNode)
secondNode=Node(20)
sll.insertend(secondNode)
fifth=Node(15)
# sll.insertpos(fifth,-1)
# sll.printList()
