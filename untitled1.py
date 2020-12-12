class Cliente:
    def __init__(A,Nombre,Productos,DineroGastado,Horario):
        A.Prod = Productos
        A.Dinero = DineroGastado
        A.Horario = Horario
        A.Nom = Nombre
Jhon = Cliente("Jhon",{"Tomate":0,"Frijoles":0,"Yuca":2,"Papa":0,"Esfero":1},3000,[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

Maria = Cliente("Maria",{"Tomate":0,"Frijoles":0,"Yuca":2,"Papa":0,"Esfero":1},3000,[0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0])

Jose = Cliente("Jose",{"Tomate":1,"Frijoles":0,"Yuca":1,"Papa":0,"Esfero":1},3000,[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
Clientes = [Jhon,Maria,Jose]
Nombres= [Jhon.Nom,Maria.Nom,Jose.Nom]
Productos = ["Tomate","Frijoles","Yuca","Papa","Esfero"]
J = 4
M = 2
JS = 1
def Horario():
    Contador = 1
    for i in Clientes:
        Contador = 1
        print(i.Nom,end = " ")
        for j in Productos:
            if i == Jose and j == "Frijoles":
                i.Prod[j] = i.Prod[j] + J
            elif i == Maria and j == "Tomate":
                i.Prod[j] = i.Prod[j] + M
            elif i == Jhon and j == "Yuca":
                i.Prod[j] = i.Prod[j] + JS
            print(i.Prod[j],end = " ")
            if Contador == len(Productos):
                print(i.Prod[j])
            Contador += 1
            
Horario()
#def Productos():
#def DineroGastado():