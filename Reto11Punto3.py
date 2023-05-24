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

#Definimos la función para la matriz traspuesta
def matrizTraspuesta (matriz):
    #Determinamos la cantidad de elementos en las filas y columas
    filas = len(matriz)
    columnas = len(matriz[0])
    #Matriz vacías para agregar elementos
    traspuestaMatriz = []
    for j in range (columnas): #Ciclo for para las columnas
        filaTraspuesta = [] #Fila vacia
        for i in range (filas): #Ciclo for para las filas
            filaTraspuesta.append(matriz[i][j]) #Agregar los elementos recorridos inviertiendo las filas y columnas
        traspuestaMatriz.append(filaTraspuesta) #Se agregan las filas a la matriz traspuesta
    return traspuestaMatriz #Se retorna la matriz traspuesta
    
    
if __name__ == "__main__":
    #Se solicita el ingreso de la cantidad de filas y columnas que tendrá la matriz
    filas = int(input("Ingrese la cantidad de filas que contendrá la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas que contendrá la matriz: "))
    #Se llaman las funciones definidas anteriormente
    matriz = matriz()
    traspuestaMatriz = matrizTraspuesta (matriz)
    #Se imprimen los resultados usando las funciones definidas, haciendo uso de un ciclo for para imprimir la matriz resultante
    print("Matriz: ")
    for fila in matriz:
        print(fila)
    print("Matriz traspuesta:")
    for fila in traspuestaMatriz:
        print(fila)