f = open('StockTienda.txt','w')
class Producto:
        def __init__(A,Nombre,CodigoProducto,Marca,Precio,Cantidad,Vendidos):
            A.Nom = Nombre
            A.Precio = Precio
            A.Cant = Cantidad
            A.Vendidos = Vendidos
            A.CP = CodigoProducto
            A.Marca = Marca
Cl1 = Producto("Frijol",1,"LaAbuelita",3000,12,0)
Cl2 = Producto("Arroz ",2,"LaAbuelita",5000,6,0)
Cl3 = Producto("Huevos",3,"SantaMaria",4500,32,1)
Cl4 = Producto("Leche ",4,"SantaMaria",2000,10,14)
Productos = (Cl1,Cl2,Cl3,Cl4)
def Stock():
    
    Menu = input('''------Stock------
 1: Ver tienda
 2: Agregar Stock
 3: Retirar Stock
 4: Salir
 
 Ingrese el numero de su eleccion :  ''')
    if Menu == "1":
         VerTienda()
         #parcialmente hecha
    elif Menu =="2":
        Product = input('''Introduzca el producto
(recuerde que los productos tienen 5 Caracteres por lo que si su 
 producto tiene menso de 5 caracteres rellene el espacio restante 
 con espacios " " hasta tener 5)
--> ''')
        Agregar = int(input('''Cuanto desea agregar
--> '''))
        AgregarStock(Product,Agregar)
    elif Menu =="3":
        Product = input('''Introduzca el producto
(recuerde que los productos tienen 5 Caracteres por lo que si su 
 producto tiene menso de 5 caracteres rellene el espacio restante 
 con espacios " " hasta tener 5)
--> ''')
        Restar = int(input('''Cuanto desea Restar
--> '''))
        RetirarStock(Product,Restar) 
        #HistorialDelDia
        #hacer historial
    elif Menu =="4":
         Salir()
         print('''
               Input invalido
 #''' )
    A = input()
    Menu = A
#///////////////////////////////////////////////////////////////
def VerTienda():
    global Productos
    for i in Productos:
        print(i.Nom,"|",i.Cant)
    A = input('''
Regresando
''')
    Stock()
#///////////////////////////////////////////////////////////////
def VerUsuarios():
    global Productos
    global Clientes
    for i in Productos:
        if i == Productos[0]:
            print("     ",i.Nom,end="|")
        elif i == Productos[-1]:
            print(i.Nom)
        else:
            print(i.Nom,end= "|")
    for i in Clientes:
        Contador = 1
        if not(i == "vacio"):
            print(i.Nom,end = "   ")
        for j in i.Prod:
            ##print(Contador,len(i.Prod))
            if Contador == len(i.Prod):
                    print(i.Prod[j])
            else:
                print(j,end="  |  ")
            Contador += 1
#///////////////////////////////////////////////////////////////
def VerTiendita():
    global Productos
   
