
# =====================================================
# +CLASSNOTE+
# Calculadora creada por Ángel
# ¡Matemáticas fáciles para todos!
# =====================================================

from fractions import Fraction
from math import sqrt

nombre_app = "+CLASSNOTE+"
nombre_creador = "Ángel"

print("=" * 45)
print("        ¡ADELANTE A +CLASSNOTE+!")
print("=" * 45)
print("Una calculadora creada con cariño por", nombre_creador)
print("Aquí podrás realizar diferentes operaciones matemáticas.")
print()

nombre_usuario = input("¿Cómo te llamas, querido/a usuario/a? ")

print()
print(f"¡Hola, {nombre_usuario}! Me alegra tenerte por aquí.")
print("¡Adelante! Vamos a hacer matemáticas juntos.")
print()


# =====================================================
# FUNCIÓN PARA PEDIR NÚMEROS
# =====================================================

def pedir_numero(mensaje):
    while True:
        try:
            numero = float(
                input(
                    f"Querido/a {nombre_usuario}, "
                    f"si amablemente digitas el número, "
                    f"por favor, {mensaje}"
                )
            )
            return numero

        except ValueError:
            print("Ups, ese dato no parece un número válido.")
            print("Inténtalo nuevamente, por favor.")


# =====================================================
# FUNCIÓN PARA PEDIR NÚMEROS ENTEROS
# =====================================================

def pedir_entero(mensaje):
    while True:
        try:
            numero = int(
                input(
                    f"Querido/a {nombre_usuario}, "
                    f"si amablemente digitas el número entero, "
                    f"por favor, {mensaje}"
                )
            )
            return numero

        except ValueError:
            print("Por favor, escribe un número entero válido.")


# =====================================================
# FUNCIÓN PARA MOSTRAR LOS RESULTADOS
# =====================================================

def mostrar_resultado(operacion, resultado):
    print()
    print("-" * 45)
    print("Operación:", operacion)
    print("Resultado:", resultado)
    print("-" * 45)
    print()


# =====================================================
# MENÚ PRINCIPAL
# =====================================================

def mostrar_menu():
    print()
    print("========= +CLASSNOTE+ =========")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. División entera")
    print("6. Módulo o residuo (%)")
    print("7. Operaciones con fracciones")
    print("8. Porcentajes")
    print("9. Promedios")
    print("10. Ecuaciones básicas")
    print("11. Potenciación")
    print("12. Radicación")
    print("13. Operaciones lógicas")
    print("14. Información de la aplicación")
    print("0. Salir")
    print("=" * 31)


# =====================================================
# PROGRAMA PRINCIPAL
# =====================================================

