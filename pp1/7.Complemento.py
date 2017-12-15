import re
entrada = str(input())
lista = []
lista = entrada.split(" ")

def complemento (g):
    if(re.match(r'(\A[R][$\b])', g)):
        if(re.match(r'([0-9]{1,}[\.][0-9]{2}$)', g)):
            return True
        else:
            return False
        
if((complemento(lista) == True)):
    print(True)
elif((complemento(lista) == False)):
    print(False)