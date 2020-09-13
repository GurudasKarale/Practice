class Node:                    #node class
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:

    def __init__(self):
        self.head=None              #initialize head

    def beginning(self,data):            #method to insert at the beginnning of the list
        newNode=Node(data)               #create new Node
        newNode.next=self.head           #what node was storing is now stored at next field of newNode

        if self.head is not None:
            self.head.prev=newNode
        self.head=newNode                #head now stores the address of new node

    def insert(self,data,previous):      #method to insert after the node

        if previous is None:
            print("cannot be null")
            return

        newNode=Node(data)             # create new Node
        newNode.next=previous.next     #Address that previous node was storing is now stored at new node's next field
        previous.next=newNode          #previous node now stores the address of new node
        newNode.prev=previous          #new Node's previous field stores the address of previous node
        if newNode.next is not None:
            newNode.next.prev=newNode

    def end(self,data):                #method to  insert at the end of list
        newNode=Node(data)             #create new node
        newNode.next=None              #node which is added at the end points to the null
        if self.head  is None:
            newNode.prev=None
            self.head=newNode
            return
        temp=self.head
        while(temp.next):              #traverse the list
            temp=temp.next
        temp.next=newNode
        newNode.prev=temp              #previous field of new node will store the address of temp
        return

    def print(self,node):
        while(node):
            print(node.data),
            temp=node
            node=node.next

        while(temp):
            print(temp.data)
            temp=temp.prev
list=LinkedList()
list.beginning(3)
list.beginning(1)
list.end(5)
list.insert(4,list.head.next)
list.print(list.head)
