def incremento(n):
    l = list(str(n))          
    for el in range(1,len(l)):
	    if l[el] >= l[el-1]:
		    continue
	    else:
		    return False
    return True

def decremento(n):
    l = list(str(n))
    for el in range(1,len(l)):
	    if l[el] <= l[el-1]:
		    continue
	    else:
		    return False
    return True


def bouncy(n):
    if not decremento(n) and not incremento(n): 
	    return True
    else:
	    return False


num = 0 
no_num= 99 # los numeros bouncy son de 3 digitos hacia arriba
d=no_num / 100

cont=99

while float((num)/(no_num + num)) < d :
    cont += 1
    if bouncy(cont):
        num += 1
    else:
        no_num += 1

print(f"Este es el numero bouncy {cont} al {d* 100}% ", flush=True)

        
    

    
     


