productos = []

def agregar_producto():
  nombre = str(input("Nombre del producto"))
  precio = int(input("Ingrese precio"))
  stock = int(input("Cantidad stock"))

  plantilla = {
    "nombre": nombre,
    "precio": precio,
    "stock": stock,
  }

  productos.append(plantilla)

  print("Producto agregado!")

while True:
  print("========================================")
  print("   SISTEMA MINIMARKET 'LOS ANDES'")
  print("========================================")
  print("1. Agregar")
  print("2. Buscar")
  print("3. Stock crítico")
  print("4. Calcular valor")
  print("5. Ver productos")
  print("6. Salir")
        
  opcion = input("Seleccione una opción")

  if opcion == "1":
    agregar_producto()
  elif opcion == "5":
    print(productos)
  elif opcion == "6":
    break
