# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:37:56 2020

@author: fhwx
"""
class Producto:
        def __init__(A,Nombre,CodigoProducto,Marca,Precio,Cantidad,CantidadEstanteria,Vendidos):
            A.Nom = Nombre
            A.Precio = Precio
            A.Cant = Cantidad
            A.Vendidos = Vendidos
            A.CP = CodigoProducto
            A.Marca = Marca
            A.CantEsta = CantidadEstanteria
Cl1 = Producto("Frijol",1,"LaAbuelita",3000,12,10,0)
Cl2 = Producto("Arroz ",2,"LaAbuelita",5000,6,10,0)
Cl3 = Producto("Huevos",3,"SantaMaria",4500,32,10,1)
Cl4 = Producto("Leche ",4,"SantaMaria",2000,10,10,14)
Productos = (Cl1,Cl2,Cl3,Cl4)
def Stock():
    
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