
import random   #Biblioteca para sacar numeros aleatorios, en este codigo depende de un rango.
import os    #Biblioteca para limpiar la consola de ejecución dependiendo del sistema operativo.
import sys   #Biblioteca para hacer una acción del sistema, en este caso hacer un cierre forzado cuando se indique.

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

def limpiar():     #Funcion para limpiar la ventana de consola.
    if os.name=='posix':    #Depende del sistema operetivo.
        os.system('clear')
    elif os.name=='ce' or os.name=='nt' or os.name=='dos':
        os.system('cls')

def salir():    #Funcion para salir del juego automaticamente cuando se acabe el juego.
    limpiar()    #O cuando el jugador quiera salir desde el menu.
    print('Se acabo el juego')
    input('Presiona Intro para salir')
    sys.exit()

def instrucciones():    #Las instrucciones del juego.
    limpiar()
    print(' -Instruciones de juego- ')
    print()
    print('1. Selecciona en Jugar, si quieres 1 vs 1 o 1 vs maquina')
    print('2. Cada jugador tiene 2 fichas')
    print('3. Para sacar ficha de casa es necesario tirar 5')
    print('4. Gana el primero en llegar a la meta')
    print('5. Al terminar el juego, este saldra automaticamnete')
    print()
    input('Presiona Intro para regresar a menu')
    menu()
    salir()    

          #_____________ Modificacion de codigo ____________
   #_____ Condiciones para sacar fichas del jugador 1 ____
def sacar_fichaA(x):
    limpiar()
    #condiciones para sacar fichas
    if x==5 and tablero[3][0]== ' A1 /' and tablero[3][1]==' A2 /' and tablero[0][4]=='____/' and tablero[0][0]=='*****' and tablero[0][1]=='*****':
        tablero[0][4]=' A1 /'
        tablero[3][0]='     '

    elif x==5 and tablero[3][0]== ' A1 /' and tablero[0][4]=='____/' and tablero[0][0]=='*****' and tablero[0][1]=='*****':
        tablero[0][4]=' A1 /'
        tablero[3][0]='     '
    
    elif x==5 and tablero [3][0]!= ' A1 /' and tablero [3][1]== ' A2 /' and tablero[0][4]=='____/' and tablero[0][0]=='*****':
        tablero[0][4]= ' A2 /'
        tablero[3][1]= '     
   
    else:    #- En caso de no sacar un 5 en dado imprimir el tablero y un mensaje que diga que el dado es diferente.
        for i in range(11):
            for j in range(11):
                print(tablero[i][j], end="")
            print()
        print('dado es diferente de 5')

    #_____ Condiciones para sacar fichas del jugador 2 ____
def sacar_fichaB(x,e):
    limpiar()
   #Condiciones para sacar fichas 
    if x==5 and tablero[7][7]==' B1 /' and tablero[7][8]==' B2 /' and tablero[10][6]=='____/' and tablero[10][10]=='*****' and tablero[10][9]=='*****':
        tablero[10][6]=' B1 /'
        tablero[7][7]='     '
        
    elif x==5 and tablero[7][7]==' B1 /' and tablero[10][6]=='____/' and tablero[10][10]=='*****' and tablero[10][9]=='*****':
        tablero[10][6]=' B1 /'
        tablero[7][7]='     '
        
    elif x==5 and tablero[7][7]==' B2 /' and tablero[7][8]==' B2 /' and tablero[10][6]=='____/' and tablero[10][10]=='*****' and tablero[10][8]=='*****':
        tablero[10][6]=' B2 /'
        tablero[7][8]='     '
    
    else:
        for i in range(11):
            for j in range(11):
                print(tablero[i][j], end="")
            print()

   ### ACTUALIZAR LOS MOVIMIENTOS EN TABLERO###
def actualizarA(k,t,i,j,f):
    limpiar()
    if f==1:
        tablero[k][t]='____/'
        tablero[i][j]=' A1 /'
        for i in range(11):
            for j in range(11):
                print(tablero[i][j], end="")
            print()
        print('movio ficha A1')
    else:
        tablero[k][t]='____/'
        tablero[j][j]=' A2 /'
        for i in range(11):
            for j in range(11):
                print(tablero[i][j], end="")
            print()
        print('movio ficha A2')
        
