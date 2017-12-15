import re
entrada = str(input())
lista = []
lista.append(entrada)

def md5 (h):
    if((len(lista) == 10)):
        k = lista [9]
        if(re.match(r'([0-9*a-f]{32}$)', k)):
            return True
        else:
            return False
    elif((len(lista) == 8)):
        k = lista [7]
        if(re.match(r'([0-9*a-f]{32}$)', k)):
            return True
        else:
            return False
    else:
        return False
    
if((md5(lista[0]) == True)):
    print(True)
elif((md5(lista[0]) == False)):
    print(False)