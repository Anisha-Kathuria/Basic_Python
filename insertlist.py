def insertlist(a,val,index=0):
    '''
    OBJECTIVE: To insert an element in the sorted list.
    INPUT    :
            a: Sorted list of numbers.
          val: Value to be inserted.
        index: Default parameter to check poisition where element is to
               be inserted
    OUTPUT   : Return sorted list of numbers with the element inserted.
    '''
    #Approach: 



    if len(a)<=index:
        a.append(val)
        return a
    elif a[index]<val:
        return insertlist(a,val,index+1)
    elif a[index]>=val:
        a[index+1:]=a[index:]
        a[index]=val
        return a
