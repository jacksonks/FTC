import re
entrada = str(input())
lista = []
lista.append(entrada)

print(lista)
print(len(lista))
print(len(entrada))
print(lista[0])

def banco (d):
    if(re.match(r'^(bradesco|caixa|brasil|safra|itau|outro)$', d)):
        return True
    else:
        return False
    
if((banco(lista[0]) == True)):
    print(True)
elif((banco(lista[0]) == False)):
    print(False)