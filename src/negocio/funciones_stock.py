# Funciones de Stock -------------
def updateStock(product, msg="Ingrese el Stock", entrada=False, salida=False):
    while True:
        stock_validate = intValidate(msg)
        if product.stock == 0:
            print("No hay mas Stock para este Producto")
            return 0
        if stock_validate == 0:
            print(f"{colors.FAIL}Hubo un error, el Stock no puede ser '0 (cero)'{
                colors.RESET}")
        elif entrada:
            product.stock += stock_validate
            return int(stock_validate)
        elif salida:
            if product.stock < stock_validate:
                print(f"{colors.FAIL}El stock actual es ({product.stock})")
                print(f"Y quiere egresar ({stock_validate})")
                print(f"Su Stock es menor al monto que desea egresar{
                    colors.RESET}")
                print("Intentelo nuevamente")
            else:
                product.stock -= stock_validate
                return int(stock_validate)
        else:
            print(f"{colors.FAIL}Hubo un error, no hay entrada ni salida verdadera {
                colors.RESET}")
