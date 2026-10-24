
# -*- coding: utf-8 -*-
# ==========================================================
# +CLASSNOTE+
# Calculadora creativa creada por Ángel
# Colores: turquesa brillante, azul y negro
# ==========================================================

import ast
import operator
import math

from kivy.app import App
from kivy.metrics import dp, sp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


# ------------------ COLORES ------------------

NEGRO = (0.025, 0.035, 0.065, 1)
AZUL_OSCURO = (0.035, 0.10, 0.22, 1)
AZUL = (0.02, 0.28, 0.95, 1)
TURQUESA = (0.0, 0.85, 0.85, 1)
BLANCO = (0.95, 0.98, 1, 1)
GRIS = (0.12, 0.17, 0.24, 1)


# ------------------ APLICACIÓN ------------------

class ClassNoteApp(App):

    def build(self):
        self.title = "+CLASSNOTE+"
        Window.clearcolor = NEGRO

        self.historial = []

        principal = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(8)
        )

        # Encabezado
        encabezado = Label(
            text="[b][color=00E5E5]+CLASSNOTE+[/color][/b]",
            markup=True,
            font_size=sp(29),
            size_hint_y=None,
            height=dp(48)
        )
        principal.add_widget(encabezado)

        subtitulo = Label(
            text="¡Adelante! Tu creatividad también calcula.",
            color=TURQUESA,
            font_size=sp(13),
            size_hint_y=None,
            height=dp(25)
        )
        principal.add_widget(subtitulo)

        creador = Label(
            text="Creada con dedicación por Ángel",
            color=BLANCO,
            font_size=sp(12),
            size_hint_y=None,
            height=dp(22)
        )
        principal.add_widget(creador)

        # Pantalla de cálculo
        self.pantalla = TextInput(
            text="",
            hint_text="Escribe una operación...",
            multiline=False,
            halign="right",
            font_size=sp(28),
            foreground_color=BLANCO,
            background_color=AZUL_OSCURO,
            cursor_color=TURQUESA,
            hint_text_color=(0.55, 0.68, 0.8, 1),
            size_hint_y=None,
            height=dp(70),
            padding=[dp(12), dp(18)]
        )
        principal.add_widget(self.pantalla)

        self.mensaje = Label(
            text="¡Hola! Hagamos algo increíble.",
            color=TURQUESA,
            font_size=sp(13),
            size_hint_y=None,
            height=dp(28)
        )
        principal.add_widget(self.mensaje)

        # Teclado principal
        teclado = GridLayout(
            cols=4,
            spacing=dp(6),
            size_hint_y=0.95
        )

        botones = [
            ("C", self.limpiar, TURQUESA),
            ("⌫", self.borrar, AZUL),
            ("(", lambda b: self.agregar("("), GRIS),
            (")", lambda b: self.agregar(")"), GRIS),

            ("7", lambda b: self.agregar("7"), AZUL_OSCURO),
            ("8", lambda b: self.agregar("8"), AZUL_OSCURO),
            ("9", lambda b: self.agregar("9"), AZUL_OSCURO),
            ("÷", lambda b: self.agregar("/"), TURQUESA),

            ("4", lambda b: self.agregar("4"), AZUL_OSCURO),
            ("5", lambda b: self.agregar("5"), AZUL_OSCURO),
            ("6", lambda b: self.agregar("6"), AZUL_OSCURO),
            ("×", lambda b: self.agregar("*"), TURQUESA),

            ("1", lambda b: self.agregar("1"), AZUL_OSCURO),
            ("2", lambda b: self.agregar("2"), AZUL_OSCURO),
            ("3", lambda b: self.agregar("3"), AZUL_OSCURO),
            ("−", lambda b: self.agregar("-"), TURQUESA),

            ("0", lambda b: self.agregar("0"), AZUL_OSCURO),
            (".", lambda b: self.agregar("."), AZUL_OSCURO),
            ("%", self.abrir_porcentaje, GRIS),
            ("+", lambda b: self.agregar("+"), TURQUESA),

            ("xʸ", lambda b: self.agregar("**"), GRIS),
            ("√x", self.abrir_raiz, GRIS),
            ("//", lambda b: self.agregar("//"), GRIS),
            ("=", self.calcular, AZUL),
        ]

        for texto, accion, color in botones:
            boton = Button(
                text=texto,
                font_size=sp(21),
                bold=True,
                color=NEGRO if color == TURQUESA else BLANCO,
                background_normal="",
                background_color=color
            )
            boton.bind(on_release=accion)
            teclado.add_widget(boton)

        principal.add_widget(teclado)

        # Sección de funciones avanzadas
        etiqueta = Label(
            text="[b][color=00E5E5]FUNCIONES AVANZADAS[/color][/b]",
            markup=True,
            font_size=sp(15),
            size_hint_y=None,
            height=dp(30)
        )
        principal.add_widget(etiqueta)

        avanzadas = GridLayout(
            cols=3,
            spacing=dp(6),
            size_hint_y=None,
            height=dp(112)
        )

        funciones = [
            ("Fracciones", self.abrir_fracciones),
            ("Promedios", self.abrir_promedio),
            ("Ecuaciones", self.abrir_ecuacion),
            ("Potencias", lambda b: self.agregar("**")),
            ("Porcentajes", self.abrir_porcentaje),
            ("Lógica", self.abrir_logica),
        ]

        for texto, accion in funciones:
            boton = Button(
                text=texto,
                font_size=sp(13),
                background_normal="",
                background_color=AZUL_OSCURO,
                color=TURQUESA
            )
            boton.bind(on_release=accion)
            avanzadas.add_widget(boton)

        principal.add_widget(avanzadas)

        pie = Label(
            text="Ángel • Aprende, crea y alcanza tus metas.",
            color=BLANCO,
            font_size=sp(11),
            size_hint_y=None,
            height=dp(23)
        )
        principal.add_widget(pie)

        return principal

    # ------------------ OPERACIONES BÁSICAS ------------------

    def agregar(self, valor):
        self.pantalla.text += valor

    def limpiar(self, boton):
        self.pantalla.text = ""
        self.mensaje.text = "Pantalla limpia. ¡Adelante!"

    def borrar(self, boton):
        self.pantalla.text = self.pantalla.text[:-1]

    def evaluar(self, expresion):
        """Evalúa operaciones matemáticas permitidas."""

        operadores = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.FloorDiv: operator.floordiv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,
            ast.UAdd: operator.pos,
            ast.USub: operator.neg,
        }

        def revisar(nodo):
            if isinstance(nodo, ast.Expression):
                return revisar(nodo.body)

            if isinstance(nodo, ast.Constant):
                if type(nodo.value) in (int, float):
                    return nodo.value
                raise ValueError("Dato no permitido.")

            if isinstance(nodo, ast.BinOp):
                tipo = type(nodo.op)

                if tipo not in operadores:
                    raise ValueError("Operación no permitida.")

                izquierda = revisar(nodo.left)
                derecha = revisar(nodo.right)

                if tipo in (ast.Div, ast.FloorDiv, ast.Mod):
                    if derecha == 0:
                        raise ZeroDivisionError(
                            "No se puede dividir entre cero."
                        )

                if tipo == ast.Pow and abs(derecha) > 1000:
                    raise ValueError("El exponente es demasiado grande.")

                resultado = operadores[tipo](izquierda, derecha)

                if isinstance(resultado, complex):
                    raise ValueError("El resultado no es un número real.")

                if isinstance(resultado, float) and not math.isfinite(resultado):
                    raise ValueError("El resultado es demasiado grande.")

                return resultado

            if isinstance(nodo, ast.UnaryOp):
                tipo = type(nodo.op)

                if tipo not in operadores:
                    raise ValueError("Operación no permitida.")

                return operadores[tipo](revisar(nodo.operand))

            raise ValueError("La expresión contiene elementos no permitidos.")

        arbol = ast.parse(expresion, mode="eval")
        return revisar(arbol)

    def calcular(self, boton):
        expresion = self.pantalla.text.strip()

        if not expresion:
            self.mensaje.text = "Primero escribe una operación."
            return

        try:
            resultado = self.evaluar(expresion)

            self.historial.append((expresion, resultado))
            self.pantalla.text = str(resultado)
            self.mensaje.text = "¡Excelente! Operación realizada."

        except ZeroDivisionError:
            self.mensaje.text = "No podemos dividir entre cero."

        except (ValueError, SyntaxError, OverflowError):
            self.mensaje.text = "Revisa la operación e inténtalo otra vez."

        except Exception:
            self.mensaje.text = "No se pudo realizar el cálculo."

    # ------------------ VENTANAS AUXILIARES ------------------

    def abrir_formulario(self, titulo, campos, accion):
        contenido = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        entradas = []

        for etiqueta in campos:
            contenido.add_widget(
                Label(
                    text=etiqueta,
                    color=TURQUESA,
                    size_hint_y=None,
                    height=dp(25)
                )
            )

            entrada = TextInput(
                multiline=False,
                input_filter="float",
                font_size=sp(18),
                size_hint_y=None,
                height=dp(43)
            )

            entradas.append(entrada)
            contenido.add_widget(entrada)

        fila = BoxLayout(
            size_hint_y=None,
            height=dp(45),
            spacing=dp(8)
        )

        popup = Popup(
            title=titulo,
            content=contenido,
            size_hint=(0.92, 0.85),
            background_color=AZUL_OSCURO,
            title_color=TURQUESA
        )

        aceptar = Button(
            text="Calcular",
            background_normal="",
            background_color=TURQUESA,
            color=NEGRO
        )

        cerrar = Button(
            text="Cerrar",
            background_normal="",
            background_color=AZUL,
            color=BLANCO
        )

        def ejecutar(boton):
            try:
                valores = [float(e.text) for e in entradas]
                accion(valores)
                popup.dismiss()

            except (ValueError, ZeroDivisionError, OverflowError) as error:
                self.mensaje.text = f"Revisa los datos: {error}"

            except Exception:
                self.mensaje.text = "No fue posible realizar la operación."

        aceptar.bind(on_release=ejecutar)
        cerrar.bind(on_release=lambda b: popup.dismiss())

        fila.add_widget(aceptar)
        fila.add_widget(cerrar)
        contenido.add_widget(fila)

        popup.open()

    # ------------------ PORCENTAJES ------------------

    def abrir_porcentaje(self, boton):
        def operar(valores):
            cantidad, porcentaje = valores
            resultado = cantidad * porcentaje / 100
            self.pantalla.text = str(resultado)
            self.mensaje.text = (
                f"El {porcentaje}% de {cantidad} es {resultado}."
            )

        self.abrir_formulario(
            "Calcular porcentaje",
            ["Cantidad:", "Porcentaje:"],
            operar
        )

    # ------------------ RAÍZ CUADRADA ------------------

    def abrir_raiz(self, boton):
        def operar(valores):
            numero = valores[0]

            if numero < 0:
                raise ValueError("El número debe ser positivo o cero.")

            resultado = math.sqrt(numero)
            self.pantalla.text = str(resultado)
            self.mensaje.text = "¡Raíz cuadrada calculada!"

        self.abrir_formulario(
            "Raíz cuadrada",
            ["Número:"],
            operar
        )

    # ------------------ FRACCIONES ------------------

    def abrir_fracciones(self, boton):
        def operar(valores):
            a, b, c, d = valores

            if not all(v.is_integer() for v in (a, b, c, d)):
                raise ValueError("Usa números enteros en las fracciones.")

            a, b, c, d = int(a), int(b), int(c), int(d)

            if b == 0 or d == 0:
                raise ValueError("Los denominadores no pueden ser cero.")

            primera = a / b
            segunda = c / d
            resultado = primera + segunda

            self.pantalla.text = str(resultado)
            self.mensaje.text = (
                f"{a}/{b} + {c}/{d} = {resultado}"
            )

        self.abrir_formulario(
            "Suma de fracciones",
            [
                "Primer numerador:",
                "Primer denominador:",
                "Segundo numerador:",
                "Segundo denominador:"
            ],
            operar
        )

    # ------------------ PROMEDIOS ------------------

    def abrir_promedio(self, boton):
        contenido = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        contenido.add_widget(
            Label(
                text="Escribe los números separados por comas.",
                color=TURQUESA
            )
        )

        entrada = TextInput(
            hint_text="Ejemplo: 3.5, 4.0, 4.5",
            multiline=False,
            size_hint_y=None,
            height=dp(45)
        )

        contenido.add_widget(entrada)

        popup = Popup(
            title="Calcular promedio",
            content=contenido,
            size_hint=(0.9, 0.42)
        )

        boton_calcular = Button(
            text="Calcular promedio",
            size_hint_y=None,
            height=dp(45),
            background_normal="",
            background_color=TURQUESA,
            color=NEGRO
        )

        def calcular_promedio(boton):
            try:
                numeros = [
                    float(x.strip())
                    for x in entrada.text.split(",")
                    if x.strip()
                ]

                if not numeros:
                    raise ValueError("Escribe al menos un número.")

                promedio = sum(numeros) / len(numeros)
                self.pantalla.text = str(promedio)
                self.mensaje.text = f"Tu promedio es {promedio}."
                popup.dismiss()

            except ValueError:
                self.mensaje.text = "Escribe números separados por comas."

        boton_calcular.bind(on_release=calcular_promedio)
        contenido.add_widget(boton_calcular)
        popup.open()

    # ------------------ ECUACIONES ------------------

    def abrir_ecuacion(self, boton):
        def operar(valores):
            a, b, c = valores

            if a == 0:
                if b == c:
                    self.mensaje.text = "La ecuación tiene infinitas soluciones."
                else:
                    self.mensaje.text = "La ecuación no tiene solución."
                return

            x = (c - b) / a
            self.pantalla.text = str(x)
            self.mensaje.text = f"Solución de ax + b = c: x = {x}"

        self.abrir_formulario(
            "Resolver ax + b = c",
            ["Valor de a:", "Valor de b:", "Valor de c:"],
            operar
        )

    # ------------------ LÓGICA ------------------

    def abrir_logica(self, boton):
        contenido = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        contenido.add_widget(
            Label(
                text="Selecciona verdadero o falso.",
                color=TURQUESA
            )
        )

        entradas = []

        for texto in ("Primera condición", "Segunda condición"):
            contenido.add_widget(
                Label(text=texto, color=BLANCO)
            )

            entrada = TextInput(
                text="verdadero",
                multiline=False,
                size_hint_y=None,
                height=dp(40)
            )

            entradas.append(entrada)
            contenido.add_widget(entrada)

        popup = Popup(
            title="Lógica: AND, OR y NOT",
            content=contenido,
            size_hint=(0.9, 0.65)
        )

        def comprobar(boton):
            respuestas = [
                e.text.strip().lower() for e in entradas
            ]

            verdaderos = ("verdadero", "v", "sí", "si", "true")
            falsos = ("falso", "f", "no", "false")

            if any(
                r not in verdaderos + falsos
                for r in respuestas
            ):
                self.mensaje.text = (
                    "Escribe verdadero o falso en ambas condiciones."
                )
                return

            a = respuestas[0] in verdaderos
            b = respuestas[1] in verdaderos

            resultado = (
                f"AND: {a and b} | OR: {a or b} | NOT A: {not a}"
            )

            self.pantalla.text = ""
            self.mensaje.text = resultado
            popup.dismiss()

        boton = Button(
            text="Evaluar condiciones",
            size_hint_y=None,
            height=dp(45),
            background_normal="",
            background_color=TURQUESA,
            color=NEGRO
        )

        boton.bind(on_release=comprobar)
        contenido.add_widget(boton)
        popup.open()


# ------------------ INICIO ------------------

if __name__ == "__main__":
    ClassNoteApp().run()
