from utils.validaciones import intValidate
from utils.colors_text import red_text


# Funciones de Stock -------------
def updateStock(product, msg="Ingrese el Stock", entrada=False, salida=False):
    while True:
        stock_validate = intValidate(msg)
        if product.stock == 0:
            print("No hay mas Stock para este Producto")
            return 0
        if stock_validate == 0:
            print(red_text("Hubo un error, el Stock no puede ser '0 (cero)'"))
        elif entrada:
            product.stock += stock_validate
            return int(stock_validate)
        elif salida:
            if product.stock < stock_validate:
                print(red_text(f"El stock actual es ({product.stock})"))
                print(red_text(f"Y quiere egresar ({stock_validate})"))
                print(red_text(f"Su Stock es menor al monto que desea egresar"))
                print("Intentelo nuevamente")
            else:
                product.stock -= stock_validate
                return int(stock_validate)
        else:
            print(red_text("Hubo un error, no hay entrada ni salida verdadera"))