#///////////////////////////////////
def AgregarStock(Product,Agregar):
    global Productos
    Verificacion = "2"
    Contador = 0
    Fallos = 0
    while  Verificacion == "2":
        if Contador == 0:
            for i in Productos:
        #print(i.Nom,Product)
                if i.Nom == Product:
                    Antiguo = i.Cant
                    i.Cant = i.Cant + Agregar
                    print(f'''
                          
----Cambio realizado----
{i.Nom}|{Antiguo} --> {i.Nom}|{i.Cant}''')
                    Verificacion = input('''Continuar con los cambios
1: si
2: No
                
--> ''')
                    Fallos += 1
                    if Verificacion == "1":
                        #print("logro")
                        break
                    elif Verificacion == "2":
                        i.Cant = i.Cant - Agregar
                        
                elif Fallos == len(Productos):
                    print("Producto invalido. Porfavor ingreselos de nuevo")
                    i.Cant = i.Cant - Agregar
                    Fallos = 0
        if Verificacion == "1":
             break 
        Product = input('''Introduzca producto
(recuerde que los productos tienen 5 Caracteres por lo que si su 
 producto tiene menso de 5 caracteres rellene el espacio restante 
 con espacios " " hasta tener 5)
--> ''')
                           
        Agregar = int(input('''Cuanto desea agregar
--> '''))
        Contador =+ 1  
        for i in Productos:
        #print(i.Nom,Product)
                if i.Nom == Product:
                    Antiguo = i.Cant
                    i.Cant = i.Cant + Agregar
                    print(f'''----Cambio realizado----
{i.Nom}|{Antiguo} --> {i.Nom}|{i.Cant}''')
                    Verificacion = input('''Continuar con los cambios
1: si
2: No
                
--> ''')       
                Fallos += 1
                if Verificacion == "1":
                    #print("logro")
                    break
                elif Verificacion == "2":
                    i.Cant = i.Cant - Agregar
                        
                elif Fallos == len(Productos):
                    print("Producto invalido. Porfavor ingreselos de nuevo")
                    i.Cant = i.Cant - Agregar
        if Verificacion == "2":
            i.Cant = i.Cant - Agregar
    #
    CambiosStockTxt()
    Pausa = input("Regresando")
    Stock()        
                  
            #poner una resta al dinero total
#::::::::::::::::::::::::::::::::::::
def CambiosStockTxt():
    global Productos
    import time
    Hora = time.strftime("%H:%M:%S")
    P = open("CambiosStock.txt","a")
    P.write(f"{Hora} :\n" )
    for i in Productos:
        P.write(f"{i.Nom} | {i.Cant} \n")
    P.close()
#::::::::::::::::::::::::::::::::::::::::::::
#///////////////////////////////////
def RetirarStock(Product,Restar):
    global Productos
    Verificacion = "2"
    Contador = 0
    Fallos = 0
    while  Verificacion == "2":
        if Contador == 0:
            for i in Productos:
        #print(i.Nom,Product)
                if i.Nom == Product:
                    Antiguo = i.Cant
                    i.Cant = i.Cant - Restar
                    print(f'''
                          
----Cambio realizado----
{i.Nom}|{Antiguo} --> {i.Nom}|{i.Cant}''')
                    Verificacion = input('''Continuar con los cambios
1: si
2: No
                
--> ''')
                    Fallos += 1
                    if Verificacion == "1":
                        #print("logro")
                        break
                    elif Verificacion == "2":
                        i.Cant = i.Cant + Restar
                        
                elif Fallos == len(Productos):
                    print("Producto invalido. Porfavor ingreselos de nuevo")
                    i.Cant = i.Cant + Restar
                    Fallos = 0
        if Verificacion == "1":
             break 
        Product = input('''Introduzca producto
(recuerde que los productos tienen 5 Caracteres por lo que si su 
 producto tiene menso de 5 caracteres rellene el espacio restante 
 con espacios " " hasta tener 5)
--> ''')
                           
        Agregar = int(input('''Cuanto desea agregar
--> '''))
        Contador =+ 1  
        for i in Productos:
        #print(i.Nom,Product)
                if i.Nom == Product:
                    Antiguo = i.Cant
                    i.Cant = i.Cant - Restar
                    print(f'''----Cambio realizado----
{i.Nom}|{Antiguo} --> {i.Nom}|{i.Cant}''')
                    Verificacion = input('''Continuar con los cambios
1: si
2: No
                
--> ''')       
                Fallos += 1
                if Verificacion == "1":
                    #print("logro")
                    break
                elif Verificacion == "2":
                    i.Cant = i.Cant - Agregar
                        
                elif Fallos == len(Productos):
                    print("Producto invalido. Porfavor ingreselos de nuevo")
                    i.Cant = i.Cant - Agregar
        if Verificacion == "2":
            i.Cant = i.Cant - Agregar
    #
    Pausa = input("Regresando")
    Stock()   
#//////////////////////////////////////
def Salir():
    print("hola")
    #Administrar()

#--------------------------------------------------------------------------


Stock()