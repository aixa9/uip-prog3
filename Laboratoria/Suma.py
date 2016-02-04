#suma del 10 al 5000

print("______________________________________________________________")
print("........PROGRAMA PARA REALIZAR SUMA DEL 10 AL 5000........")
print("______________________________________________________________")

n = 10
sum = 0
i = 0
while n <= 5000:
    if n % 2 == 0:
        if n != 100 or n != 1000:
             sum += n
    else : i += n
    n += 1



print ("RESULTADOS....")
print("\nTotal de pares : %i" %sum)
print("Total de  impares %i" %i)


