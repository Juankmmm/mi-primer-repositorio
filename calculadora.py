import customtkinter as ctk


# ==========================================
# CLASE CALCULADORA
# ==========================================

class Calculadora:

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")

        return a / b

    def calcular(self, expresion):
        operadores = ["+", "-", "*", "/"]

        for operador in operadores:
            if operador in expresion:

                partes = expresion.split(operador)

                if len(partes) != 2:
                    raise ValueError("Operación no válida")

                a = float(partes[0])
                b = float(partes[1])

                if operador == "+":
                    return self.sumar(a, b)

                if operador == "-":
                    return self.restar(a, b)

                if operador == "*":
                    return self.multiplicar(a, b)

                if operador == "/":
                    return self.dividir(a, b)

        raise ValueError("Operación no válida")


# ==========================================
# CLASE INTERFAZ GRÁFICA
# ==========================================

class CalculadoraApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Calculadora POO")
        self.geometry("380x520")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.calculadora = Calculadora()

        self.crear_pantalla()
        self.crear_botones()

    # ==========================================
    # PANTALLA
    # ==========================================

    def crear_pantalla(self):

        self.pantalla = ctk.CTkEntry(
            self,
            font=("Arial", 32),
            justify="right",
            height=70,
            corner_radius=10
        )

        self.pantalla.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=15,
            pady=20,
            sticky="nsew"
        )

    # ==========================================
    # BOTONES
    # ==========================================

    def crear_botones(self):

        botones = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "Salir"]
        ]

        for fila, botones_fila in enumerate(botones, start=1):

            for columna, texto in enumerate(botones_fila):

                boton = ctk.CTkButton(
                    self,
                    text=texto,
                    font=("Arial", 20, "bold"),
                    fg_color=self.obtener_color(texto),
                    command=lambda valor=texto: self.presionar(valor)
                )

                boton.grid(
                    row=fila,
                    column=columna,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

        for columna in range(4):
            self.grid_columnconfigure(columna, weight=1)

        for fila in range(1, 6):
            self.grid_rowconfigure(fila, weight=1)

    # ==========================================
    # COLORES
    # ==========================================

    def obtener_color(self, texto):

        if texto in ["/", "*", "-", "+", "="]:
            return "#1f538d"

        if texto == "Salir":
            return "#a83232"

        return "#2471a3"

    # ==========================================
    # BOTONES
    # ==========================================

    def presionar(self, valor):

        expresion = self.pantalla.get()

        if valor == "C":
            self.limpiar()

        elif valor == "⌫":
            self.borrar()

        elif valor == "Salir":
            self.destroy()

        elif valor == "=":
            self.mostrar_resultado()

        elif valor == "%":
            self.calcular_porcentaje()

        else:
            self.pantalla.insert("end", valor)

    # ==========================================
    # LIMPIAR
    # ==========================================

    def limpiar(self):

        self.pantalla.delete(0, "end")

    # ==========================================
    # BORRAR
    # ==========================================

    def borrar(self):

        expresion = self.pantalla.get()

        self.pantalla.delete(0, "end")
        self.pantalla.insert("end", expresion[:-1])

    # ==========================================
    # RESULTADO
    # ==========================================

    def mostrar_resultado(self):

        expresion = self.pantalla.get()

        if not expresion:
            return

        try:
            resultado = self.calculadora.calcular(expresion)

            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)

            self.limpiar()
            self.pantalla.insert("end", str(resultado))

        except ValueError:
            self.limpiar()
            self.pantalla.insert("end", "Error")

    # ==========================================
    # PORCENTAJE
    # ==========================================

    def calcular_porcentaje(self):

        try:
            numero = float(self.pantalla.get())
            resultado = numero / 100

            self.limpiar()
            self.pantalla.insert("end", str(resultado))

        except ValueError:
            self.limpiar()
            self.pantalla.insert("end", "Error")


# ==========================================
# EJECUTAR PROGRAMA
# ==========================================

if __name__ == "__main__":

    app = CalculadoraApp()
    app.mainloop()



