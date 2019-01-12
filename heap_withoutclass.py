def create(q):
    '''
        OBJECTIVE: To create heap of given priority queue
        INPUT PARAMETERS:
                        self: inbuilt parameter
                        q:queue to be converted to heap
        OUTPUT PARAMETERS:
                        Return heap
    '''
    h=[]
    for i in range(0,len(q)):
        h[:i+1]=insertheap(h[:i],q[i])
    return h

def qInsert(q,ele):
    '''
    OBJECTIVE: To insert element in the priority queue
    INPUT PARAMETERS:
                        self: inbuilt parameter
                        ele: element to be inserted
    OUTPUT PARAMETERS:
                        Return queue with inserted element
    '''
    q=create(q)
    q=insertheap(q,ele)
    return q
        
    
def insertheap(q,ele):
    '''
        OBJECTIVE: To insert element in heap
        INPUT PARAMETERS:
                        self: inbuilt parameter
                        q:heap
        OUTPUT PARAMETERS:
                        Return heap
    '''
    if len(q)==0:
        q=[ele]
        return q
    else:
        q.append(ele)
        pos=len(q)-1
        while True:
            par=(pos-1)//2
            if q[par]<ele and par>=0:
                q[par],q[pos]=q[pos],q[par]
                pos=par
            else:
                break
        return q
