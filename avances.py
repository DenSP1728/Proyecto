
import random
import os    #Biblioteca para limpiar la ventana 
import sys   #Biblioteca para cerrar el codigo automaticamente 

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

def limpiar():     #Funcion para limpiar la ventana de codigo
    if os.name=='posix':
        os.system('clear')
    elif os.name=='ce' or os.name=='nt' or os.name=='dos':
        os.system('cls')

def salir():    #Funcion para salir del juego automaticamente 
    limpiar()
    print('Se acabo el juego')
    input('Presiona Intro para salir')
    sys.exit()

def instrucciones():
    limpiar()
    print(' -Instruciones de juego- ')
    print()
    print('1. Para comenzar el juego cada jugador registra su nombre')
    print('2. Para sacar ficha de casa es necesario tirar 5')
    print('3. Gana el jugador que primero llegue a la meta')
    print()
    input('Presiona Intro para regresar a menu')
    menu()
    salir()    

          #_____________ Modificacion de codigo ____________
# matriz del primer jugador           
def pasosA(x,f):    
    #f es la ficha que mueve A1 o A2
    matriz_jugador= [[0 ,0 ,0, 0, 1,40,39, 0, 0, 0, 0],
                     [0 ,0, 0, 0, 2,41,38, 0, 0, 0, 0],
                     [0 ,0, 0, 0, 3,42,37, 0, 0, 0, 0],
                     [0 ,0, 0, 0, 4,43,36, 0, 0, 0, 0],
                     [9 ,8, 7, 6, 5,44,35,34,33,32,31],
                     [10,0, 0, 0, 0,45, 0, 0, 0, 0,30],
                     [11,12,13,14,15,0,25,26,27,28,29],
                     [0 ,0, 0, 0,16, 0,24, 0, 0, 0, 0],
                     [0 ,0, 0, 0,17, 0,23, 0, 0, 0, 0],
                     [0 ,0, 0, 0,18, 0,22, 0, 0, 0, 0],
                     [0 ,0, 0, 0,19,20,21, 0, 0, 0, 0]]

          # matriz del segundo jugador    
def pasos_B(p,f):
    #f es la ficha que mueve B1 o B2
    matriz_jugador= [[0 , 0, 0, 0,21,20,19, 0, 0, 0, 0],
                     [0 , 0, 0, 0,22, 0,18, 0, 0, 0, 0],
                     [0 , 0, 0, 0,23, 0,17, 0, 0, 0, 0],
                     [0 , 0, 0, 0,24, 0,16, 0, 0, 0, 0],
                     [29,28,27,26,25, 0,15,14,13,12,11],
                     [30, 0, 0, 0, 0,45, 0, 0, 0, 0,10],
                     [31,32,33,34,35,44, 5, 6, 7, 8, 9],
                     [0 , 0, 0, 0,36,43, 4, 0, 0, 0, 0],
                     [0 , 0, 0, 0,37,42, 3, 0, 0, 0, 0],
                     [0 , 0, 0, 0,38,41, 2, 0, 0, 0, 0],
                     [0 , 0, 0, 0,39,40,21, 0, 0, 0, 0]]
         #_____________ Modificacion de codigo ____________

def dado(f):  #fichas
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
        dado1 =  [[" __"," __"," __"],
                 ["/o ","   ","  o/"],
                 ["/o ","   ","  o/"],
                 ["/o "," __"," _o/"]]
        for i in range (4):
            for j in range (3):
                print (dado1[i][j], end = "")
            print ()
        print ("Sacaste", dado)
    limpiar()
    
    if f==1:
        sacar_fichaA(dado)   #Asiganda a jugador 1
    elif f==2:
        sacar_fichaB(dado,2)   #Para jugador 2
    else:                   # 2 si es contra maquina
        sacar_fichaB(dado, 1)  

# Para empezar el juego
def game(x):
    limpiar()
    j1=input('Ingresa nombre del Jugador 1: ')
    print()
    if x==2:
        j2=input('Ingresa nombre del Jugador 2: ')
    else:
        pass
    for i in range(11):
        for j in range(11):
            print(tablero[i][j], end='')
        print()
    q = 0
    while q==0 and x==2:
        #Si las fichas llegan a meta, imprime lo siguiente:
        if tablero[0][0]=='1****' and tablero[0][1]=='2****':
            print('Gano', j1, '¡Congratulations!')
            input('Presiona Intro para salir')
            salir()
        elif tablero[10][10]=='1****' and tablero[10][9]=='2****':
            print('Gano', j2, '¡Congratulations!')
            input('Presiona Intro para salir')
            salir()
        else:
          #En dado caso de que todavia no termine seguiran jugando
            print('Juega', j1)
            input('Presiona Intro para continuar')
            dado(1)
            print('Juega', j2)
            input('Presiona Intro para continuar')
            dado(2)
    while q==0 and x==1:
        # Mismo caso, pero aqui se juega contra maquina 
        if tablero[0][0]=='1****' and tablero[0][1]=='2****':
            print('Gano', j1, '¡Congratulations!')
            input('Presiona Intro para salir')
            salir()
        elif tablero[10][10]=='1****' and tablero[10][9]=='2****':
            print('Gana la maquina, suerte para la proxima')
            input('Presiona Intro para salir')
            salir()
        else:
            print('Juega', j1)
            input('Presiona Intro para continuar')
            dado(1)
            print('Sigue jugando la maquina')
            input('Presiona Intro para continuar')
            dado(0)
            
# ___Seleccion de jugadores___
def jugadores():
    limpiar()
    print('Selecciona los jugadores')
    print()
    print('Presiona 1 para jugar contra la maquina')
    print('Presiona 2 para dos jugaores')
    print()
    print('Presiona cualquier tecla para volver al menu')
    a = input('Respuesta: ')
    if a=='1':
        game(1)
    elif a=='2':
        game(2)
    else:
        limpiar()
        menu()
 
# Menu que conecta con las otras funciones principales 
def menu():  
    print('Hola, este es el juego de Parchis')
    print()
    print('Presiona 1 para jugar')
    print()
    print('Presiona 2 para ver instrucciones')
    print()
    print('Presiona 3 para salir')
    a= input('Respuesta: ')
    if a== '1':
       jugadores()
    elif a== '2':
       print(instrucciones())
    elif a== '3':
       print(salir())
menu()

#_______MODIFICAR_______


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
    

 
