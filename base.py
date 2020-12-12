#//////////////////////////////////////////////////////////////////////////////////////
class Cliente:
        def __init__(A,Nombre,Productos,DineroGastado,Horario):
            A.Prod = Productos
            A.Dinero = DineroGastado
            A.Horario = Horario
            A.Nom = Nombre
Cl1 = Cliente("Eduardo Castellanos",{"Frij. ":0,"Arroz ":0,"Huevos": 0,"Leche":0},0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
Cl2 = Cliente("Maria Gonzales",{"Frij. ":0,"Arroz ":0,"Huevos": 0,"Leche":0},0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
Cl3 = Cliente("Omar Valderrama",{"Frij. ":0,"Arroz ":0,"Huevos": 0,"Leche":0},0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
Cl4 = Cliente("Francisco Mesa",{"Frij. ":0,"Arroz ":0,"Huevos": 0,"Leche":0},0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
Cl5 = Cliente("Juan Muelas",{"Frij. ":0,"Arroz ":0,"Huevos": 0,"Leche":0},0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
Clientes = [Cl1,Cl2,Cl3,Cl4,Cl5]
#//////////////////////////////////////////////////////////////////////////////////////////////
class Producto:
        def __init__(A,Nombre,CodigoProducto,Marca,Precio,Cantidad,Vendidos):
            A.Nom = Nombre
            A.Precio = Precio
            A.Cant = Cantidad
            A.Vendidos = Vendidos
            A.CP = CodigoProducto
            A.Marca = Marca
P1 = Producto("Frij. ",1,"LaAbuelita",3000,12,0)
P2 = Producto("Arroz ",2,"LaAbuelita",5000,6,0)
P3 = Producto("Huevos",3,"SantaMaria",4500,32,1)
P4 = Producto("Leche ",4,"SantaMaria",2000,10,14)
Productos = [P1,P2,P3,P4]
NumeroFacturas = 3
#/////////////////////////////////////////////////////////////////////////////////////////////////

#Dinero.Txt
P = open("DineroHoy.txt","w")
P.write("Dinero \n")
P.close()
#VendidoHoy.txt   ([Hora] :[Producto vendido] x [cantidad])
P = open("VendidoHoy.txt","w")
P.write("Productos vendidos \n")
P.close()
#Cambios Stock ([Hora] :[Producto Antiguo] -> [NuevoProducto])
P = open("CambiosStock.txt","w")
P.write("Cambios Stock \n")
P.close()
#Ganancias
P = open("Ganancias.txt","w")
P.write("Ganancias \n")
P.close()
#Ediciones Precios
P = open("EdicionesPrecios.txt","w")
P.write("Ediciones Precios \n")
P.close()

def MenuPrincipal():
    MenuP = input(''' -----La tiendita del viejo Jose-----
                 
1: Tiendita
2: Administrador
''')
    if MenuP == "1":
        Tiendita()
    elif MenuP == "2":
        Administrar()
    else:
         print('''
               Input invalido
 ''' )
         A = input()
         MenuPrincipal()
#/////////////////////////////////////////////
def Tiendita():
    Menu = input('''---Tiendita---
 1: stock
 2: Caja
 3: VolverAMenuPrincial''')
    if Menu == "1":
        StockHoy()    
    elif Menu =="2":
        Caja()  

    elif Menu =="4":
        SalirP()
    else:
        print('''
               Input invalido
 ''' )
        A = input()
        Tiendita()
#-------------------------------------------------------------------------




#/////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////
def Administrar():
    Menu = input('''---Administrar---
 1: Stock
 2: Precios
 3: Extra
 4: Retorno a MenuPrincial 
 -->''')
    if Menu == "1":
         Stock()
    elif Menu == "2":
         Precios()

    elif Menu == "3":
         FuncionesExtra()
    elif Menu == "4":
         SalirP()
    else:
         print('''
               Input invalido
 ''' )
         A = input()
         Administrar()
        
#???????????????????????????????????????????????????????????????????????
def Stock():
    
    Menu = input('''------Stock------
 1: Ver tienda
 2: Agregar Stock
 3: Retirar Stock
 4: Salir
 
 Ingrese el numero de su eleccion :  
-->''')
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
         SalirAdm()
         print('''
               Input invalido
 #''' )
    A = input()
    Menu = A
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def VerTienda():
    global Productos
    for i in Productos:
        print(i.Nom,"|",i.Precio)
    A = input('''
Regresando
''')
    Stock()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
#no se usa
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

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
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#????????????????????????????????????????????????????????????????????????????????????
#????????????????????????????????????????????????????????????????????????????????????
def Precios():
    Menu = input('''---Historial---
 1: Cambiar Precios
 2: Mostrar Precios
 3: Volver a Administraciones
 
 --> ''')
    if Menu == "1":
        Produc = input('''Inserte el producto al que le quiere cambiar el precio.
Recuerde Usar majusculas y en caso que su producto no tenga 6 caracteres agregar espacios
--> ''')
        NuevoPrecio = input("Inserte el Nuevo precio que le dara al producto")
        CambiarPrecios(Produc,NuevoPrecio)
    elif Menu == "2":
        MostrarPrecios()
    elif Menu == "3":
        SalirAdm()
    
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def CambiarPrecios(Produc,NuevoPrecio):
    import time
    global Productos
    for i in Productos:
        if Produc == i.Nom:        
            i.Precio = NuevoPrecio
            P = open("EdicionesPrecios.txt","a")
            Hora = time.strftime("%H:%M:%S")
            P.write(f"{Hora} :: {Produc} | {i.Precio}  --> {Produc} | {NuevoPrecio} \n ")
            P.close()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def MostrarPrecios():
    global Productos
    for i in Productos:
        print(f"{i.Nom} | {i.Precios}")
    Pausa = input("Regresando")
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''  
#??????????????????????????????????????????????????????????????????????????????????????????????????
#????????????????????????????????????????????????????????????????????????????????????????
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
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def FuncionesExtra():
    global Productos
    MenuExtra = print('''------Funciones extra------
1: Agregar Empleado
2: Agregar Producto
3: Remover Empleado
4: Remover Producto
5: Calculadora ganacia del precio bruto''')
    if MenuExtra == "1":
        NombreN = input("Inserte el Nuevo nombre")
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
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def AgregarProducto(NombreN,Marca,Precio,Cantidad):
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
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def RemoverCliente(NombreN):
    global Clientes
    Clientes.remove(NombreN)
    NombreN = "vacio"
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def RemoverProducto(NombreN):
    global Productos
    Productos.remove(NombreN)
    NombreN = "vacio"
#''''''''''''''''''''''''''''''''''''''''''''''''''''
#???????????????????????????????????????????????????????????????????????????????????????
def Caja():
    
    CodigoP,ListaCaja= ListaCompra()
    Cliente = input('''Ingrese el Numero del Cliente, en caso de ser un cliente no registrado introduzca "Cliente 0"
--> ''')
    CC = input('''Ingrese la Cedula del Cliente
--> ''')
    Existe = input(''' El Usuario es un "Jose Cliente"
--> ''')
    Hora,Fecha = PresentacionFactura(Cliente, CC,Existe)
    Pausa = input("")
    Total = SumaPrecios(CodigoP,ListaCaja)
    Paga = int(input('''Con cuanto paga:    '''))
    DetallesValores(Total,Paga)
    VendidoHoyTxt(ListaCaja ,Hora)
    DineroHoyTxt(Hora)
    CambiosStockTxt(Hora)
    global Stock
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def CambiosStockTxt(Hora):
    global Productos
    P = open("CambiosStock.txt","a")
    P.write(f"{Hora} :\n" )
    for i in Productos:
        P.write(f"{i.Nom} | {i.Cant} \n")
    P.close()
#::::::::::::::::::::::::::::::::::::::::::
def DineroHoyTxt(Hora,Total):
    P = open("VendidoHoy.txt","a")
    P.write(f"{Hora} : {Total}")
    P.close()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def VendidoHoyTxt(ListaCaja ,Hora):
    P = open("VendidoHoy.txt","a")
    P.write(Hora)
    P.write("\n")
    for i in ListaCaja:
        P.write(f"{i} x {ListaCaja[i]}")
    P.write("\n")
    P.close()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#/////////////////////////////////////////////
def PresentacionFactura(Cliente,CC,Existe):
    import time
    global Clientes
    Comprobacion = 0
    if Existe == "Si":
        for i in Clientes:
            if Cliente == i.Nom and CC == i.CC:
                Temp = i
                break
            else:
                while Comprobacion == 0:
                    print('''La informacion suministrada es invalida.Intente de nuevo''')
                    Cliente = input('''Ingrese el Numero del Cliente, en caso de ser un cliente no registrado introduzca "Cliente 0"
--> ''')
                    CC = input('''Ingrese la Cedula del Cliente
--> ''')
                    Existe = input('''El Usuario que usted pretende ingresar ya esta registado en la base de datos
1: Si
2: No
--> ''')                    
                    if Existe =="si":
                        for i in Clientes:
                            if Cliente == i.Nom and CC == i.CC:
                                Temp = i
                                break
                    elif Existe == "No":
                        Comprobacion = 1    
    Hora = time.strftime("%H:%M:%S")
    Fecha = time.strftime("%d/%m/%Y")
    global NumeroFacturas
    print(f'''--------------------------------
 -[La tiendita del viejo Jose]- 
--------------------------------

Fecha:             {Fecha}
Hora:              {Hora}
Numero de factura: {NumeroFacturas}
Nombre:            {Cliente}
C.C :              {CC}
Registrado:        {Existe}
''')   
    NumeroFacturas += 1
    return Hora,Fecha
#///////////////////////////////////////////////////////
def SumaPrecios(CodigoP,ListaCaja):
    global Productos
    print("--------------------------------")
    SubTotal = 0
    for i in Productos:
        #print(C)
        for j in CodigoP:
            #print(i.CP,j)
            if i.CP == j:
                Suma = i.Precio * ListaCaja[i.Nom]
                i.Cant = i.Cant - ListaCaja[i.Nom]
                SubTotal += Suma
                print(
f'''------------ {i.Nom} ------------       
 C.P. : {i.CP} | Marca: "{i.Marca}"             
 Precio |  Cantidad  | Total                        
 {i.Precio}   ||    {ListaCaja[i.Nom]}     || {Suma}
         
           SubTotal  = {SubTotal}
           
           ''')
    print("--------------------------------")
    return SubTotal
#///////////////////////////////////////////////////////
def DetallesValores(Total,Paga):
    Total2 = float(Total) * 0.81
    Vueltas = Paga - Total
    print(f'''--------------------------------
Total sin Iva........... {Total2}
Iva..................... 19%
Descuento Cliente....... No
Total................... {Total}

Paga.................... {Paga}
Vueltas................. {Vueltas}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
#///////////////////////////////////////////////////////
def MenuCaja():
      Menu = input('''---Stock---
 1: Caja
 2: Volver a tienda
 
 --> ''')
      if Menu == "1":
          Caja()
      elif  Menu == "2":
          SalirT()
#/////////////////////////////////////////////////////////
def ListaCompra():
    global Productos
    CodigoP = []
    ListaCaja = {}
    Lista2 = []
    Lista1 = input('''Introduzca la lista de compra en este espacio.
Porfavor Introduzcalo de la forma [Producto1]-[Cantidad1],[Producto2]-[Cantidad2],[Producto n]-[Cantidad n]

Notas:
    1- Usted no debe poner los [] solo introduzca el producto y en el espacio de cantidad un numero
    2- Asegurece de escribir bien los productos:
        2.1- Todos los productos deben tener 6 caracteres en caso de no tenerlos llenelos con espacios en la parte final de este
        2.2- Todos los productos comienzan por mayuscula
        
--> ''')
    Lista2 = Lista1.split(",")
    for i in Lista2:
        Parte = i.split("-")
        Parte[1] = int(Parte[1])
        ListaCaja[Parte[0]] = Parte[1]
        
    for i in ListaCaja:
        for j in Productos:
            print(i,j.Nom)
            if i == j.Nom:
                CodigoP.append(j.CP)
    print(CodigoP,ListaCaja)
    return CodigoP,ListaCaja
#????????????????????????????????????????????????????????????????????????????????????????????????
def StockHoy():
    
    Menu = print('''---Stock---
 1: Vendido hoy
 2: Inventario de tienda
 3: Productos en estanteria
 4: Rellenar Inventario en estanteria
 5: Volver a tienda
 
 --> ''')
    if Menu == "1":
        VendidoHoy()
    elif  Menu == "2":
        InventarioTienda()  
    elif  Menu == "3":
        InventarioTienda()
    elif  Menu == "4":
        ProductosEstanteria()
    elif  Menu == "5":
        Product = input('''Introduzca el producto
(recuerde que los productos tienen 5 Caracteres por lo que si su 
 producto tiene menso de 5 caracteres rellene el espacio restante 
 con espacios " " hasta tener 5)
--> ''')
        Agregar = int(input('''Cuanto desea agregar
--> '''))
        RellenarProductoEstanteria(Product,Agregar)
    else:
     Menu = Menu    
        
#///////////////////////////////////////////////////////////////////////////// 
def VendidoHoy():
    P = open("VendidoHoy","r")
    Ver = P.read()
    print(Ver)
    P.close()
#/////////////////////////////////////////////////////////////////////////////////
def InventarioTienda():
    global Productos
    for i in Productos:
        print(f"{i.Nom} | {i.Cant}")
#///////////////////////////////////////////////////////////////////////////////    
def ProductosEstanteria():
   global Productos
   for i in Productos:
       print(f"{i.Nom} | {i.CantEstanteria}")
#///////////////////////////////////////////////////////////////////////////////
def RellenarProductoEstanteria(Product,Agregar):
    global Productos
    Verificacion = "2"
    Contador = 0
    Fallos = 0
    while  Verificacion == "2":
        if Contador == 0:
            for i in Productos:
        #print(i.Nom,Product)
                if i.Nom == Product:
                    Antiguo = i.CantEsta
                    i.CantEsta = i.CantEsta + Agregar
                    #
                    print(f'''
                          
----Cambio realizado----
{i.Nom}|{Antiguo} --> {i.Nom}|{i.CantEsta}''')
                    Verificacion = input('''Continuar con los cambios
1: si
2: No
                
--> ''')
                    Fallos += 1
                    if Verificacion == "1":
                        #print("logro")
                        break
                    elif Verificacion == "2":
                        i.CantEsta = i.CantEsta - Agregar
                        
                elif Fallos == len(Productos):
                    print("Producto invalido. Porfavor ingreselos de nuevo")
                    i.CantEsta = i.CantEsta - Agregar
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
                    Antiguo = i.CantEsta
                    i.CantEsta = i.CantEsta + Agregar
                    print(f'''----Cambio realizado----
{i.Nom}|{Antiguo} --> {i.Nom}|{i.CantEsta}''')
                    Verificacion = input('''Continuar con los cambios
1: si
2: No
                
--> ''')       
                Fallos += 1
                if Verificacion == "1":
                    #print("logro")
                    break
                elif Verificacion == "2":
                    i.CantEsta = i.CantEsta - Agregar
                        
                elif Fallos == len(Productos):
                    print("Producto invalido. Porfavor ingreselos de nuevo")
                    i.CantEsta = i.CantEsta - Agregar
        if Verificacion == "2":
            i.CantEsta = i.CantEsta - Agregar
    #
    Pausa = input("Regresando")
#////////////////////////////////////


def SalirP():
    Pausa = input('''Regresando''')
    MenuPrincipal()
def SalirT():
    Pausa = input('''Regresando''')
    Tiendita()
def SalirAdm():
    Pausa = input('''Regresando''')
    Administrar()
#______________________________________________________________________________

MenuPrincipal()

