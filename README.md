# Proyecto Juego
Denisse A. Sánchez Paz       | A01706668

# Proyecto Parchis 
Introducción:
¿Qué es Parchís?
El tablero del juego cuenta con una división de cuatro. Además, cada jugador dispone de cuatro fichas con colores identificativos: Amarillas, rojas, verdes o azules. Cada uno cuenta con su zona de inicio llamada casa. Alrededor se tiene 68 casillas numeradas para avanzar. Además, hay casillas de descanso que son seguros para reposar y evitar perder. En el centro del tablero, se encuentra el punto de objetivo donde se debe llegar.

# Contexto
Realizar un juego en Python que es similar al juego de mesa, Parchís, donde se permita de 1 a 2 jugadores, cada uno representado por una letra distinta en el tablero y cada uno tenga 2 fichas en su zona de inicio. Alrededor tendrá casillas (todavía sin delimitar) para avanzar, tendrá uno dado, una vez que se tiren los dados y nos muestre el número de espacios que disponemos para avanzar. El primer jugador que llegue al centro con sus 2 fichas ganara. 

# Instrucciones 
Descargar el arvhivo y correr en terminal con:

python avances.py

o abrir en Thonny o cualquier editor de python y dar boton de play.

Aparece un menu donde te pregunta que quieres hacer, jugar, ver instrucciones o salir de juego; al contestar te mandara a esa sección, si es ver instrucciones, apareceran las reglas, al terminar de leerlas te permite regresar a menú, en caso de seleccionar jugar, pregunta si jugaras solo o 1 contrar 1, seleccionas la opción y antes de jugar ingresaras nombre para que reconozcas cuando es tu turno; si en manu seleccionaste salir, simplemente terminara el programa.

# Bibiotecas incluidas 
random: Ofrece generadores de números pseudo-aleatorios para varias distribuciones. En este caso, permite el lanzamiento de un dado de forma aleatoria en un rango de 1 a 6.

sys: Tiene varias funcionalidades. Para el proyecto es utilizado para forzar el cierra del programa, es decir, cuando termineel juego o sea seleccionado en menú.

os: El módulo os también nos provee de un diccionario con las variables de entorno relativas al sistema. El programa cuenta con una funcion para limpiar el codigo en pantalla, dependiendo del sistema operativo ejecutara la accion de limpiar.