def actualizarb(k,t, i,j, f):
    limpiar()
    if f==1:
        tablero[k][t]='____/'
        tablero[i][j]=' B1 /'
        for i in range(11):
            for j in range(11):
                print(tablero[i][j], end="")
            print()
        print('movio ficha B1')
    else:
        tablero[k][t]='____/'
        tablero[i][j]=' B2 /'
        for i in range(11):
            for j in range(11):
                print(tablero[i][j], end="")
            print()
        print('movio ficha B2')
   # # # # # # # # # # # # # # # #
          
   # ____ La ubicación de las fichas: _____
# Al resivir la ubicación imprima cual es la ubicación de la ficha y mandar a función mover 
def ubicacion_ficha1(x, i, j):   
    k=i
    t=j
    f=1
    for i in range(11):
        for j in range(11):
            if tablero[i][j]==' A1 /':
                print('La ubicacion es', i, j)
                break
            else:
                pass
    moverA(x,i,j,f)
# Misco que caso, pero para ficha 2        
def ubicacion_ficha2(x, i, j):
    k=i
    t=j
    f=2
    for i in range(11):
        for j in range(11):
            if tablero[i][j]==' A2 /':
                print('La ubicacion es', i, j)
                break
            else:
                pass
    moverA(x,i,j,f)
  
# Ubicaciones de fichas b        
def ubicacion_fichaB(x, i, j):
    k=i
    t=j
    f=1
    for i in range(11):
        for j in range(11):
            if tablero[i][j]==' B1 /':
                print('La ubicacion es', i, j)
                a=i
                b=j
                break
            else:
                pass
    moverB(x,a,b,f)
  
 # Ubicaciones de fichas b
def ubicacion_fichaB2(x, i, j):
    k=i
    t=j
    f=2
    for i in range(11):
        for j in range(11):
            if tablero[i][j]==' B1 /':
                print('La ubicacion es', i, j)
                a=i
                b=j
                break
            else:
                pass
    moverB(x,a,b,f)

          # MATRICES #
  # matriz del primer jugador     
def moverA(x,i,j,f):    
    k= i #Guardara la variable inicial 
    t= j
    #f es la ficha que mueve B1 o B2
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
    #Son los pasos que deben dar en el tablero parchis 
    cont=0
    #un bucle para delimitar las direcciones que debe llevar la ficha
    while cont < x: 
        if matriz_jugador[0][4] or matriz_jugador[1][4] or matriz_jugador[2][4] or matriz_jugador[3][4]:
            cont= cont + 1
            i=i+x
                
        elif matriz_jugador[4][4] or matriz_jugador[4][3] or matriz_jugador[4][2] or matriz_jugador[4][1]:
            cont= cont + 1
            j=j-x
                
        elif matriz_jugador[4][0] or matriz_jugador[5][0] or matriz_jugador[6][0]:
            cont= cont + 1
            i=i+x
            
        elif matriz_jugador[6][1] or matriz_jugador[6][2] or matriz_jugador[6][3] or matriz_jugador[6][4]:
            cont= cont + 1
            j=j+x
        
        elif matriz_jugador[6][4] or matriz_jugador[7][4] or matriz_jugador[8][4] or matriz_jugador[9][4]:
            cont= cont + 1
            i=i+x
        
        elif matriz_jugador[10][4] or matriz_jugador[10][5] or matriz_jugador[10][6]:
            cont= cont + 1
            j=j+x
                
        elif matriz_jugador[9][6] or matriz_jugador[8][6] or matriz_jugador[7][6]:# or matriz_jugador[6][6]:
            matriz_jugador[i-1][j]
            cont= cont + 1
            i=i-x
        
        elif matriz_jugador[6][6] or matriz_jugador[6][7] or matriz_jugador[6][8] or matriz_jugador[6][9]:
            cont= cont + 1
            j=j+x
                
        elif matriz_jugador[6][10] or matriz_jugador[5][10]: # subir 
            cont= cont + 1
            i=i-x
                
        elif matriz_jugador[4][10] or matriz_jugador[4][9] or matriz_jugador[4][8] or matriz_jugador[4][7]:
                cont= cont + 1
                j=j-x
        
        elif matriz_jugador[4][6] or matriz_jugador[3][6] or matriz_jugador[2][6] or matriz_jugador[1][6]: 
                cont= cont + 1
                i=i-x
                
        elif matriz_jugador[0][6] or matriz_jugador[0][5]:  #paso 40
                cont= cont + 1
                j=j-x
                
        elif matriz_jugador[0][5] or matriz_jugador[1][5] or matriz_jugador[2][5] or matriz_jugador[3][5] or matriz_jugador[4][5]: 
                cont= cont + 1
                i=i+x
                
        elif matriz_jugador[6][5] and x==1 or x-cont==1:
            print('Ficha llega a meta')
            tablero[i][j]='____/'
            cont=7
            
            if f==1:
                tablero[10][10]='1****'
            else:
                tablero[10][9]='2****'
      #Nos indica si la cicha no llega exactamente debe disminuir
        elif matriz_jugador[4][5] and x>1 or x-cont>1:
            g= x-cont
            matriz_jugador[i-g][j]
            cont=7
            i=i-g+2
    #imprima los cambios
    actualizarA(k, t, i, j, f)
         
