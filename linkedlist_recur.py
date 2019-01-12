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
            return "empty list"
        current=self.head
        while current.next!=None:
            strlist+=str(current.data)+ "->"
            current=current.next
        strlist+=str(current.data)
        return strlist

    def deletenode(self,value,prev=None):
        '''
        OBJECTIVE: To delete a node in linkedlist with a given value recurrsively
        INPUT PARAMETERS:
                    self: Inbuilt parameter
                    value: Value of node to be deleted
                    prev: To keeep count of prev node of current node to be checked
        OUTPUT PARAMETER:
                    return list with deleted value if value not present None
        '''
        if prev==None:
            if self.head==None:
                print("Empty List no value")
                return
            elif self.head.data==value:
                if self.head.next==None:
                    self.head=None
                    print("Deleted value "+ str(value)+"\n")
                    return
                elif self.head.next!=None:
                    self.head=self.head.next
                    print("Deleted value "+ str(value)+"\n")
                    return
            else:
                prev=self.head
                self.deletenode(value,prev)
        else:
            current=prev.next
            if current!=None and current.data==value:
                prev.next=current.next
                print("Deleted value "+ str(value))
                return
            elif current==None:
                print("Not Found value " + str(value)+ " in list\n")
                return
            else:
                prev=prev.next
                self.deletenode(value,prev)

                
    def insertsort(self,value,prev=None):
        '''
        OBJECTIVE: To insert values in list in sorted manner
        INPUT PARAMETERS:
                    self: Inbuilt parameter
                    value: To be inserted
        OUTPUT PARAMETERS:
                    None
        '''
        if self.head==None:
            self.head=Node(value)
            return
        else:
            if prev==None:
                prev=self.head
            n=Node(value)
            if prev.data>=value:
                n.next=prev
                if prev==self.head:
                    self.head=n
                    return
            elif prev.next!=None and prev.data<value:
                prev=prev.next
                self.insertsort(value,prev)
                return
            elif prev.next==None:
                prev.next=n
                return  
def main():
    '''
    OBJECTIVE : Menu based linkedlist program
    '''
    L=LinkedList()
    while True:
        print("\n\nLinked List Menu")
        print("1. Insert at beginning")
        print("2. Delete a node with specific value")
        print("3. Display the list")
        print("4. Exit")
        choice=int(input("\n\nEnter your choice "))
        if choice==1:
            val=int(input("Enter the value to be inserted "))
            L.insertnode(val)
        elif choice==2:
            val=int(input("Enter the value to be deleted "))
            L.deletenode(val)
        elif choice==3:
            print(L)
        elif choice==4:
            break
        else:
            print("Invalid Choice")
    
if __name__=="__main__":
    main()

