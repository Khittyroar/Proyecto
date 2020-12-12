# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:30:32 2020

@author: fhwx
"""
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
