class Node:

    def __init__(self,data):       #class for node
        self.data=data
        self.next=None

class Linked:

    def __init__(self):
        self.head=None           #initialize head as none

    def beginning(self,data):        #insert at the beginning
        newNode=Node(data)           #create new node
        newNode.next=self.head       #next field will store the address of node which head was storing before insertion
        self.head=newNode            #head will store the address of new node
    def insert(self,prev,data):
        if prev is None:
            print("")
            return
        newNode=Node(data)          #create node
        newNode.next=prev.next         #address which previous node was storing is now stored by new node
        prev.next=newNode              #next field of previous node now stores the address of new node
    def end(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        temp=self.head
        while(temp.next):           #traverse the list till end
            temp=temp.next
        temp.next=newNode
    def search(self,key):
        temp=self.head
        while(temp):
            if temp.data==key:      #if key found return true
                return True
            temp=temp.next
        return False
    #bubble sort
    def sort(self):
        end=None
        while end!=self.head:
            p=self.head
            while p.next!= end:
                q=p.next
                if p.data>q.data:
                    p.data,q.data=q.data,p.data
                p=p.next
            end=p

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next


listt=Linked()
listt.beginning(50)
listt.end(30)
listt.beginning(20)
listt.insert(listt.head.next,8)
listt.beginning(90)
listt.sort()
if listt.search(40):
    print("Key Found")
else:
    print("Key Not found")

listt.print()
