# Condiciones para avanzar en juego, donde el número mayor es el jugador que empieza 
   
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
        
def sacar_ficha (dados_1, dado_2):
    return dados_1, dado_2

dado_1=int(input())
dado_2=int(input())

suma = dado_1 + dado_2
print(suma)

if suma == 5:
    print ("Saca 1 ficha")
    
elif  suma == 10:
    print ("Saca 2 fichas")
else:
    print (suma)
