#Definimos la primera matriz
def matriz1():
    matriz1 = [] #Matriz vacía en la cual se agregaran elementos
    for i in range(filas): #Ciclo for para filas
        fila = []
        for j in range(columnas): #Ciclo for para columnas
            elemento = int(input("Ingrese el elemento de la matriz 1: ")) #Se solicita el ingreso de los elementos
            fila.append(elemento) #Se agrega elemento por elemento en cada fila de la matriz
        matriz1.append(fila) #Se agregan las filas a la matriz
    return matriz1 #Se retorna la matriz

#Definimos la primera matriz
def matriz2():
    matriz2 = [] #Matriz vacía en la cual se agregaran elementos
    for i in range(filas): #Ciclo for para filas
        fila = []
        for j in range(columnas): #Ciclo for para columnas
            elemento = int(input("Ingrese el elemento de la matriz 2: ")) #Se solicita el ingreso de los elementos
            fila.append(elemento) #Se agrega elemento por elemento en cada fila de la matriz
        matriz2.append(fila) #Se agregan las filas a la matriz
    return matriz2 #Se retorna la matriz

#Definimos la función para la suma de matrices
def sumaMatriz(matriz1, matriz2):
    matrizSuma = [] #Matriz vacía en la cual se agregaran elementos
    for i in range(len(matriz1)): #Ciclo for para recorrer los elementos de la matriz 1
        filaSuma = [] #Fila vacia
        for j in range(len(matriz1[0])): #Se recorre elemento por elemento de la matriz 1
            suma = matriz1[i][j] + matriz2[i][j] #Se realiza la operación de la suma entre los elementos de las matrices
            filaSuma.append(suma) #Se agrega elemento por elemento en cada fila
        matrizSuma.append(filaSuma) #Se agregan las filas a la matriz
    return matrizSuma #Retornamos la variable de matriz suma

#Definimos la función para la resta de matrices
def restaMatriz(matriz1, matriz2):
    matrizResta = [] #Matriz vacía en la cual se agregaran elementos
    for i in range(len(matriz1)): #Ciclo for para recorrer los elementos de la matriz 1
        filaResta = [] #Fila vacia
        for j in range(len(matriz1[0])): #Se recorre elemento por elemento de la matriz 1
            resta = matriz1[i][j] - matriz2[i][j] #Se realiza la operación de la resta entre los elementos de las matrices
            filaResta.append(resta) #Se agrega elemento por elemento en cada fila
        matrizResta.append(filaResta) #Se agregan las filas a la matriz
    return matrizResta #Retornamos la variable de matriz resta

if __name__ == "__main__":
    #Se solicita el ingreso de la cantidad de filas y columnas que tendrá la matriz
    filas = int(input("Ingrese la cantidad de filas que contendrá la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas que contendrá la matriz: "))
    #Se llaman las funciones definidas anteriormente
    matriz1 = matriz1()
    matriz2 = matriz2()
    matrizSuma = sumaMatriz(matriz1, matriz2)
    matrizResta = restaMatriz(matriz1, matriz2)
    #Se imprimen los resultados usando las funciones definidas, haciendo uso de un ciclo for para imprimir la matriz resultante
    print("Matriz 1:")
    for fila in matriz1:
        print(fila)
    print("Matriz 2:")
    for fila in matriz2:
        print(fila)
    print("Suma de matrices:")
    for fila in matrizSuma:
        print(fila)
    print("Resta de matrices:")
    for fila in matrizResta:
        print(fila)