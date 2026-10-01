
inventario = [
    
]

def crear_producto():
    print("\n" * 40 + "=" * 40 + "")
    print("     ➕ CREANDO PRODUCTO NUEVO")
    print("=" * 40 + "\n")
    nombre = input("---> Ingrese nombre: ")
    precio = float(input("---> Ingrese precio: "))
    stock = int(input("---> Cantidad de stock: "))

    plantilla = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
    }

    inventario.append(plantilla)

    print("\n" * 40 + "=" * 40 + "")
    print("     ✅ PRODUCTO AÑADIDO AL INVENTARIO")
    print("=" * 40 + "\n")
    print(f"Nombre: {plantilla['nombre']} | Precio S/.{plantilla['precio']} | Stock: {plantilla['stock']} und")
    input("\n---> Presiona cualquier tecla para regresar al menú ")

def stock():
    if len(inventario) > 0:
        contador = 1
        print("\n" * 40 + "=" * 40 + "")
        print(f"     Hay ({len(inventario)}) productos en tu inventario")
        print("=" * 40 + "\n")
        for item in inventario:
            print(f"Nombre: {item['nombre']} | Precio S/.{item['precio']} | Stock: {item['stock']} und")
            contador += 1
    else:
        print("\n" * 40 + "=" * 40 + "")
        print("     ❌ NO HAY INVENTARIO")
        print("=" * 40 + "\n")
    input("\n---> Presiona cualquier tecla para regresar al menú ")

def buscar_producto(nombre):
    encontrado = False
    for item in inventario:
        if item["nombre"].lower() == nombre.lower():
            print("\n" * 40 + "=" * 40 + "")
            print("     ✅ PRODUCTO ENCONTRADO")
            print("=" * 40 + "\n")
            print(f"Nombre: {item['nombre']} | Precio S/.{item['precio']} | Stock: {item['stock']} und")
            encontrado = True
            break

    if not encontrado:
        print("\n" * 40 + "=" * 40 + "")
        print("     ❌ PRODUCTO NO ENCONTRADO")
        print("=" * 40 + "")

    input("\n---> Presiona cualquier tecla para regresar al menú ")

def stock_critico():
    if len(inventario) > 0:
        for item in inventario:
            critico = []
            if item["stock"] < 5:
                critico.append(item)
            else:
                print("\n" * 40 + "=" * 40 + "")
                print("     ❌ NO HAY PRODUCTOS CRITICOS")
                print("=" * 40 + "")
    else:
        print("\n" * 40 + "=" * 40 + "")
        print("     ❌ NO HAY INVENTARIO")
        print("=" * 40 + "")

while True:
    print("\n" * 40 + "=" * 40 + "")
    print("     🛒 MINIMARKET LOS ANDES")
    print("=" * 40 + "\n")
    print("1) Crear producto")
    print("2) Ver stock")
    print("3) Buscar producto")
    print("4) Stock critico")
    print("5) Valor total")
    print("5) Cerrar programa")

    opcion = int(input("\n---> Ingrese una opcion: "))

    if opcion == 1:
        crear_producto()
    elif opcion == 2:
        stock()
    elif opcion == 3:
        nombre = input("---> Ingrese nombre del producto a buscar: ")
        buscar_producto(nombre)
    elif opcion == 4:
        stock_critico()
    elif opcion == 5:
        valor_total()
    elif opcion == 5:
        break
