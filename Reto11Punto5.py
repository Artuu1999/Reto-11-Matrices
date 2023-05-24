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
def sumarFilas(matriz):
    #Filas y colimnas
    filas = len(matriz)
    columnas = len(matriz[0])
    # Fila vacía para agregar elementos y definir
    filasSuma = []
    #Ciclo for para iterar sobre cada elemento de fila en la matriz
    for i in range(filas):
        suma = 0
        #Ciclo for para actualizar la suma sobre todos los elementos de la fila
        for j in range(columnas):
         suma += matriz[i][j]
        filasSuma.append(suma) #Agregar llos elementos de la suma a la lista de filasSuma
    return filasSuma

if __name__ == "__main__":
    #Se solicita el ingreso de la cantidad de filas y columnas que tendrá la matriz
    filas = int(input("Ingrese la cantidad de filas que contendrá la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas que contendrá la matriz: "))
    #Se llaman las funciones definidas anteriormente
    matriz = matriz()
    filasSuma = sumarFilas(matriz)
    #Se imprimen los resultados usando las funciones definidas, haciendo uso de un ciclo for para imprimir la matriz resultante
    print("Matriz: ")
    for fila in matriz:
        print(fila)
    print("Suma de cada fila:")
    for i, suma in enumerate(filasSuma):
     print("Fila "+str(i+1)+":", suma)