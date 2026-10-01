
inventario = []

def crear_producto():
    nombre = input("Ingrese nombre: ")
    precio = float(input("Ingrese precio: "))
    stock = int(input("Cantidad de stock: "))

    plantilla = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
    }

    inventario.append(plantilla)

def buscar_producto(nombre):
    encontrado = False
    for item in inventario:
        if item["nombre"].lower() == nombre.lower():
            print("Producto encontrado")
            print("-" * 20 + "\n")
            print(f"Nombre {item['nombre']}")
            print(f"Precio S/.{item['precio']}")
            print(f"Stock {item['stock']} und")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró el producto")

    input("\n Presiona cualquier tecla para regresar al menú ")


while True:
    print("MINIMARKET LOS ANDES")
    print("")
    print("1) Crear producto")
    print("2) Ver stock")
    print("3) Buscar producto")
    print("5) Cerrar programa")

    opcion = int(input("\n Ingrese una opcion: "))

    if opcion == 1:
        crear_producto()
    elif opcion == 2:
        if len(inventario) > 0:
            contador = 1
            print("-" * 20 + "\n")
            print(f"Hay ({len(inventario)}) productos en tu inventario")
            print("-" * 20 + "\n")
            for item in inventario:
                print(f"Nombre {item['nombre']} | Precio S/.{item['precio']} | Stock {item['stock']} und")
                contador += 1
        else:
            print("\n ------> No se encontraron productos")
        input("\n Presiona cualquier tecla para regresar al menú ")
    elif opcion == 3:
        nombre = input("Que producto quiere buscar: ")
        buscar_producto(nombre)
    elif opcion == 5:
        break
