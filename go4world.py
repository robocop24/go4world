st = input()
experession=[]
for i in st:
    if i.isdigit():
        if experession[-1].isdigit():
            experession[-1]+=i
        else:
            experession.append(i)
    elif i == ' ':
        pass
    else:
        experession.append(i)
        
for i in range(len(experession)):
    if experession[i].isdigit():
        experession[i]=int(experession[i])
print(experession)


def solve(exp):
    while len(exp) != 1:
        if '/' in exp:
            op_index = exp.index('/')
            a = op_index-1
            b = op_index+1
            v = exp[a] / exp[b]
            exp= exp[:op_index]+exp[b+1:]
            #print(v)
            exp[a] = v
        elif '*' in exp:
            op_index = exp.index('*')
            a = op_index-1
            b = op_index+1
            v = exp[a] * exp[b]
            exp= exp[:op_index]+exp[b+1:]
            #print(v)
            exp[a] = v
        elif '+' in exp:
            op_index = exp.index('+')
            a = op_index-1
            b = op_index+1
            v = exp[a] + exp[b]
            exp= exp[:op_index]+exp[b+1:]
            #print(v)
            exp[a] = v
        elif '-' in exp:
            op_index = exp.index('-')
            a = op_index-1
            b = op_index+1
            v = exp[a] - exp[b]
            exp= exp[:op_index]+exp[b+1:]
            #print(v)
            exp[a] = v
        #print(exp)
    return exp[0]
        

def rec(stack,i):
    c = experession[i]
    print(stack)
    if c == ')':
        return solve(stack)
    elif c== '(':
        i+=1
        return rec([],i)
    else:
        stack.append(experession[i])
        i+=1
        return rec(stack,i)

stack = []

print(rec(stack,0))