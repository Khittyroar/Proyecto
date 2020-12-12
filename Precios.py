# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:53:10 2020

@author: fhwx
"""
def Precios():
    Menu = input('''---Historial---
 1: Cambiar Precios
 2: Mostrar Precios
 3: Agregar Promociones *
 4: Volver a Administraciones
 
 --> ''')
    if Menu == "1":
        CambiarPrecios(Produc,NuevoPrecio)
    elif Menu == "2":
        MostrarPrecios()
    elif Menu == "3":
        EdiStockPrecios()
    elif Menu == "4":
        Salir()
    
#/////////////////////////////////////////////////////
def CambiarPrecios(Produc,NuevoPrecio):
    import time
    global Productos
    for i in Productos:
        if Produc == i.Nom:        
            i.Precio = NuevoPrecio
            P = open("EdicionesPrecios.txt","a")
            P.write(f"{Hora} :: {Produc} | {i.Precio}  --> {Produc} | {NuevoPrecio} \n ")
            P.close()
#//////////////////////////////////////
def MostrarPrecios():
    global Productos
    for i in Productos:
        print(f"{i.Nom} | {i.Precios}")
    Pausa = input("Regresando")
#//////////////////////////////////////////////////
def VolverAdmin():
    