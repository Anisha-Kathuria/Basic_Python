class Node:
    '''
    DESCRIPTION: To create an object of type node having 2 attributes data and next
    '''
    def __init__(self,value):
        '''
        OBJECTIVE: To initialize object of class node
        INPUT PARAMETERS:
                    self: Inbuilt parameter
                    value: To assign data attribute of node object
        '''
        self.data=value
        self.next=None

class LinkedList:
    '''
    DESCRIPTION: To create an object of type linkedlist with using multiple objects
                of class node
    '''
    def __init__(self):
        '''
        OBJECTIVE: To initialize object of class LinkedList
        INPUT PARAMETERS:
                    self: Inbuilt parameter
        '''
        self.head=None

    def insertnode(self,value):
        '''
        OBJECTIVE: To insert value at the start of linked list object
                    using new node
        INPUT PARAMETERS:
                    self: Inbuilt parameter
                    value: Value to be inserted
        '''
        if self.head==None:
            self.head=Node(value)
        else:
            n=Node(value)
            n.next=self.head
            self.head=n

    def __str__(self):
        '''
        OBJECTIVE: To print the linked list
        INPUT PARAMETERS:
                    self: Inbuilt parameter
        OUTPUT PARAMETER:
                    To print the elements of linked list
        '''
        strlist=''
        if self.head==None:
            return 'Empty List'
        current=self.head
        while current.next!=None:
            strlist+=str(current.data)+ "->"
            current=current.next
        strlist+=str(current.data)
        return strlist

    def deletenode(self,value):
        '''
        OBJECTIVE: To delete a node in linkedlist with a given value
        INPUT PARAMETERS:
                    self: Inbuilt parameter
                    value: Value of node to be deleted
        OUTPUT PARAMETER:
                    return list with deleted value if value not present None
        '''
                    
        if self.head.data == value:
            self.head = self.head.next
            return "Node with value " + str(value) + " is deleted from the Linked List"
        elif self.head.next == None :
            return "Node with value " + str(value) + " is not present in the Linked List"
            
            
        prevNode = self.head
        currNode = self.head.next

        
        while currNode != None and currNode.data != value :
            currNode = currNode.next
            prevNode = prevNode.next

        if currNode == None :
            return "Node with value " + str(value) + " is not present in the Linked List"
        else :
            prevNode.next = currNode.next
            return "Node with value " + str(value) + " is deleted from the Linked List"
  
