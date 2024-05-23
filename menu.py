print("Bienvenido al menú interactivo")
print("Selecciona una opción:")

while True:
    print("\n1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

    opcion = input("Ingresa el número de la opción: ")

    if opcion == "1":
        print("Ejecutando opción 1...")
        # Agrega aquí el código para la opción 1
    elif opcion == "2":
        print("Ejecutando opción 2...")
        # Agrega aquí el código para la opción 2
    elif opcion == "3":
        print("Ejecutando opción 3...")
        # Agrega aquí el código para la opción 3
    elif opcion == "4":
        print("Saliendo del menú...")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción del 1 al 4.")
