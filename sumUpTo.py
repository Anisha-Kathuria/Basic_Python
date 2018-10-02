def sumUpTo(n):
    '''
    Objective: Find out the sum of numbers from 0 to n.
    Input    : Limit n upto which sum is to be calculated.
    n        : Limit/Last mumber
    Output   : Sum of 1 to n.
    '''

    #Approach: sumUpTo(n)= n + sumUpTo(n-1)

    if n==0:
        return 0
    else:
        return n + sumUpTo(n-1)
    
