import random

#Definimos el tablero
tablero= [["*****","*****","*****","*****","_____","_____","_____","*****","*****","*****","*****"],
          ["*****","*****","*****","*****","_____","_____","_____","*****","*****","*****","*****"],
          ["*****","*****","*****","*****","_____","_____","_____","*****","*****","*****","*****"],
          [" A1 /"," A2 /","*****","*****","_____","_____","_____","*****","*****","*****","*****"],
          ["_____","_____","_____","_____","_____","_____","_____","_____","_____","_____","_____"],
          ["_____","_____","_____","_____","_____"," Meta","_____","_____","_____","_____","_____"],
          ["_____","_____","_____","_____","_____","_____","_____","_____","_____","_____","_____"],
          ["_____","_____","_____","_____","_____","_____","_____"," B1 /"," B2 /","*****","*****"],
          ["*****","*****","*****","*****","_____","_____","_____","*****","*****","*****","*****"],
          ["*****","*****","*****","*****","_____","_____","_____","*****","*****","*****","*****"],
          ["*****","*****","*****","*****","_____","_____","_____","*****","*****","*****","*****"]]

def menu():
    print('Hola, este es el juego de Parchis')
    print()
    print('Presiona 1 para jugar')
    print()
    print('Presiona 2 para ver instrucciones')
    print()
    print('Presiona 3 para salir')
    a = input('Respuesta: ')
    if a == '1':
         jugar()   #funcion que conecte con menu, sin definir
    elif a == '2':
         instrucciones()   #sin definir
    elif a == '3':
         salir()   #sin definir 
def dado():
    dado = random.randint (1,6)
    
    if dado == 1:
        dado1 = [[" __"," __"," __"],
                 ["/  ","   ","   /"],
                 ["/  "," o ","   /"],
                 ["/_ "," __"," __/"]]
        for i in range (4):
            for j in range (3):
                print (dado1[i][j], end = "")
            print ()
        print ("Sacaste", dado)
    
    elif dado == 2:
        dado1 = [[" __"," __"," __"],
                 ["/o ","   ","   /"],
                 ["/  ","   ","   /"],
                 ["/_ "," __"," _o/"]]
        for i in range (4):
            for j in range (3):
                print (dado1[i][j], end = "")
            print ()
        print ("Sacaste", dado)
    
    elif dado == 3:
        dado1 = [[" __"," __"," __"],
                 ["/o ","   ","   /"],
                 ["/  "," o ","   /"],
                 ["/_ "," __"," _o/"]]
        for i in range (4):
            for j in range (3):
                print (dado1[i][j], end = "")
            print ()
        print ("Sacaste", dado)
        
    elif dado == 4:
        dado1 = [[" __"," __"," __"],
                 ["/o ","   ","  o/"],
                 ["/  ","   ","   /"],
                 ["/o "," __"," _o/"]]
        for i in range (4):
            for j in range (3):
                print (dado1[i][j], end = "")
            print ()
        print ("Sacaste", dado)
        
    elif dado == 5:
        dado1 = [[" __"," __"," __"],
                 ["/o ","   ","  o/"],
                 ["/  "," o ","   /"],
                 ["/o "," __"," _o/"]]
        for i in range (4):
            for j in range (3):
                print (dado1[i][j], end = "")
            print ()
        print ("Sacaste", dado)
        
    else:
        dado1 = [[" __"," __"," __"],
                 ["/o ","   ","  o/"],
                 ["/o ","   ","  o/"],
                 ["/o "," __"," _o/"]]
        for i in range (3):
            for j in range (4):
                print (dado1[i][j], end = "")
            print ()
        print ("Sacaste", dado)
print(dado())

#_______MODIFICAR_______
#AVANCE 3 ESTRUCTURA DE DESICIONES.
#Eleccion de color para el jugador, escogiendo un color del 1 al 3, si no le toca verde 
def elegir_color (color):
    return color
color = int (input("Escoge color:   "))

if color == 1:
    print ("Color de jugador es:", "amarillo")
elif color == 2:
    print ("Color de jugador es:", "verde")
elif color == 3:
    print ("Color de jugador es:", "azul")
else:
    print ("Color de jugador es:", "rojo")
      
      
# CONDICIONES: para avanzar en juego, donde el número mayor es el jugador que empieza    
def casillas (jugador_1, jugador_2, jugador_3):
    return jugador_1 or jugador_2 or jugador_3

jugador_1 = int(input())
jugador_2 = int(input())
jugador_3 = int(input())
    
if jugador_1 > jugador_2 and jugador_1 > jugador_3:
        print ("comienza partida","jugador_1")
        
elif jugador_2 > jugador_1 and jugador_2 > jugador_3:
        print ("comienza partida","jugador_2")
        
elif jugador_3 > jugador_1 and jugador_3 > jugador_2:
        print ("comienza partida","jugador_3")
               


#El jugador deberá sacar ficha si la suma de ambos dados es un 5, por ejemplo 2+3.
#También es posible sacar 5 y 5 y sacar dos fichas en el mismo turno.

#---OPERADORES CON DESICION---  
# NOTA AVANCE CICLO: Ciclo while de tiro, para que solo hasta que saque 5.
       # marque que puede sacar ficha.
while True:
    dado = random.randint(1,6)
    print ("Sin ficha- Dado arroja:", dado) 
    
    if dado == 5:
        print ("Sacas ficha")
        
    x = input("¿Volver a tirar?")
    if x == "no":
        break
    

  #---Para hacer pruebas con datos de juego Parchis con Quiz----
def dado (dados):
    return dados

dado=int(input())

if dado in range (1, 13):
    print("avanza")

else:
    print ("número de dado inválido")
    
    #NOTA: cambie el codigo para que fuera en un solo if
