def insertlist(a,val):
    '''
    OBJECTIVE: To insert an element in the sorted list.
    INPUT    :
            a: Sorted list of numbers.
          val: Value to be inserted.
    OUTPUT   : Return sorted list of numbers with the element inserted.
    '''
    #Approach: 

    if a==[]:
        a=[val]
        return a
    elif a[0]>=val:
        a[1:]=a
        a[0]=val
        return a
    elif a[0]<val:
        a[1:]=insertlist(a[1:],val)
        return a

