# Nombre de la tienda
nombre_tienda = "Tienda TechPro"

# Estructura del inventario: un diccionario que mapea categorías a productos
inventario = {
    "Smartphones": {
        "iPhone 13": (999.99, 20),  # (precio, cantidad)
        "Samsung Galaxy S21": (799.99, 15),
    },
    "Accesorios": {
        "AirPods Pro": (249.99, 50),
        "Cargador Inalámbrico": (39.99, 100),
    },
    "Computadoras": {
        "MacBook Pro 16\"": (2399.99, 10),
        "HP Spectre x360": (1499.99, 8),
    }
}

# Función para agregar un producto a una categoría del inventario
def agregar_producto(categoria, nombre, precio, cantidad):
    if categoria in inventario:
        if nombre in inventario[categoria]:
            print(f"El producto {nombre} ya existe en la categoría {categoria}.")
        else:
            inventario[categoria][nombre] = (precio, cantidad)
            print(f"Producto {nombre} agregado a la categoría {categoria}.")
    else:
        inventario[categoria] = {nombre: (precio, cantidad)}
        print(f"Categoría {categoria} creada y producto {nombre} agregado.")

# Función para consultar los productos de una categoría
def consultar_categoria(categoria):
    if categoria in inventario:
        print(f"\nProductos en la categoría {categoria}:")
        for nombre, (precio, cantidad) in inventario[categoria].items():
            print(f"{nombre}: Precio: ${precio}, Cantidad disponible: {cantidad}")
    else:
        print(f"La categoría {categoria} no existe en el inventario.")

# Función para actualizar el precio de un producto
def actualizar_precio(categoria, nombre, nuevo_precio):
    if categoria in inventario and nombre in inventario[categoria]:
        cantidad = inventario[categoria][nombre][1]
        inventario[categoria][nombre] = (nuevo_precio, cantidad)
        print(f"El precio del producto {nombre} en la categoría {categoria} ha sido actualizado a ${nuevo_precio}.")
    else:
        print(f"El producto {nombre} no se encuentra en la categoría {categoria}.")

# Función para eliminar un producto de una categoría
def eliminar_producto(categoria, nombre):
    if categoria in inventario and nombre in inventario[categoria]:
        del inventario[categoria][nombre]
        print(f"Producto {nombre} eliminado de la categoría {categoria}.")
    else:
        print(f"El producto {nombre} no existe en la categoría {categoria}.")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    total = 0
    for categoria in inventario.values():
        total += sum(map(lambda x: x[0] * x[1], categoria.values()))  # Calcula el valor de cada producto
    print(f"\nValor total del inventario: ${total:.2f}")

# Función para validar los datos numéricos ingresados
def validar_dato(mensaje, tipo_dato):
    while True:
        try:
            dato = tipo_dato(input(mensaje))
            return dato
        except ValueError:
            print(f"Por favor, ingrese un valor válido ({tipo_dato.__name__}).")

# Menú interactivo para el usuario
def menu():
    while True:
        print(f"\n--- Gestión de Inventarios - {nombre_tienda} ---")
        print("1. Añadir producto a categoría")
        print("2. Consultar productos de categoría")
        print("3. Actualizar precio de producto")
        print("4. Eliminar producto de categoría")
        print("5. Calcular valor total del inventario")
        print("6. Salir")
        
        opcion = validar_dato("Elija una opción: ", int)
        
        if opcion == 1:
            categoria = input("Ingrese la categoría del producto (Smartphones, Accesorios, Computadoras): ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = validar_dato("Ingrese el precio del producto: ", float)
            cantidad = validar_dato("Ingrese la cantidad disponible: ", int)
            agregar_producto(categoria, nombre, precio, cantidad)
        
        elif opcion == 2:
            categoria = input("Ingrese la categoría que desea consultar: ")
            consultar_categoria(categoria)
        
        elif opcion == 3:
            categoria = input("Ingrese la categoría del producto a actualizar: ")
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            nuevo_precio = validar_dato("Ingrese el nuevo precio: ", float)
            actualizar_precio(categoria, nombre, nuevo_precio)
        
        elif opcion == 4:
            categoria = input("Ingrese la categoría del producto a eliminar: ")
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(categoria, nombre)
        
        elif opcion == 5:
            calcular_valor_total()
        
        elif opcion == 6:
            print("¡Gracias por usar el sistema de gestión de inventarios!")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    menu()
