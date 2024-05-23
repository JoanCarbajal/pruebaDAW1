def calculadora():
    print("Bienvenido a la Calculadora")
    print("Selecciona la operación que deseas realizar:")

    while True:
        print("\n1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Ingresa el número de la operación (1-5): ")

        if opcion == "1":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = num1 + num2
            print(f"El resultado de {num1} + {num2} es: {resultado}")
        elif opcion == "2":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = num1 - num2
            print(f"El resultado de {num1} - {num2} es: {resultado}")
        elif opcion == "3":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = num1 * num2
            print(f"El resultado de {num1} * {num2} es: {resultado}")
        elif opcion == "4":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            if num2 == 0:
                print("Error: No se puede dividir entre 0")
            else:
                resultado = num1 / num2
                print(f"El resultado de {num1} / {num2} es: {resultado}")
        elif opcion == "5":
            print("Saliendo de la Calculadora...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción del 1 al 5.")

calculadora()
