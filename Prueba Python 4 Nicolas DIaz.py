def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_stock(stock):
    return stock.isdigit() and int(stock) >= 0 

def validar_precio(precio):
    try:
        return float(precio) >= 0
    except ValueError:
        return False

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar una opción entre 1 y 6.")
        except ValueError:
            print("Debe ingresar un número válido.")

def agregar_producto(lista):
    nombre = input("Ingrese nombre del producto: ")
    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacío ni ser solo espacios en blanco.")
        return

    stock = input("Ingrese el stock del producto: ")
    if not validar_stock(stock):
        print("Error: El stock debe ser un número entero mayor o igual que cero.")
        return

    precio = input("Ingrese el precio del producto: ")
    if not validar_precio(precio):
        print("Error: El precio debe ser un número decimal mayor o igual que cero.")
        return

    elemento = {
        "Nombre": nombre,
        "Stock": int(stock),
        "Precio": float(precio),
        "Disponible": False
    }

    lista.append(elemento)
    print("Producto registrado correctamente.")

def buscar_producto(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["Nombre"] == nombre:
            return i
    return -1

def eliminar_producto(lista): 
    nombre = input("Ingrese el producto a eliminar: ")
    posicion = buscar_producto(lista, nombre)
    if posicion != -1:
        lista.pop(posicion)
        print("Producto eliminado correctamente.")
    else:
        print(f"El producto '{nombre}' no se encuentra registrado.")

def actualizar_disponibilidad(lista):
    for producto in lista:
        producto["Disponible"] = producto["Stock"] >= 1

def mostrar_productos(lista):
    actualizar_disponibilidad(lista)
    if len(lista) == 0:
        print("No existen productos registrados.")
        return

    print("\n=== LISTA DE PRODUCTOS ===")
    for producto in lista:
        print(f"Nombre: {producto['Nombre']}")
        print(f"Stock: {producto['Stock']}")
        print(f"Precio: {producto['Precio']}")
        if producto["Disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN STOCK")
        print("-" * 26)