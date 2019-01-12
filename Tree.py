class Node:
    '''
    DESCRIPTION: To create an object of type node having 3 attributes
    data, left and right
    '''
    def __init__(self,value):
        '''
        OBJECTIVE: To initialize object of class node
        INPUT PARAMETERS:
                    self: Inbuilt parameter
                    value: To assign data attribute of node object
        '''
        self.data=value
        self.left=None
        self.right=None

class Tree:
    '''
    DESCRIPTION: To create an object of type tree with using multiple objects
                of class node
    '''
    def __init__(self):
        '''
        OBJECTIVE: To initialize object of class Tree
        INPUT PARAMETERS:
                    self: Inbuilt parameter
        OUTPUT PARAMETERS:
                    None
        '''
        self.root=None
        
    def insertwrapper(self):
        '''
        OBJECTIVE: To initialize object of class Tree
        INPUT PARAMETERS:
                    self: Inbuilt parameter
        OUTPUT PARAMETERS:
                    return string of tree
        '''
        return self.traverse(self.root,"")
    
    def __str__(self):
        '''
        OBJECTIVE: To print the linked list
        INPUT PARAMETERS:
                    self: Inbuilt parameter
        OUTPUT PARAMETER:
                    To return the elements of linked list
        '''
        return self.insertwrapper()
        
    def insertnode(self, value):
        '''
        OBJECTIVE: To insert value in tree
        INPUT PARAMETERS:
                    self: Inbuilt parameter
                    value: Value to be inserted
        OUTPUT PARAMETERS:
                    None
        '''
        if self.root==None:
            self.root=Node(value)
        else:
            n=Node(value)
            current=self.root
            done=False
            while done==False:
                if current.data<n.data:
                    if current.right==None:
                        current.right=n
                        done=True
                    else:
                        current=current.right
                elif current.data>n.data:
                    if current.left==None:
                        current.left=n
                        done=True
                    else:
                        current=current.left
                else:
                    print(" Same value already present")
                    break
    
    def traverse(self,current=None,Tstring=""):
        '''
        OBJECTIVE: To traverse the tree
        INPUT PARAMETERS:
                    self: Inbuilt parameter
                    current: To keep track of root of current subtree to be traversed
                    Tstring: Tree string to be displayed
        OUTPUT PARAMETERS:
                    return Tstring
        '''
        #APPROACH: Recurrsive call to traverse: left subtree, root, right subtree

        if current.left!=None:
            Tstring = self.traverse(current.left,Tstring)
        Tstring+=" "+str(current.data)
        if current.right!=None:
            Tstring = self.traverse(current.right,Tstring)
        return Tstring

def main():
    '''
    OBJECTIVE : Menu based linkedlist program
    '''
    T=Tree()

    while True:
        print("\n\nTree Menu")
        print("1. Create Tree")
        print("2. Traverse and display")
        print("3. Exit")
        choice=int(input("\n\nEnter your choice "))
        if choice==1:
            L=eval(input("Enter list to be converted to string "))
            for i in L:
                T.insertnode(i)
        elif choice==2:
            print(T)
        elif choice==3:
            break
        else:
            print("Invalid Choice")
    
if __name__=="__main__":
    main()
               
                
                

