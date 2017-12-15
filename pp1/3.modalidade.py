import re
entrada = str(input())
lista = []
lista = entrada.split(" ")

def login(a):
    if(re.match(r'^[a-z]*[a-zA-Z]*$', a)):
        return True
    else:
        return False
    
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

def formatocnpj (c):
    if(re.match(r'([0-9]{2}[\.][0-9]{3}[\.][0-9]{3}[/][0-9]{4}[-][0-9]{2}$)', lista[4])):
        return True
    else:
        return False

def banco (d):
    if(re.match(r'^(bradesco|caixa|brasil|safra|itau|outro)$', lista[3])):
        return True
    else:
        return False

def modalidade (e):
    if(re.match(r'^(user)$', lista[2])):
        if(login(lista[3]) and formatocpf(lista[4]) == True):
            return True
    elif(re.match(r'^(bank)$', lista[2])):
        if(banco(lista[3]) and formatocnpj(lista[4]) == True):
            return True
        else:
            return False
    else:
        return False
    
def v1(lista):
    if( login(lista[0]) and formatocpf(lista[1]) and modalidade(lista) and login(lista[3]) and formatocpf(lista[4]) == True):
        print(True)
    else:
        print(False)

def v2(lista):
    if( login(lista[0]) and formatocpf(lista[1]) and modalidade(lista) and banco(lista) and formatocnpj(lista) == True):
        print(True)
    else:
        print(False)
        
l = lista[2]
if(l == 'user'):
    v1(lista)
elif(l == 'bank'):
    v2(lista)