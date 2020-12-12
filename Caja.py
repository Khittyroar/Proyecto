# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:24:05 2020

@author: fhwx
"""
class Cliente:
        def __init__(A,Nombre,Productos,DineroGastado,Horario):
            A.Prod = Productos
            A.Dinero = DineroGastado
            A.Horario = Horario
            A.Nom = Nombre
Cl1 = Cliente("Eduardo Castellanos",{"Tomate":0,"Frijol":0,"Yuca  ":0,"Papa  ":0,"Huevos":0,"Leche ":0,"Maiz  ":0,"Gallet":0,"Yogurt":0,"Quesos":0,"Gomitas":0,"Mentas":0,"Chile ":0,"Deterg":0,"LimpVi":0,"Paleta":0,"Helado":0,"Cervez":0,"Desodor":0,"Escoba":0},0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
Cl2 = Cliente("Maria Gonzales",{"Tomate":0,"Frijol":0,"Yuca  ":0,"Papa  ":0,"Huevos":0,"Leche ":0,"Maiz  ":0,"Gallet":0,"Yogurt":0,"Quesos":0,"Gomitas":0,"Mentas":0,"Chile ":0,"Deterg":0,"LimpVi":0,"Paleta":0,"Helado":0,"Cervez":0,"Desodor":0,"Escoba":0},0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
Cl3 = Cliente("Omar Valderrama",{"Tomate":0,"Frijol":0,"Yuca  ":0,"Papa  ":0,"Huevos":0,"Leche ":0,"Maiz  ":0,"Gallet":0,"Yogurt":0,"Quesos":0,"Gomitas":0,"Mentas":0,"Chile ":0,"Deterg":0,"LimpVi":0,"Paleta":0,"Helado":0,"Cervez":0,"Desodor":0,"Escoba":0},0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
Cl4 = Cliente("Francisco Mesa",{"Tomate":0,"Frijol":0,"Yuca  ":0,"Papa  ":0,"Huevos":0,"Leche ":0,"Maiz  ":0,"Gallet":0,"Yogurt":0,"Quesos":0,"Gomitas":0,"Mentas":0,"Chile ":0,"Deterg":0,"LimpVi":0,"Paleta":0,"Helado":0,"Cervez":0,"Desodor":0,"Escoba":0},0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
Cl5 = Cliente("Juan Muelas",{"Tomate":0,"Frijol":0,"Yuca  ":0,"Papa  ":0,"Huevos":0,"Leche ":0,"Maiz  ":0,"Gallet":0,"Yogurt":0,"Quesos":0,"Gomitas":0,"Mentas":0,"Chile ":0,"Deterg":0,"LimpVi":0,"Paleta":0,"Helado":0,"Cervez":0,"Desodor":0,"Escoba":0},0,[0,0,0,0,0,0,0,0,0,0,0,0,0])
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
#/////////////////////////////////////////////////////////////////////////////////////////////
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
    DineroHoyTxt(Hora,Total)
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
      Menu = input('''---Caja---
 1: Caja
 2: Volver a tienda
 
 --> ''')
      if Menu == "1":
          Caja()
      elif  Menu == "2":
          VolverTienda()
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
            #print(i,j.Nom)
            if i == j.Nom:
                CodigoP.append(j.CP)
    print(CodigoP,ListaCaja)
    return CodigoP,ListaCaja
def Ajustes(ListaCaja,Total):
    global Stock
    
    
MenuCaja()