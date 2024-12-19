# validaciones
def intValidate(msg="Ingrese un numero positivo: "):
    entero = ""
    while not entero.isdecimal():
        entero = input(msg)
        if not entero.isdecimal():
            print(colors.WARNING, "Debe ingresar un numero entero!", colors.RESET)
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
        name = input("Ingrese el nombre el Nombre y Apellido: ")
        if len(name) < 61:
            return name
        else:
            print(
                colors.FAIL
                + "El nombre debe tener menos de 60 caracteres"
                + colors.RESET
            )


def validateProductName(msg="Ingrese el nombre no mas de 30 caracteres: ") -> str:
    while True:
        name = input(msg)
        if len(name) < 30:
            return name
        else:
            print(
                colors.FAIL
                + "El nombre debe tener menos de 50 caracteres"
                + colors.RESET
            )


def dniValidate() -> int:
    dni = intValidate(
        colors.WARNING + "Ingrese su DNI, sin coma ni puntos: " + colors.RESET
    )
    while len(str(dni)) != 8:
        print(
            colors.FAIL
            + "El DNI ingresado no es valido, Intentelo nuevamente!"
            + colors.RESET
        )
        dni = intValidate(
            colors.WARNING + "Ingrese su DNI, sin coma ni puntos: " + colors.RESET
        )
    print(f"{colors.OK}Su DNI ({dni}) se guardo satisfactoriamente! {colors.RESET}")
    return int(dni)
