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

#Definimos la función del producto de matrices
def productoMatriz(matriz1, matriz2):
    #Para realizar el producto se deben obtener los elemento de cada fila y da cada columna por aparte
    filasMatriz1 = len(matriz1)
    columnasMatriz1 = len(matriz1[0])
    filasMatriz2 = len(matriz2)
    columnasMatriz2 = len(matriz2[0])
    # Se crea unamatriz vacia en la cual se agregaran los elementos
    matrizProducto = []
    for i in range(filasMatriz1): #Ciclo for para recorrer las filas de la matriz1
        filaProducto = [] 
        for j in range(columnasMatriz2): #Ciclo for para recorrer los elementos de las columnas de la matriz 2
            producto = 0
            for k in range(columnasMatriz1): #Dentro de dicho bucle se crea otro para las columnas de la amtriz 2
                producto += matriz1[i][k] * matriz2[k][j] #Se realiza como tal la multiplicación
            filaProducto.append(producto) #Se agregan los elementos del producto a cada fila
        matrizProducto.append(filaProducto) #Se agregan las filas a la matriz
    return matrizProducto #Se retorna la función


if __name__ == "__main__":
    #Se solicita el ingreso de la cantidad de filas y columnas que tendrá la matriz
    filas = int(input("Ingrese la cantidad de filas que contendrá la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas que contendrá la matriz: "))
    #Se llaman las funciones definidas anteriormente
    matriz1 = matriz1()
    matriz2 = matriz2()
    matrizProducto = productoMatriz(matriz1, matriz2)
    #Se imprimen los resultados usando las funciones definidas, haciendo uso de un ciclo for para imprimir la matriz resultante
    print("Matriz 1: ")
    for fila in matriz1:
        print(fila)
    print("Matriz 2:")
    for fila in matriz2:
        print(fila)
    print("Producto de matrices:")
    for fila in matrizProducto:
        print(fila)