def sumList(n):
    '''
    Objective: Find out the sum of list.
    Input    : List n.
    n        : List
    Output   : Sum of list.
    '''

    #Approach: sumList(n)= n[0] + sumList(n[1:])

    if n==[]:
        return 0
    else:
        return n[0] + sumList(n[1:])
