Product
#//////////////////////////////////////////////////////////
def AgregarCliente(NombreN):
    class Cliente:
        def __init__(A,Nombre,Productos,DineroGastado,Horario):
            A.Prod = Productos
            A.Dinero = DineroGastado
            A.Horario = Horario
            A.Nom = Nombre
    Nom = str(NombreN)
    NombreN = Cliente(Nom,{"Tomate":0,"Frijoles":0,"Yuca":0,"Papa":0,"Esfero":0},0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
    return NombreN
#/////////////////////////////////////////////////////////
#CP codigo producto
def AgregarProducto(NombreN,Marca,PrecioAdquirido,Cantidad):
    global NumProduc
    class Producto:
        def __init__(A,Nombre,CodigoProducto,Marca,Precio,PrecioAdquirido,Cantidad,Vendidos):
            A.Nom = Nombre
            A.Precio = Precio
            A.Cant = Cantidad
            A.Vendidos = Vendidos
            A.CP = CodigoProducto
            A.Marca = Marca
            A.PrecioA = PrecioAdquirido
    Nom = str(NombreN)
    CP = NumProduc + 1
    NumProduc = NumProduc + 1
    NombreN = Producto(Nom,CP,Marca,Precio,Cantidad,0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
    return NombreN
#/////////////////////////////////////////////////////////
def RemoverCliente(NombreN):
    global Empleados
    removeEmpleados(NombreN)
    NombreN = "vacio"
#////////////////////////////////////////////
def RemoverProducto(NombreN):
    global Productos
    removeProductos(NombreN)
    NombreN = "vacio"
#//////////////////////////////////////////////
def CalculaoraGanaciaDueñoTotal():
    for i in Productos:
        CajaTotal = (i.Precio * i.Vendidos) + CajaTotal
    print(CajaTotal)
    Leer = input()
#//////////////////////////////////////////////
def FuncionesExtra():
    global Productos
    MenuExtra = print('''------Funciones extra------
1: Agregar Empleado
2: Agregar Producto
3: Remover Empleado
4: Remover Producto
5: Calculadora ganacia del precio bruto''')
    if MenuExtra == "1":
        AgregarCliente(NombreN)
    elif MenuExtra == "2":
        NombreN = input("Ingrese Nombre del Producto")
        Precio = input("Ingrese el Precio del nuevo Producto")
        Cantidad = input("Ingrese la Cantidad inicial en Stock de este Producto")
        Marca = input("Ingrese la marca del producto")
        Productos = AgregarProducto(NombreN,Marca,Precio,Cantidad)
    elif MenuExtra == "3":
        NombreN = input("Ingrese el Cliente que desea borrar")
        RemoverCliente(NombreN)
    elif MenuExtra == "4":
        NombreN = input("Ingrese el Producto que desea borrar")
        RemoverProducto(NombreN)
    elif MenuExtra == "5":
        CalculaoraGanaciaDueñoTotal()
    else:
        #Volver()
        hola = 1