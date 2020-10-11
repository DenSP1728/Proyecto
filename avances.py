
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
def ubicacion_ficha1(x):   #Para ficha A1
    a=0
    b=0
    f=1
    
    for i in range(11):
        for j in range(11):
            if tablero[i][j]==' A1 /':
                print('La ubicacion es', i, j)
                a=i
                b=j
                break
            else:
                pass
    print(a,b)
    pasos(x,a,b,f)
        
def ubicacion_ficha2(x):   #Para ficha A2
    a=0
    b=0
    f=2
    for i in range(11):
        for j in range(11):
            if tablero[i][j]==' A2 /':
                print('La ubicacion es', i, j)
                a=i
                b=j
                break
            else:
                pass
    pasos(x,a,b,f)
    
def ubicacion_fichaB(x):     #Para ficha B1
    a=0
    b=0
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
    pasos_B(x,a,b,f)
    
def ubicacion_fichaB2(x):     #Para ficha B2
    a=0
    b=0
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
    pasos_B(x,a,b,f)
          
def pasos(p,x,v,f):    
    #x representa fila
    #v es la columna
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
    #Son los pasos que deben dar en el tablero parchis 
    k=x
    t=v
    #k es fila y t es columna
    u=0
    y=matriz_jugador[x][v]
    cont=0
    while cont < p:
        #Aumenta filas
        if y==matriz_jugador[0][4] or y==matriz_jugador[1][4] or y==matriz_jugador[2][4] or y==matriz_jugador[3][4]:
            y==matriz_jugador[x + 1][v]
            cont= cont + 1
            x= x + 1
        
        #Disminuye filas
        elif y==matriz_jugador[4][4] or y==matriz_jugador[4][3] or y==matriz_jugador[4][2] or y==matriz_jugador[4][1]:
            y==matriz_jugador[x][v-1]
            cont= cont + 1
            v= v - 1
        
        elif y==matriz_jugador[4][0] or y==matriz_jugador[5][0]:
            y==matriz_jugador[x + 1][v]
            cont= cont + 1
            x= x + 1
        elif y==matriz_jugador[6][0] or y==matriz_jugador[6][1] or y==matriz_jugador[6][2] or y==matriz_jugador[6][3]:
            y==matriz_jugador[x][v+1]
            cont= cont + 1
            v = v + 1
        elif y==matriz_jugador[6][4] or y==matriz_jugador[7][4] or y==matriz_jugador[8][4] or y==matriz_jugador[9][4]:
            y==matriz_jugador[x + 1][v]
            cont= cont + 1
            x= x + 1
        elif y==matriz_jugador[10][4] or y==matriz_jugador[10][5]:
            y==matriz_jugador[x][v+1]
            cont= cont + 1
            v= v + 1
        elif y==matriz_jugador[10][6] or y==matriz_jugador[9][6] or y==matriz_jugador[8][6] or y==matriz_jugador[7][6]:
            y==matriz_jugador[x - 1][v]
            cont= cont + 1
            x= x - 1
        elif y==matriz_jugador[6][6] or y==matriz_jugador[6][7] or y==matriz_jugador[6][8] or y==matriz_jugador[6][9]:
            y==matriz_jugador[x][v+1]
            cont= cont + 1
            v= v + 1
        elif y==matriz_jugador[6][10] or y==matriz_jugador[5][10]:
            y==matriz_jugador[x - 1][v]
            cont= cont + 1
            x= x - 1
        elif y==matriz_jugador[4][10] or y==matriz_jugador[4][9] or y==matriz_jugador[4][8] or y==matriz_jugador[4][7]:
            y==matriz_jugador[x][v-1]
            cont= cont + 1
            v= v - 1
        elif y==matriz_jugador[4][6] or y==matriz_jugador[3][6] or y==matriz_jugador[2][6] or y==matriz_jugador[1][6]:
            y==matriz_jugador[x - 1][v]
            cont= cont + 1
            x= x - 1
        elif y==matriz_jugador[0][6]:
            y==matriz_jugador[x][v-1]
            cont= cont + 1
            v= v - 1
        elif y==matriz_jugador[0][5] or y==matriz_jugador[1][5] or y==matriz_jugador[2][5] or y==matriz_jugador[3][5]:
            y==matriz_jugador[x + 1][v]
            cont= cont + 1
            x=x + 1
        elif y==matriz_jugador[4][5] and p==1 or p-cont==1:
            print('Coronaste ficha')
            tablero[k][t]='____/'
            u=1
            cont=7
            if f==1:
                tablero[0][0]='1****'
            else:
                tablero[0][1]='2****'
        
        #Si la ficha no llega exactamente, disminuye las fichas
        elif y==matriz_jugador[4][5] and p>1 or p-cont>1:
            g= p - cont
            y= matriz_jugador[x - g][v]
            cont = 7
            x = x - g + 2
        else:
            cont=7
    print('La posicion final', x,v)
    
    if tablero[x][v]==' A1 /' and f==1:
        tablero[x][v]=' A1 /'
        
    elif tablero[x][v]==' A2 /' and f==2:
        tablero[x][v]=' A2 /'
    elif tablero[x][v]==' B1 /':
        comer(x,v,k,t,f,1)
    
    elif tablero[x][v]==' B2 /':
        comer(x,v,k,t,f,2)
    
    else:
        actualizar(x,v,k,t,f)   

