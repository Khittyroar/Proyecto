class Persona:
    def __init__(A,Nombre,DineroGastado,ConQueSuelePagar,Horario,Productos):
        A.Nom = Nombre
        A.Din = DineroGastado
        A.Pago = ConQueSuelePagar
        A.Hor = Horario
        A.Prod = Productos
class Producto:
    def __init__(A,Nombre,Precio,Cantidad):
        A.Nom = Nombre
        A.Precio = Precio
        A.Cant = Cantidad
Cliente1 = Persona("Sofia",0,0,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0])
Cliente2 = Persona("Maria",0,0,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0])
Cliente3 = Persona("Pablo",0,0,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0])
Cliente4 = "vacio"
Cliente5 = "vacio"
#**encontrar la manera de Nombrar una variable sin necesitar saber el nobmre
##contador clientes
Clientes = [Cliente1,Cliente2,Cliente3]

Produc1 = Producto("Arroz",5000.00,10)
Produc2 = Producto("Frij.",8000.00,10)
Produc3 = Producto("Yuca ",1000.00,10)
Produc4 = Producto("Papa ",500.000,10)
Produc5 = Producto("Agua ",10000.0,10)
Produc6 = "vacio"
Produc7 = "vacio"
Produc8 = "vacio"
Produc9 = "vacio"
Productos = [Produc1,Produc2,Produc3,Produc4,Produc5] 
##Contador Productos
ConProductos = 5
#/////////////////////////////////////////////////////////////
def Cl(A):
    #se puede aregar un modo de cliente que no sea nuevo y que le pueda personalizar cada dato
    Nombre = A
    NCliente = Persona(Nombre,0,0,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0])
    print(NCliente)
    return NCliente
#//////////////////////////////////////////////////////////////
def NuevoPd(A,B,C):
    Nombre = A
    Precio = B
    Cantidad = C
    NProducto = Producto(Nombre,Precio,Cantidad)
    print(NProducto)
    return NProducto
#///////////////////////////////////////////////////////////////
def AgregarCl():
    global Cliente1
    global Cliente2
    global Cliente3
    global Cliente4
    global Cliente5
    Nombre = input("Nombre de la persona")
    if not( Cliente1 == "vacio"):
        Cliente1 = Cl(Nombre)
    elif not(Cliente2 == "vacio"):
        Cliente2 = Cl(Nombre)
    elif not(Cliente3 == "vacio"):
        Cliente3 = Cl(Nombre)
    elif not(Cliente4 == "vacio"):
        Cliente4 = Cl(Nombre)
    elif not(Cliente5 == "vacio"):
        Cliente5 = Cl(Nombre)
    else:
        "Limite maximo de usuarios"
#/////////////////////////////////////////////////////////////////////
def AgregarProd():        
    global Produc1
    global Produc2
    global Produc3
    global Produc4
    global Produc5
    global Produc6
    global Produc7
    global Produc8
    global Produc9
    Nombre = input("Ingrese el Nombre del Producto ")
    Precio = input("Ingrese el Precio del Producto ")
    Cantidad = input("Ingrese el Cantidad del Producto ")
    if Produc1 == "vacio":
        Produc1 = Producto(Nombre,Precio,Cantidad)
    elif Produc2 == "vacio":
        Produc2 = Producto(Nombre,Precio,Cantidad)
    elif Produc3 == "vacio":
        Produc3 = Producto(Nombre,Precio,Cantidad)
    elif Produc4 == "vacio":
        Produc4 = Producto(Nombre,Precio,Cantidad)
    elif Produc5 == "vacio":
        Produc5 = Producto(Nombre,Precio,Cantidad)
    elif Produc6 == "vacio":
        Produc5 = Producto(Nombre,Precio,Cantidad)
    elif Produc6 == "vacio":
        Produc6 = Producto(Nombre,Precio,Cantidad)
    elif Produc7 == "vacio":
        Produc7 = Producto(Nombre,Precio,Cantidad)
    elif Produc8 == "vacio":
        Produc8 = Producto(Nombre,Precio,Cantidad)
    elif Produc9 == "vacio":
        Produc9 = Producto(Nombre,Precio,Cantidad)
#////////////////////////////////////////////////////////////////////////
def VerUsuarios():
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
#////////////////////////////////////////////////////////////////////////
def VerTiendita():
    for i in Productos:
            print(i.Nom,"|",i.Precio)
VerTiendita()