def classnote():

    continuar = True

    while continuar:

        mostrar_menu()

        opcion = pedir_entero(
            "elige el número de la operación que deseas realizar: "
        )

        # ---------------- SUMA ----------------

        if opcion == 1:

            numero1 = pedir_numero("digita el primer número: ")
            numero2 = pedir_numero("digita el segundo número: ")

            suma = numero1 + numero2

            mostrar_resultado("Suma", suma)

        # ---------------- RESTA ----------------

        elif opcion == 2:

            numero1 = pedir_numero("digita el primer número: ")
            numero2 = pedir_numero("digita el segundo número: ")

            resta = numero1 - numero2

            mostrar_resultado("Resta", resta)

        # ---------------- MULTIPLICACIÓN ----------------

        elif opcion == 3:

            numero1 = pedir_numero("digita el primer número: ")
            numero2 = pedir_numero("digita el segundo número: ")

            multiplicacion = numero1 * numero2

            mostrar_resultado("Multiplicación", multiplicacion)

        # ---------------- DIVISIÓN ----------------

        elif opcion == 4:

            numero1 = pedir_numero("digita el dividendo: ")
            numero2 = pedir_numero("digita el divisor: ")

            if numero2 != 0:

                division = numero1 / numero2

                mostrar_resultado("División", division)

            else:
                print("No podemos dividir entre cero.")

        # ---------------- DIVISIÓN ENTERA ----------------

        elif opcion == 5:

            numero1 = pedir_numero("digita el dividendo: ")
            numero2 = pedir_numero("digita el divisor: ")

            if numero2 != 0:

                division_entera = numero1 // numero2

                mostrar_resultado(
                    "División entera",
                    division_entera
                )

            else:
                print("No podemos dividir entre cero.")

        # ---------------- MÓDULO ----------------

        elif opcion == 6:

            numero1 = pedir_numero("digita el primer número: ")
            numero2 = pedir_numero("digita el segundo número: ")

            if numero2 != 0:

                modulo = numero1 % numero2

                mostrar_resultado("Módulo o residuo", modulo)

            else:
                print("No podemos calcular el módulo con divisor cero.")

        # ---------------- FRACCIONES ----------------

        elif opcion == 7:

            print()
            print("¡Vamos a trabajar con fracciones!")

            numerador1 = pedir_entero("digita el primer numerador: ")
            denominador1 = pedir_entero("digita el primer denominador: ")

            numerador2 = pedir_entero("digita el segundo numerador: ")
            denominador2 = pedir_entero("digita el segundo denominador: ")

            if denominador1 != 0 and denominador2 != 0:

                fraccion1 = Fraction(numerador1, denominador1)
                fraccion2 = Fraction(numerador2, denominador2)

                print()
                print("1. Sumar las fracciones")
                print("2. Restar las fracciones")
                print("3. Multiplicar las fracciones")
                print("4. Dividir las fracciones")

                tipo_fraccion = pedir_entero(
                    "elige la operación que deseas realizar: "
                )

                if tipo_fraccion == 1:

                    resultado = fraccion1 + fraccion2

                elif tipo_fraccion == 2:

                    resultado = fraccion1 - fraccion2

                elif tipo_fraccion == 3:

                    resultado = fraccion1 * fraccion2

                elif tipo_fraccion == 4:

                    if fraccion2 != 0:

                        resultado = fraccion1 / fraccion2

                    else:
                        print("No puedes dividir entre una fracción igual a cero.")
                        continue

                else:
                    print("Esa opción no existe.")
                    continue

                print("Primera fracción:", fraccion1)
                print("Segunda fracción:", fraccion2)
                print("Resultado exacto:", resultado)
                print("Resultado decimal:", float(resultado))

            else:
                print("Los denominadores no pueden ser cero.")

        # ---------------- PORCENTAJES ----------------

        elif opcion == 8:

            cantidad = pedir_numero(
                "digita la cantidad a la que deseas calcularle el porcentaje: "
            )

            porcentaje = pedir_numero(
                "digita el porcentaje que deseas calcular: "
            )

            resultado_porcentaje = cantidad * porcentaje / 100

            mostrar_resultado(
                f"{porcentaje}% de {cantidad}",
                resultado_porcentaje
            )

        # ---------------- PROMEDIOS ----------------

        elif opcion == 9:

            while True:

                cantidad_notas = pedir_entero(
                    "¿cuántos números deseas promediar?: "
                )

                if cantidad_notas > 0:
                    break

                else:
                    print("Debes ingresar al menos un número.")

            suma_notas = 0

            for i in range(cantidad_notas):

                nota = pedir_numero(
                    f"digita el número {i + 1}: "
                )

                suma_notas = suma_notas + nota

            promedio = suma_notas / cantidad_notas

            mostrar_resultado("Promedio", promedio)

        # ---------------- ECUACIONES BÁSICAS ----------------

        elif opcion == 10:

            print()
            print("Resolveremos una ecuación de la forma:")
            print("ax + b = c")
            print()

            a = pedir_numero("digita el valor de a: ")
            b = pedir_numero("digita el valor de b: ")
            c = pedir_numero("digita el valor de c: ")

            if a != 0:

                x = (c - b) / a

                mostrar_resultado("Solución de la ecuación: x", x)

            elif b == c:

                print("La ecuación tiene infinitas soluciones.")

            else:

                print("La ecuación no tiene solución.")

        # ---------------- POTENCIACIÓN ----------------

        elif opcion == 11:

            base = pedir_numero("digita la base de la potencia: ")
            exponente = pedir_numero("digita el exponente: ")

            if base == 0 and exponente < 0:

                print("Cero no puede tener un exponente negativo.")

            else:

                potencia = base ** exponente

                mostrar_resultado("Potenciación", potencia)

        # ---------------- RADICACIÓN ----------------

        elif opcion == 12:

            numero = pedir_numero(
                "digita el número al que deseas calcularle la raíz cuadrada: "
            )

            if numero >= 0:

                raiz = sqrt(numero)

                mostrar_resultado("Raíz cuadrada", raiz)

            else:

                print(
                    "La raíz cuadrada real de un número negativo "
                    "no está definida."
                )

        # ---------------- OPERACIONES LÓGICAS ----------------

        elif opcion == 13:

            print()
            print("========= ZONA DE LÓGICA =========")

            variable = pedir_numero("digita el valor de tu variable: ")
            limite = pedir_numero("digita el valor del límite: ")

            condicion_not = not (variable > limite)

            condicion_or = (
                variable > limite
            ) or (
                variable == limite
            )

            condicion_and = (
                variable >= 0
            ) and (
                variable <= limite
            )

            print()
            print("Resultados de las condiciones:")
            print("not (variable > límite):", condicion_not)
            print("(variable > límite) or (variable == límite):", condicion_or)
            print("(variable >= 0) and (variable <= límite):", condicion_and)

            print()
            print("Ahora puedes probar tus propias condiciones.")

            condicion1 = input(
                "¿La primera condición es verdadera? (sí/no): "
            ).strip().lower()

            condicion2 = input(
                "¿La segunda condición es verdadera? (sí/no): "
            ).strip().lower()

            respuestas_validas = ("si", "sí", "no")

            if (
                condicion1 not in respuestas_validas
                or condicion2 not in respuestas_validas
            ):

                print("Por favor, responde únicamente sí o no.")

            else:

                valor1 = condicion1 in ("si", "sí")
                valor2 = condicion2 in ("si", "sí")

                print("not de la primera condición:", not valor1)
                print("Primera condición OR segunda:", valor1 or valor2)
                print("Primera condición AND segunda:", valor1 and valor2)

        # ---------------- INFORMACIÓN ----------------

        elif opcion == 14:

            print()
            print("========= SOBRE CLASSNOTE =========")
            print("Nombre de la aplicación:", nombre_app)
            print("Creador:", nombre_creador)
            print("Versión: 1.0")
            print("Una calculadora para aprender y practicar.")
            print("¡Gracias por utilizar mi aplicación!")

        # ---------------- SALIR ----------------

        elif opcion == 0:

            continuar = False

            print()
            print(f"¡Hasta pronto, {nombre_usuario}!")
            print("Gracias por utilizar +CLASSNOTE+.")
            print("¡Sigue aprendiendo y alcanzando tus metas!")
            print("Con cariño, Ángel.")

        # ---------------- OPCIÓN INCORRECTA ----------------

        else:

            print(
                "Esa opción no existe. "
                "Por favor, elige una opción del menú."
            )


# =====================================================
# INICIO DE LA APLICACIÓN
# =====================================================

if __name__ == "__main__":

    classnote()