def pasos_B(p,x,v,f,e):
    #x representa fila
    #v es la columna
    #f es la ficha que mueve B1 o B2
    #e en caso de ser la maquina 
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
    #Son los pasos que deben dar en el tablero parchis 
    k=x
    t=v
    #k es fila y t es columna
    u=0
    y=matriz_jugador[x][v];
    cont=0
    while cont < p:
        #Aumenta filas
        if y==matriz_jugador[0][4] or y==y==matriz_jugador[1][4] or y==matriz_jugador[2][4] or y==matriz_jugador[3][4]:
            y==matriz_jugador[x + 1][v]
            cont= cont + 1
            x= x + 1
        
        #Disminuye filas
        elif y==matriz_jugador[4][4] or y==y==matriz_jugador[4][3] or y==matriz_jugador[4][2] or y==matriz_jugador[4][1]:
            y==matriz_jugador[x][v-1]
            cont= cont + 1
            v= v - 1
        
        elif y==matriz_jugador[4][0] or y==y==matriz_jugador[5][0]:
            y==matriz_jugador[x + 1][v]
            cont= cont + 1
            x= x + 1
        elif y==matriz_jugador[6][0] or y==y==matriz_jugador[6][1] or y==matriz_jugador[6][2] or y==matriz_jugador[6][3]:
            y==matriz_jugador[x][v+1]
            cont= cont + 1
            v = v + 1
        elif y==matriz_jugador[6][4] or y==y==matriz_jugador[7][4] or y==matriz_jugador[8][4] or y==matriz_jugador[9][4]:
            y==matriz_jugador[x + 1][v]
            cont= cont + 1
            x= x + 1
        elif y==matriz_jugador[10][4]:
            y==matriz_jugador[x][v+1]
            cont= cont + 1
            v= v + 1
        elif y==matriz_jugador[10][6] or y==y==matriz_jugador[9][6] or y==matriz_jugador[8][6] or y==matriz_jugador[7][6]:
            y==matriz_jugador[x - 1][v]
            cont= cont + 1
            x= x - 1
        elif y==matriz_jugador[6][6] or y==y==matriz_jugador[6][7] or y==matriz_jugador[6][8] or y==matriz_jugador[6][9]:
            y==matriz_jugador[x][v+1]
            cont= cont + 1
            v= v + 1
        elif y==matriz_jugador[6][10] or y==y==matriz_jugador[5][10]:
            y==matriz_jugador[x - 1][v]
            cont= cont + 1
            x= x - 1
        elif y==matriz_jugador[4][10] or y==y==matriz_jugador[4][9] or y==matriz_jugador[4][8] or y==matriz_jugador[4][7]:
            y==matriz_jugador[x][v-1]
            cont= cont + 1
            v= v - 1
        elif y==matriz_jugador[4][6] or y==y==matriz_jugador[3][6] or y==matriz_jugador[2][6] or y==matriz_jugador[1][6]:
            y==matriz_jugador[x - 1][v]
            cont= cont + 1
            x= x - 1
        elif y==matriz_jugador[0][6] or y==matriz_jugador[0][5]:
            y==matriz_jugador[x][v-1]
            cont= cont + 1
            v= v - 1
        elif y==matriz_jugador[10][5] or y==y==matriz_jugador[9][5] or y==matriz_jugador[8][5] or y==matriz_jugador[7][5]:
            y==matriz_jugador[x - 1][v]
            cont= cont + 1
            x= x - 1
        elif y==matriz_jugador[6][5] and p==1 or p-cont==1:
            print('Coronaste ficha')
            tablero[k][t]='____/'
            u=1
            cont=7
            
            if f==1:
                tablero[10][10]='1****'
            else:
                tablero[10][9]='2****'
        
        #avanzar y devolver a la llegada 
        elif y==matriz_jugador[6][5] and p>1 or cont - p >1:
            g= p - cont -2
            y= matriz_jugador[x + g][v]
            cont = 7
            x = x + g 
        else:
            print('Algo anda mal')
            
    print('La posicion final', x,v)
    if tablero[x][v]==' B2 /' and f==1:
        print('No puede estar en la misma posicion')
        #seleccionar_ficha(p, e)
    elif tablero[x][v]==' B1 /' and f==2:
        print('No puede estar en la misma posicion')
        #seleccionar_ficha(p, e)
    
    elif tablero[x][v]==' B1 /' and f==1:
        tablero[x][v]=' B1 /'
        
    elif tablero[x][v]==' B2 /' and f==2:
        tablero[x][v]=' B2 /'
        #mostrar2()
        
    elif tablero[x][v]==' A1 /':
        comer1(x,v,k,t,f,1)
    elif tablero[x][v]==' A2 /':
        comer1(x,v,k,t,f,2)
    
    else:
        actualizarb(x,v,k,t,f)
         #_____________ Modificacion de codigo ____________

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
    

 
