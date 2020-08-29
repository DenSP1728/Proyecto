#Para hacer pruebas con datos de juego Parchis con Quiz.
def dado (dados):
    return dados

dado=int(input())

if dado in range (1, 13):
    print("avanza")

if dado == 0:
    print ("nulo")
    
elif dado >13:
    print ("numero de dado no existe")
    
#Si se encuentra en rango (1, 13) es un numero existente y puede avanzar, de otro modo se considera nulo.
