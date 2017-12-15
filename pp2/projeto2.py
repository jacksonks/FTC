def ehNum(n):
    return (n != '*' and n != '+' and n != '-' and n != '/')

def op (pilha_op, pilha_num):
    a = pilha_op.pop()
    if(a == '*'):
        n1 = pilha_num.pop(-2)
        n2 = pilha_num.pop(-1)
        r = (n1)*(n2)
        pilha_num.append(r)
    elif(a == '/'):
        n1 = pilha_num.pop(-2)
        n2 = pilha_num.pop(-1)
        if(n2 != 0.00):
            r = (n1)/(n2)
            pilha_num.append(r)
    elif(a == '+'):
        n1 = pilha_num.pop(-2)
        n2 = pilha_num.pop(-1)
        r = (n1)+(n2)
        pilha_num.append(r)        
    elif(a == '-'):
        n1 = pilha_num.pop(-2)
        n2 = pilha_num.pop(-1)
        r = (n1)-(n2)
        pilha_num.append(r)
        
def pre(pilha_op,pilha_num,i):
    b = pilha_op[-1]
    if(b == '*' and (i == '+' or i =='-' or i =='*')):
        op(pilha_op,pilha_num)
    elif(b == '/' and (i == '+' or i =='-')):
        op(pilha_op,pilha_num)
    elif(b == '-' and (i == '+' or i =='-')):
        op(pilha_op,pilha_num)
            
def main(pilha_op,pilha_num):
    if(len(pilha_op) >= 1 or len(pilha_num) > 1):
        print("Error")
    elif(len(pilha_num) == 1 and len(pilha_op) == 0):
        print("%.2f" % pilha_num[0])
    else:
        print("Error")    

e = str(input())
e2 = []
pilha_num = []
pilha_op = []
aux = ""
for i in range(len(e)):
    if(e[i] != " "):
        if(ehNum(e[i])):
            aux= aux +e[i]
            if(i == len(e) -1):
                e2.append(aux)            
        else:
            if(len(aux)!= 0):
                e2.append(aux)
                aux=""
            e2.append(e[i])
    else:
        if(len(aux) != 0):
            e2.append(aux)
            aux=""
            
for i in e2:
    if(i != '*') and (i != '/') and (i != '+') and (i != '-'):
            pilha_num.append(float(i))
    else:
        if(len(pilha_num) >= 2 and len(pilha_op) >= 1):
            pre(pilha_op,pilha_num,i)
            while(pilha_op[-1:] == '/' or pilha_op[-1:] == '*'):
                if(i == '+' or i == '-'):
                    pre(pilha_op,pilha_num,i)
                else:
                    pilha_op.append(i)
            pilha_op.append(i)
        else:
            pilha_op.append(i)
            
while(len(pilha_num) != 1 and len(pilha_op) != 0):
    op(pilha_op,pilha_num)
main(pilha_op,pilha_num)