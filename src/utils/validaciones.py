from negocio.negocio import graphi
from utils.colors_text import red_text, yellow_text, green_text


# validaciones
def intValidate(msg="Ingrese un numero positivo: "):
    entero = ""
    while not entero.isdecimal():
        entero = input(msg)
        if not entero.isdecimal():
            print(red_text("Debe ingresar un numero entero!"))
    return int(entero)


def floatValidate(msg="Ingrese un numero decimal: "):
    float_num = ""
    while not is_float(float_num):
        float_num = input(msg)
        if not is_float(float_num):
            print("Ingrese un numero decimal: ")
    float_num = float(float_num)
    if float_num < 0:
        texto = "El numero no puede ser negativo"
        graphi(texto)
        return floatValidate()
    return float(float_num)


def floatValidate_neg(msg="Ingrese un numero decimal: "):
    float_num = ""
    while not is_float(float_num):
        float_num = input(msg)
        if not is_float(float_num):
            print("Ingrese un numero decimal: ")
    return float(float_num)


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def validateClientName():
    while True:
        name = input("Ingrese el Nombre y Apellido: ")
        if len(name) < 61:
            return name
        else:
            print(red_text("El nombre debe tener menos de 60 caracteres"))


def validateProductName(msg="Ingrese el nombre no mas de 30 caracteres: ") -> str:
    while True:
        name = input(msg)
        if len(name) < 30:
            return name
        else:
            print(red_text("El nombre debe tener menos de 50 caracteres"))


def dniValidate() -> int:
    dni = intValidate(yellow_text("Ingrese su DNI, sin coma ni puntos: "))
    while len(str(dni)) != 8:
        print(red_text("El DNI ingresado no es valido, Intentelo nuevamente!"))
        dni = intValidate(yellow_text("Ingrese su DNI, sin coma ni puntos: "))
    print(green_text(f"Su DNI ({dni}) se guardo satisfactoriamente!"))
    return int(dni)
