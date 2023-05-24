# Reto #11 Matrices
Espero que se encuentren excelente estimados lectores, en el presente repositorio haremos varios ejemplos de código en Python utilizando lo aprendido acerca de las matrices dentro de nuestra clase de programación de computadores.

## Ejemplo No. 1
Diseñar un código, el cual al ejecutarlo permita el ingreso de dos matrices de determinado número de filas y columnas, y sume dichas matrices ingresadas.
El siguiente código, es la solución al problema descrito anteriormente:
```sh
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
```
Así se ve el programa funcionando:

![image](https://github.com/Artuu1999/Reto-11-Matrices/assets/124615034/48130788-7e38-4f2e-9d71-37b88e457038)


## Ejemplo No. 2
Crear un programa en Python que permita ingresar dos matrices y realizar el producto de estas dos matrices.
El código solución al anterior problema es:
```sh
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
```
De la siguiente manera se ve el programa funcionando:

![image](https://github.com/Artuu1999/Reto-11-Matrices/assets/124615034/9dc1b9db-12e5-41e0-a6de-8b34004fec9f)


## Ejemplo No. 3
Realizar un código que al correrse, obtenga la matriz transpuesta de una matriz ingresada por el usuario.
La solución al problema es la siguiente:
```sh
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
```
El programa funcionando:

![image](https://github.com/Artuu1999/Reto-11-Matrices/assets/124615034/1ece06b1-6172-49e9-a639-4db5b504e112)


## Ejemplo No. 4
Crear un código que permita sumar los elementos de una columna de una matriz ingresada.
La solución a continuación:
```sh
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
```
De la siguiente manera se puede observar el programa al ejecutarse:

![image](https://github.com/Artuu1999/Reto-11-Matrices/assets/124615034/2f7b546d-1f55-42cf-9efb-ec95e1fc79b2)


## Ejemplo No. 5
Diseñar un programa en Python que sume los elementos de una fila dada de una matriz ingresada por el usuario.
El código solución es el siguiente:
```sh
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
```
Al ejecutarse el programa se ve así:

![image](https://github.com/Artuu1999/Reto-11-Matrices/assets/124615034/1cee0f8d-7129-4210-bebd-3a47acaa834e)


## Fin
Hasta acá llega nuestro camino en el presente repo, espero que haya sido de tu interés, si encuentras algún error o alguna inconsistencia, no dudes en contactarme y hacermela saber.
Muchas Gracias por tu atención.

   **"Mi país, más que mi patria, mi raíz, más que mi suelo, la matriz que me enseñó a parir pensamientos"**
         - Ricardo Arjona
