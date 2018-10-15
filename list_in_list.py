def insertlist2(a,val):
    if a==[]:
        a=[val]
        return a
    elif a[0]>=val:
        a[1:]=a
        a[0]=val
        return a
    else:
        a[1:]=insertlist2(a[1:],val)
        return a

def list2(s,u):
    if u==[]:
        return
    else:
        s=insertlist2(s,u[0])
        list2(s,u[1:])
        