# matriz del segundo jugador    
def moverB(p,x,v,f):
    k=i
    t=j
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
                     [0 , 0, 0, 0,39,40, 1, 0, 0, 0, 0]]
    
#Son los pasos que deben dar en el tablero parchis 
    cont=0
    while cont < x:
        if matriz_jugador[0][4] or matriz_jugador[1][4] or matriz_jugador[2][4] or matriz_jugador[3][4]:
            cont= cont + 1
            i=i + x
        
        elif matriz_jugador[4][4] or matriz_jugador[4][3] or matriz_jugador[4][2] or matriz_jugador[4][1]:
            cont= cont + 1
            j=j - x
        
        elif matriz_jugador[4][0] or matriz_jugador[5][0]:
            cont= cont + 1
            i=i + x
                    
        elif matriz_jugador[6][0] or matriz_jugador[6][1] or matriz_jugador[6][2] or matriz_jugador[6][3]:
            cont= cont + 1
            j=j + x
          
        elif matriz_jugador[6][4] or matriz_jugador[7][4] or matriz_jugador[8][4] or matriz_jugador[9][4]:
            cont= cont + 1
            i=i + x
                    
        elif matriz_jugador[10][4]:
            cont= cont + 1
            j=j + x
          
        elif matriz_jugador[10][6] or matriz_jugador[9][6] or matriz_jugador[8][6] or matriz_jugador[7][6]:
            cont= cont + 1
            i=i - x
          
        elif matriz_jugador[6][6] or matriz_jugador[6][7] or matriz_jugador[6][8] or matriz_jugador[6][9]:
            cont= cont + 1
            j=j + x
          
        elif matriz_jugador[6][10] or matriz_jugador[5][10]:
            cont= cont + 1
            i=i - x
          
        elif matriz_jugador[4][10] or matriz_jugador[4][9] or matriz_jugador[4][8] or matriz_jugador[4][7]:
            cont= cont + 1
            j=j -x
          
        elif matriz_jugador[4][6] or matriz_jugador[3][6] or matriz_jugador[2][6] or matriz_jugador[1][6]:
            cont= cont + 1
            i= i - x
          
        elif matriz_jugador[0][6] or matriz_jugador[0][5]:
            cont= cont + 1
            j=j - x
          
        elif matriz_jugador[10][5] or matriz_jugador[9][5] or matriz_jugador[8][5] or matriz_jugador[7][5]:
            cont= cont + 1
            i=i - x
          
        elif matriz_jugador[6][5] and x==1 or x-cont==1:
            print('Llega ficha a meta')
            tablero[i][j]='____/'
            cont=7
            
            if f==1:
                tablero[10][10]='1****'
            else:
                tablero[10][9]='2****'
         
        elif matriz_jugador[6][5] and x>1 or cont - x >1:
            g= x - cont -2
            cont = 7
            i=i + g 
        actualizarb(k,t, i,j, f)
#__________ Modificacion ______________

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
