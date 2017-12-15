import re
entrada = str(input())
lista = []
lista.append(entrada)

def calculocpf(l):

    formatado = ""
    final = l[12:14]    
    container = []

    for i in range (0,11):
        if(l[i] != '.'):
            container.append(int(l[i]))
    
    numero1 = 10
    soma1 = 0

    for i in range (0,9):
        aux1 = container[i]*numero1
        soma1 = soma1 + aux1
        numero1 = numero1 - 1
    
    div1 = (soma1 % 11)

    if(div1 < 2):
        digito1 = 0
    else:
        digito1 = (11-div1)    
     
    numero2 = 11
    soma2 = 0

    for i in range (0,9):
        aux2 = container[i]*numero2
        soma2 = soma2 + aux2
        numero2 = numero2 - 1
    soma2 = soma2 + (digito1*2)    
    
    div2 = (soma2%11)

    if(div2 < 2):
        digito2 = 0
    else:
        digito2 = (11-div2)
    
    formatado = formatado + str(digito1) + str(digito2)
    
    if(formatado == final):
        return True
    else:
        return False

def formatocpf (k):
    if(re.match(r'([0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2}$)', k)):
        if(calculocpf(k)):
            return True
        else:
            return False
    else:
        return False

if((formatocpf(lista[0]) == True)):
    print(True)
elif((formatocpf(lista[0]) == False)):
    print(False)