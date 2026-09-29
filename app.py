while True:
  print("========================================")
  print("   SISTEMA MINIMARKET 'LOS ANDES'")
  print("========================================")
  print("1. Agregar")
  print("2. Buscar")
  print("3. Stock crítico")
  print("4. Calcular valor")
  print("5. Salir")
        
  opcion = input("Seleccione una opción (1-5): ")

  if opcion == 1:
    agregar_producto()
  elif opcion == 2:
    buscar_producto()
  elif opcion == 3:
    stock_critico()
  elif opcion == 4:
    calcular()
  elif opcion == 5:
    break
