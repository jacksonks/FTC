import re
entrada = str(input())
lista = []
lista.append(entrada)

def calculocnpj(v):
    formatado = ""
    final = v[16:18]
    container = []
    container2 = []
    print(final)
    for i in range (0,16):
        if(v[i] != '.' and v[i] != '/' and v[i] != '-'):
            container.append(int(v[i]))    
    
    for i in range (0,17):
        if(v[i] != '.' and v[i] != '/' and v[i] != '-'):
            container2.append(int(v[i]))    

            
    numero1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = 0

    for i in range (0,12):
        aux1 = container[i]*numero1[i]
        soma1 = soma1 + aux1
    
    div1 = (soma1 % 11)
    
    if(div1 < 2):
        digito1 = 0
    else:
        digito1 = (11-div1)    
     
    numero2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = 0
    
    for i in range (0,13):
        aux2 = container2[i]*numero2[i]
        soma2 = soma2 + aux2
        
    div2 = (soma2 % 11)
    
    if(div2 < 2):
        digito2 = 0
    else:
        digito2 = (11-div2)
    
    formatado = str(digito1) + str(digito2)
    print(formatado)
    if(formatado == final):
        return True
    else:
        return False

def formatocnpj (e):
    if(re.match(r'([0-9]{2}[\.][0-9]{3}[\.][0-9]{3}[/][0-9]{4}[-][0-9]{2}$)', e)):
        if(calculocnpj(e)):
            return True
        else:
            return False
    else:
        return False
    
if((formatocnpj(lista[0]) == True)):
    print(True)
elif((formatocnpj(lista[0]) == False)):
    print(False)