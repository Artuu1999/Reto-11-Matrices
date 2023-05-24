#Definimos la matriz
def matriz():
    matriz = [] #Matriz vacía en la cual se agregaran elementos
    for i in range(filas): #Ciclo for para filas
        fila = []
        for j in range(columnas): #Ciclo for para columnas
            elemento = int(input("Ingrese el elemento de la matriz 1: ")) #Se solicita el ingreso de los elementos
            fila.append(elemento) #Se agrega elemento por elemento en cada fila de la matriz
        matriz.append(fila) #Se agregan las filas a la matriz
    return matriz #Se retorna la matriz

#Definimos la función para sumar los elementos de una columna
def sumarColumnas (matriz):
    #Se determina elemento de cada fila y columna
    filas = len(matriz)
    columnas = len(matriz[0])
    columnasSuma = [0] * columnas
    #Ciclo for para recorrer toda la matriz
    for j in range(columnas):
        for i in range(filas):
            columnasSuma[j] += matriz[i][j] #Sumar cada elemento de cada calumna
    return columnasSuma #Retornamos la función
     
if __name__ == "__main__":
    #Se solicita el ingreso de la cantidad de filas y columnas que tendrá la matriz
    filas = int(input("Ingrese la cantidad de filas que contendrá la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas que contendrá la matriz: "))
    #Se llaman las funciones definidas anteriormente
    matriz = matriz()
    columnasSuma = sumarColumnas(matriz)
    #Se imprimen los resultados usando las funciones definidas, haciendo uso de un ciclo for para imprimir la matriz resultante
    print("Matriz: ")
    for fila in matriz:
        print(fila)
    print("Suma de cada columna:")
    for i, suma in enumerate(columnasSuma):
     print("Columna "+str(i+1)+":", suma)