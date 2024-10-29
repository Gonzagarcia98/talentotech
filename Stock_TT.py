# 1. Menú interactivo para cargar productos y cantidades. 
# 2. Poder visualizarlos y modificarlos.
#3. Opción de Salir

#DATOS PARA NOMBRE DE VARIABLES:
    #NP = Nombre Producto
    #QP = Cantidad Producto
    #PP = Precio Producto
    #BP = Buscar Producto

lista_productos = []
cantidad_productos = []
precio_productos = []

#1. Menú

while True: 
    print("Control de Inventario - Talento Tech \n1. Agregar productos \n2. Mostrar productos \n3. Salir")
    opcion = input("Seleccione la tarea a realizar")

    if opcion == "1":
        np = input(str("Ingres el nombre del producto: \n")).upper()
        qp = input("Ingrese la cantidad de unidades del producto: \n")
        pp = input("Ingrese el precio unitario del producto en pesos: $\n")
        print("Producto agregado")

        lista_productos.append(np)
        cantidad_productos.append(qp)
        precio_productos.append(pp)   

    elif opcion == "2":
        bp = input(str("Indique el producto a buscar: \n")).upper()
        posicion = lista_productos.index(bp)
        print("------------------------------------------")
        print("Producto: ",lista_productos[posicion])
        print("Cantidad: ", cantidad_productos[posicion])
        print("Precio: $",precio_productos[posicion])
        print("------------------------------------------\n")


    else:
        print("\nSaliendo del programa")
        break