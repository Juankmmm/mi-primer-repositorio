import tkinter as tk


# ==========================================
# PREGUNTAS Y PREMIOS
# ==========================================

preguntas = [
    {
        "pregunta": "¿Cuál es la capital de Colombia?",
        "opciones": [
            "Medellín",
            "Bogotá",
            "Cali",
            "Barranquilla"
        ],
        "correcta": 1,
        "premio": 100000
    },

    {
        "pregunta": "¿Cuál es el planeta más grande?",
        "opciones": [
            "Tierra",
            "Marte",
            "Júpiter",
            "Venus"
        ],
        "correcta": 2,
        "premio": 500000
    },

    {
        "pregunta": "¿Cuánto es 5 × 5?",
        "opciones": [
            "10",
            "20",
            "25",
            "30"
        ],
        "correcta": 2,
        "premio": 1000000
    }
]


# ==========================================
# VENTANA
# ==========================================

ventana = tk.Tk()

ventana.title("¿Quién quiere ser millonario?")
ventana.geometry("900x600")

ventana.configure(bg="blue")


# ==========================================
# VARIABLES DEL JUEGO
# ==========================================

pregunta_actual = 0
dinero_ganado = 0


# ==========================================
# FUNCIONES
# ==========================================

def comenzar():

    global pregunta_actual
    global dinero_ganado

    pregunta_actual = 0
    dinero_ganado = 0

    boton_comenzar.pack_forget()

    boton1.pack(pady=5)
    boton2.pack(pady=5)
    boton3.pack(pady=5)
    boton4.pack(pady=5)

    mostrar_pregunta()


def mostrar_pregunta():

    pregunta = preguntas[pregunta_actual]

    titulo.config(
        text=pregunta["pregunta"]
    )

    premio.config(
        text="Premio: $" + f"{pregunta['premio']:,}".replace(",", ".")
    )

    boton1.config(
        text="A. " + pregunta["opciones"][0],
        command=lambda: responder(0)
    )

    boton2.config(
        text="B. " + pregunta["opciones"][1],
        command=lambda: responder(1)
    )

    boton3.config(
        text="C. " + pregunta["opciones"][2],
        command=lambda: responder(2)
    )

    boton4.config(
        text="D. " + pregunta["opciones"][3],
        command=lambda: responder(3)
    )


def responder(opcion):

    global pregunta_actual
    global dinero_ganado

    correcta = preguntas[pregunta_actual]["correcta"]

    if opcion == correcta:

        dinero_ganado = preguntas[pregunta_actual]["premio"]

        pregunta_actual += 1

        if pregunta_actual == len(preguntas):

            titulo.config(
                text="🏆 ¡FELICITACIONES! GANASTE"
            )

            premio.config(
                text="Premio final: $" +
                f"{dinero_ganado:,}".replace(",", ".")
            )

            ocultar_botones()

        else:

            titulo.config(
                text="✅ ¡RESPUESTA CORRECTA!"
            )

            ventana.after(
                1000,
                mostrar_pregunta
            )

    else:

        titulo.config(
            text="❌ RESPUESTA INCORRECTA"
        )

        premio.config(
            text="Dinero ganado: $" +
            f"{dinero_ganado:,}".replace(",", ".")
        )

        ocultar_botones()


def ocultar_botones():

    boton1.pack_forget()
    boton2.pack_forget()
    boton3.pack_forget()
    boton4.pack_forget()


# ==========================================
# TÍTULO
# ==========================================

titulo = tk.Label(
    ventana,
    text="¿QUIÉN QUIERE SER MILLONARIO?",
    font=("Arial", 26),
    bg="blue",
    fg="white"
)

titulo.pack(pady=40)


# ==========================================
# PREMIO
# ==========================================

premio = tk.Label(
    ventana,
    text="Premio: $0",
    font=("Arial", 20),
    bg="blue",
    fg="white"
)

premio.pack(pady=10)


# ==========================================
# BOTÓN COMENZAR
# ==========================================

boton_comenzar = tk.Button(
    ventana,
    text="COMENZAR",
    font=("Arial", 16),
    command=comenzar
)

boton_comenzar.pack(pady=20)


# ==========================================
# BOTONES DE RESPUESTAS
# ==========================================

boton1 = tk.Button(
    ventana,
    font=("Arial", 14),
    width=35
)

boton2 = tk.Button(
    ventana,
    font=("Arial", 14),
    width=35
)

boton3 = tk.Button(
    ventana,
    font=("Arial", 14),
    width=35
)

boton4 = tk.Button(
    ventana,
    font=("Arial", 14),
    width=35
)


# ==========================================
# EJECUTAR PROGRAMA
# ==========================================

ventana.mainloop()