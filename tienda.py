#---------------------------------
#Tienda de tecnologia: "TechPro"
#Autor("Maria Fernanda Reid")
#------------------------------

#variables 
precio_dolares=int()

#Producto, precio y cantidad disponible 
inventario={'''
            1. Smartphones
            2. Accesorios
            3. Computadoras 
            '''}

Smarphones={
     "iPhone_14":( 500,20),
     "iPhone_13":(450,15),
     "iPhone_12":(300,10),
     "iPhone_11":(240,15)
            }

Accesorios={
     "AirPods Pro":(50,20),
     "Cargador Inalámbrico":(10,50)
     }

Computadoras={
     "MacBook Pro 16 ":(600,5)
     }

#funcion para entrada numericas 
def validar_dato(mensaje, tipo_dato):
     while True:
          try:
               dato=tipo_dato(input(mensaje))
               return dato
          except ValueError:
               print(f"Por favor, ingresa un valor valido ({tipo_dato})")

def agregar_producto(categorias, nombre, precio, cantidad):
     if categorias in inventario:
        if nombre in inventario[categorias]:
            print(f"El producto {nombre} ya existe en la categoría {categorias}.")
        else:
            inventario[categorias][nombre] = (precio, cantidad)
            print(f"Producto {nombre} agregado a la categoría {categorias}.")
     else:
            inventario[categorias] = {nombre: (precio, cantidad)}
            print(f"Categoría {categorias} creada y producto {nombre} agregado.")
'''
def consultar_producto(nombre):
     if categoria in inventario and nombre in inventario[categorias]:
        cantidad = inventario[categorias][nombre][1]
        inventario[categoria][nombre] = (nuevo_precio, cantidad)
        print(f"El precio del producto {nombre} en la categoría {categorias} ha sido actualizado a ${nuevo_precio}.")
     else:
        print(f"El producto {nombre} no se encuentra en la categoría {categorias}.")

def actualizar_categeria(categorias, nombre, nuevo_precio): 

def eliminar_producto(nombre):
    if categorias in inventario and nombre in inventario[categorias]:
        del inventario[categorias][nombre]
        print(f"Producto {nombre} eliminado de la categoría {categorias}.")
    else:
        print(f"El producto {nombre} no existe en la categoría {categoria}.")
    
def calcular_valor_total():'''
    

#funcion gestion de inventario 
    print("\n---Gestion de inventario -tienda tecnologica TechPro---")
def menu():
    print ('''
            1. Añadir producto a categoría
            2. Consultar productos de categoría
            3. Actualizar precio de producto
            4. Eliminar producto de categoría
            5. Calcular valor total del inventario
            6. Salir
            ''')
    
    if seleccion == 1:
                categoria = input("Ingrese la categoría del producto (Smartphones, Accesorios, Computadoras): ")
                nombre = input("Ingrese el nombre del producto: ")
                precio_dolares = validar_dato("Ingrese el precio del producto: ", float)
                cantidad    = validar_dato("Ingrese la cantidad disponible: ", int)
                agregar_producto(categoria, nombre, precio_dolares, cantidad)
                
    elif seleccion == 2:
                categoria = input("Ingrese la categoría que desea consultar: ")
                consultar_categoria(categoria)
                
    elif seleccion == 3:
                categoria = input("Ingrese la categoría del producto a actualizar: ")
                nombre = input("Ingrese el nombre del producto a actualizar: ")
                nuevo_precio = validar_dato("Ingrese el nuevo precio: ", float)
                actualizar_precio(categoria, nombre, nuevo_precio)
                
    elif seleccion == 4:
           categoria = input("Ingrese la categoría del producto a eliminar: ")
           nombre = input("Ingrese el nombre del producto a eliminar: ")
           eliminar_producto(categoria, nombre)
                
    elif seleccion == 5:
            calcular_valor_total()
                
    elif seleccion == 6:
            print("¡Gracias por usar el sistema de gestión de inventarios!")
            exit()
    else:
             print("Opción no válida, por favor intente de nuevo.")

menu()

while True:
    try:
        seleccion=int(input("INGRESE EL NUMERO DE LA FUNCION QUE DESEA HACER: "))
        if  seleccion<1 or seleccion>6:
            print("ERROR, por favor ingrese un numero entre 1 Y 6 ")




print('''SELECCIONE SU CATEGORIA:
                        1. Smartphones
                        2. Accesorios
                        3. Computadoras ''')
while True:
    try:
        categorias =int(input("ELIGE LA CATEGORIA?: "))
        if categorias<1 or categorias>3:
            print("ERROR, por favor ingrese un numero entre 1 y 3")
        match categorias:
            case 1: 
                print(Smarphones)
                break
            case 2:
                print(Accesorios)
                break
            case 3:
                print(Computadoras)
                break
    except ValueError:
        print("Por favor, ingrese un numero entero ")



#funciones 
  
