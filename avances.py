
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

def dado(fic):  #fichas
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
    
    if fic==1:
        sacar_fichaA(dado)   #Asiganda a jugador 1
    elif fic==2:
        sacar_fichaB(dado,2)   #Para jugador 2
    else:                   # 2 si es contra maquina
        sacar_fichaB(dado, 1)  

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
        
        if tablero[0][0]=='1****' and tablero[0][1]=='2****':
            print('Gano', j1, '¡Congratulations!')
            input('Presiona Intro para salir')
            salir()
        elif tablero[10][10]=='1****' and tablero[10][9]=='2****':
            print('Gano', j2, '¡Congratulations!')
            input('Presiona Intro para salir')
            salir()
        else:
            print('Juega', j1)
            input('Presiona Intro para continuar')
            dado(1)
            print('Juega', j2)
            input('Presiona Intro para continuar')
            dado(2)
    while q==0 and x==1:
        
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
            #global tablero

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
    

 
