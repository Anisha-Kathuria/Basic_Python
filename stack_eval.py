class stack:
    def __init__(self):
        self.stck=[]

    def push(self,ele):
        self.stck.append(ele)

    def isEmpty(self):
        return (len(self.stck)==0)

    def pop(self):
        if self.isEmpty():
           return True
        else:
           return self.stck.pop()

    def top(self):
        return self.stck[-1]
           
    def __str__(self):
        stackstr=''
        for i in range(len(self.stck)-1,-1,-1):
            stackstr+=str(self.stck[i])+'\n'
        return stackstr

def postfixeval(post):
    s=stack()
    for c in post:
        if c.isdigit()==True:
            s.push(c)
        else:
            op1=s.pop()
            op2=s.pop()
            res=eval(op2+c+op1)
            s.push(res)
    print(s.pop())

def inpo(exp):
    s=stack()
    pre={'+':1, '-':1, '*':2, '/':2, '^':3}
    result=''

    for c in exp:
        if c=='(':
            s.push(c)
        elif c==')':
            val=s.pop()
            while val!='(':
                result+=val
                val=s.pop()
        elif c.isdigit()==True:
            result+=c
        elif c in pre:
            if not(s.isEmpty()):
                top=s.top()
            while not(s.isEmpty()) and s.top!='(' and pre[s.top()]>=pre[c]:
                result+=top
                s.pop()
                if not(s.isEmpty()):
                    top=s.top()
            s.push(c)
    while not(s.isEmpty()):
        result+=s.pop()
    return result
