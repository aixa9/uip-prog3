#programa que maneja una lista de supermescado


tp= ("arroz","tuna","jugo","cereal","leche")
lt = [[tp],"mango","cereza"]
l2=lt[0]

print(" \t LISTA DE SUPERMERCADO ")
print("MENU: ")
print("1.ver articulos\n","2.agregar articulo \n","3.eliminar articulo \n","4.salir del menu")
op=input("Indique la opcion que desee realizar\n")

while op != '4':

    if op == '1':
     print("Artiulos en listas:")
     print(lt)
     break
    elif op =='2':
        print("agregar articulos: ")
        st=input ("articulo :")
        lt.append(st)    #agrega un articulo a la lista
        print (lt)
        break
    elif op =='3':
        print ("Eliminar articulo: ")
        st=input ("articulo:")          #borrar elemento
        lt.remove(st)
        print (lt)
        break
    else:
        print ("obcion incorrecta")
