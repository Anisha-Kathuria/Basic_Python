class heap:
    '''
    Description: Class to implement queue
    '''
    def __init__(self):
        '''
        OBJECTIVE: To initialize elements of class
        INPUT PARAMETERS:
                        self: inbuilt parameter
        '''
        self.q=[]
    
    def qInsert(self,ele):
        '''
        OBJECTIVE: To insert element in the priority queue
        INPUT PARAMETERS:
                        self: inbuilt parameter
                        ele: element to be inserted
        OUTPUT PARAMETERS:
                        Return queue with inserted element
        '''
        if len(self.q)==0:
            self.q=[ele]
            return self.q
        else:
            self.q.append(ele)
            pos=len(self.q)-1
            while pos!=0:
                par=(pos-1)//2
                if self.q[par]<ele:
                    self.q[par],self.q[pos]=self.q[pos],self.q[par]
                    pos=par
                else:
                    break
            return self.q

    def qDelete(self):
        '''
        '''
        self.q[0]=self.q[-1]
        del self.q[-1]
        heapsort(self.q)
        return self.q
        
        
    def __str__(self):
        '''
        OBJECTIVE: To print elements of class-queue
        INPUT PARAMETERS:
                        self: inbuilt parameter
        '''
        return str(self.q)

def heapsort(h):
    '''
        OBJECTIVE: To apply heapsort on entered heap
        INPUT PARAMETERS:
                        heap: list on which heapsort is to be applied
    '''
    q=heap()
    for i in range(0,len(h)):
        h[:i+1]=q.qInsert(h[i])     
        
def main():
    '''
    q=heap()
    q.qInsert(2)
    q.qInsert(3)
    q.qInsert(1)
    q.qInsert(4)
    q.qDelete()

    l=[2,3,1,4]
    heapsort(l)
    l
    '''
    
if __name__=='__main__':
    main()
