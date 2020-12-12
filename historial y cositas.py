def historial():
    Menu = print('''---Historial---
 1: Cambios Stock
 2: Ganacias
 3: Ediciones en Precios/Stock
 4: Salir''')
    if Menu == "1":
        MostrarCambiosStock() 
    elif Menu == "2":
        Ganacias()
    elif Menu == "3":
        EdiStockPrecios()
    elif Menu == "4":
        Salir()
        
 #////////////////////////////////////       
def MostrarCambiosStock():
    H = open("CambiosStock.txt","r")
    Copia = H.read()
    print(Copia)
#////////////////////////////////////////
def Ganacias():
    H = open("Ganacias.txt","r")
    Copia = H.read()
    print(Copia)
#//////////////////////////////////////
def EdiStockPrecios():
    H = open("ediciones.txt","r")
    Copia = H.read()
    print(Copia)
#////////////////////////////////////
def Salir():
    Pausa = input('''Regresando''')
    #Administrar()
#///////////////////////////////////////
def StockHoy():
    H = open("StockHoy.txt","r")
    Copia = H.read()
    print(Copia)
#///////////////////////////////////////
def DineroHoy():
    H = open("Dinero.txt","r")
    Copia = H.read()
    print(Copia)
#//////////////////////////////////    
M = 2/4
N = "hola"
H = open("Dinero.txt","w")
H.write(f"hola\n\notro renglon\t {M}{N}")
H.close()
H = open("Dinero.txt","r")
F = H.read()
print(F)
H.close()
