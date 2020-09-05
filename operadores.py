#Para hacer pruebas con datos de juego Parchis con Quiz.
def dado (dados):
    return dados

dado=int(input())

if dado in range (1, 13):
    print("avanza")

else:
    print ("número de dado inválido")
    
    #NOTA: cambie el codigo para que fuera en un solo if
