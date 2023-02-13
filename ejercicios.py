def ejercicio1():
    sueldo = float(input("Ingresa el sueldo del trabajador: "))
    aum = sueldo * 0.15 if sueldo < 4000 else sueldo * 0.08
    sueldo_aumentado = sueldo + aum
    print(f"El sueldo del trabajador es de {sueldo_aumentado}")


def ejercicio2():
    edad = int(input("Ingrese la edad del cliente: "))
    precio_juego = 50

    precio_pagar = precio_juego * 0.75 if edad < 10 else precio_juego
    print(
        f"El cliente {'es un niño y' if edad < 10 else 'no es un niño y'} debe pagar {precio_pagar} soles.")


def ejercicio3():
    mes = input("Ingrese el mes (en minúsculas): ")
    importe = float(input("Ingrese el importe: "))

    descuento = 0.15 if mes == "octubre" else 0
    importe_descuento = importe * (1 - descuento)

    print(f"{'Se aplicó un descuento del 15%.' if descuento > 0 else 'No se aplicó ningún descuento.'} El importe a pagar es:{importe_descuento}")


def ejercicio4():
    num = int(input("Ingrese un número entero menor a 10: "))

    while num >= 10:
        num = int(input("Ingrese un número válido, menor a 10"))

    print("El número ingresado es:", num)


def ejercicio5():
    num = int(input("Ingrese un número entero entre 0 y 20: "))

    while num < 0 or num >= 20:
        num = int(input("Ingrese un número válid, entre 0 y 20: "))

    print("El número ingresado es:", num)


def ejercicio6():
    contador = 0
    num = int(input("Ingrese un número entero entre 0 y 20: "))
    contador += 1

    while num < 0 or num >= 20:
        num = int(input("Ingrese un número válido, entre 0 y 20: "))
        contador += 1

    print("El número es:", num)
    print("Se leyeron", contador, "números.")


def ejercicio7():
    n = int(input("Ingrese un número entero positivo: "))
    suma = sum(range(1, n+1))
    print("La suma de los", n, "primeros números enteros positivos es:", suma)


def ejercicio8():
    suma = 0

    num = int(input("Ingrese un número (0 para terminar): "))

    while num != 0:
        suma += num
        num = int(input("Ingrese otro número (0 para terminar): "))

    print("La suma de los números ingresados es:", suma)


def ejercicio9():
    suma = 0
    while suma <= 100:
        num = float(input("Ingrese un número: "))
        suma += num
    print(f"La suma total es {suma}.")


def ejercicio10():
    nombre = input("Ingrese su nombre: ")
    horas_normales = float(input("Ingrese cantidad de horas trabajadas: "))
    horas_extras = float(
        input("Ingrese cantidad de horas extras trabajadas: "))
    hijos = int(input("Ingrese cantidad de hijos: "))

    pago_hora_normal = 10
    pago_hora_extra = 1.5 * pago_hora_normal
    monto_horas_normales = horas_normales * pago_hora_normal
    monto_horas_extras = horas_extras * pago_hora_extra
    bonificacion_hijos = hijos * 0.5

    pago_total = monto_horas_normales + monto_horas_extras + bonificacion_hijos

    print("Nombre:", nombre)
    print("Monto por horas normales:", monto_horas_normales)
    print("Monto por horas extras:", monto_horas_extras)
    print("Bonificación por hijos:", bonificacion_hijos)
    print("Pago total:", pago_total)


while True:
    print("Elija una opción:")
    print("1. Evaluar el aumento del sueldo")
    print("2. Calcular el precio en el parque de diversiones")
    print("3. Calcular el precio con descuento en la tienda")
    print("4. Número menor que 10")
    print("5. Número entre 0 y 20")
    print("6. Número entre 0 y 20 con un contador")
    print("7. Suma de los primeros números 'n' positivos")
    print("8. Suma de los números hasta ingresar '0'")
    print("9. Suma superior a 100")
    print("10. Pago de trabajador")
    print("Escriba 'exit' para salir del programa.")

    opcion = input("Opción seleccionada: ")

    if opcion == "exit":
        break

    opcion = int(opcion)

    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio3()
    elif opcion == 4:
        ejercicio4()
    elif opcion == 5:
        ejercicio5()
    elif opcion == 6:
        ejercicio6()
    elif opcion == 7:
        ejercicio7()
    elif opcion == 8:
        ejercicio8()
    elif opcion == 9:
        ejercicio9()
    elif opcion == 10:
        ejercicio10()
    else:
        print("Elija una opción entre 1 y 10 o escriba 'exit' para salir del programa.")
