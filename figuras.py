import math

# --- Funciones de Cálculo ---
def area_triangulo(b, h):
    return (b * h) / 2

def perimetro_triangulo(a, b, c):
    return a + b + c

def area_rectangulo(b, h):
    return b * h

def perimetro_rectangulo(b, h):
    return 2 * (b + h)

def area_cuadrado(lado):
    return lado * lado

def perimetro_cuadrado(lado):
    return 4 * lado

def area_circulo(r):
    return math.pi * (r ** 2)

def perimetro_circulo(r):
    return 2 * math.pi * r

# --- Menú Principal ---
print("===== FIGURAS PLANAS =====")
print("1. Triángulo")
print("2. Rectángulo")
print("3. Cuadrado")
print("4. Círculo")

figura = int(input("Seleccione una figura: "))
opcion = int(input("1. Área\n2. Perímetro\nSeleccione: "))

match figura:
    case 1:  # Triángulo
        if opcion == 1:
            b = float(input("Base: "))
            h = float(input("Altura: "))
            print("Área =", area_triangulo(b, h))
        else:
            a = float(input("Lado 1: "))
            b = float(input("Lado 2: "))
            c = float(input("Lado 3: "))
            print("Perímetro =", perimetro_triangulo(a, b, c))

    case 2:  # Rectángulo
        b = float(input("Base: "))
        h = float(input("Altura: "))
        resultado = area_rectangulo(b, h) if opcion == 1 else perimetro_rectangulo(b, h)
        etiqueta = "Área" if opcion == 1 else "Perímetro"
        print(f"{etiqueta} = {resultado}")

    case 3:  # Cuadrado
        lado = float(input("Lado: "))
        resultado = area_cuadrado(lado) if opcion == 1 else perimetro_cuadrado(lado)
        etiqueta = "Área" if opcion == 1 else "Perímetro"
        print(f"{etiqueta} = {resultado}")

    case 4:  # Círculo
        r = float(input("Radio: "))
        resultado = area_circulo(r) if opcion == 1 else perimetro_circulo(r)
        etiqueta = "Área" if opcion == 1 else "Perímetro"
        print(f"{etiqueta} = {resultado:.2f}")

    case _:
        print("Opción de figura no válida.")