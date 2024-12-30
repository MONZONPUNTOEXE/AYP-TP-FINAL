# Funcionalidades de Sucursal
def create_sucursal():
    global gestor_de_sucursal
    global gestor_de_productos
    pyfiglet.print_figlet(text="Crear Sucursal", colors="BLUE")
    while True:
        cod = clases.gestor_de_sucursal.create_sucursal_cod()
        name = validateProductName()
        new_sucursal = clases.Sucursal(cod, name, [], 0, 0, 0)
        user = input(
            f"{colors.WARNING}Desea ingresar Productos a esta Sucursal ?: s/n {colors.RESET}"
        )
        if (
            user.lower() in ("s", "si", "yes", "y")
            and clases.gestor_de_productos.validarListaVacia()
        ):
            new_sucursal_with_products = carrito_add_product(new_sucursal)
            clases.gestor_de_sucursal.sucursales.append(
                new_sucursal_with_products)
        else:
            clases.gestor_de_sucursal.sucursales.append(new_sucursal)
            escribir_en_binario_sucursales()
            print(colors.OK, "Se ha creado una nueva Sucursal", colors.RESET)
            print(new_sucursal)
        if not clases.gestor_de_productos.validarListaVacia() and user.lower() in (
            "s",
            "si",
            "yes",
            "y",
        ):
            print(
                colors.FAIL,
                "Lista de Productos Vacia",
                colors.RESET,
            )
            print(
                colors.FAIL,
                "Si deseas agregar productos a esta Sucursal, agregue Productos en el Gestor de Productos e intentelo nuevamente",
                colors.RESET,
            )
        user = input(f"{colors.WARNING}hay un total de ({
                     len(clases.gestor_de_sucursal.sucursales)}) Sucursales, desea ingresar mas Sucursales ?: s/n {colors.RESET}")
        if user.lower() == "n":
            break


def add_sucursal_product():
    global gestor_de_productos
    global gestor_de_sucursal
    pyfiglet.print_figlet(text="Agregar Productos a Sucursal", colors="BLUE")
    clases.gestor_de_sucursal.mostrar_simplificado()
    if (
        clases.gestor_de_sucursal.validarListaVacia()
        and clases.gestor_de_productos.validarListaVacia()
    ):
        sucursal_encontrado = buscar_sucursal_producto()
        while True:
            if not (sucursal_encontrado):
                break
            carrito_add_product(sucursal_encontrado)
    else:
        if len(clases.gestor_de_productos.productos) == 0:
            text = "No hay productos para seleccionar, debe cargar los Productos e intentelo nuevamente"
            graphi(text)


# sumar todos los stock que tiene el Producto


def carrito_add_product(sucursal):
    global gestor_de_productos
    global gestor_de_sucursal

    CARRITO_DE_PRODUCTOS = []
    while True:
        if len(CARRITO_DE_PRODUCTOS) > 1:
            print("\n\n\t----------------------------------------------------------")
            print(
                f"\tHay ({len(CARRITO_DE_PRODUCTOS)}) Productos en el Carrito para {
                    sucursal.sucursal_name}\n\tEl Subtotal sin Cargos es de ${subtotalCarrito(CARRITO_DE_PRODUCTOS)}"
            )
            print("\t----------------------------------------------------------")
        print("\n\t--------- Productos Disponibles -------------")
        clases.gestor_de_productos.mostrar_simplificado()
        prod_code = intValidate(
            "Ingrese el Codigo del Producto que desee agregar: ")
        producto_encontrado = clases.gestor_de_productos.buscar_por_codigo(
            prod_code)
        if producto_encontrado:
            producto_de_sucursal = copy.deepcopy(producto_encontrado)
            stock_validate = "Ingrese el Stock que desea destinar a la Sucursal"
            sucursal_stock = updateStock(
                producto_encontrado, stock_validate, False, True
            )
            user = ""
            if producto_de_sucursal.stock == 0 or None:
                print(colors.FAIL, "No hay mas Stock para este Producto", colors.RESET)
                user = input(
                    f"Desea ingresar mas Productos al Carrito para {
                        sucursal.sucursal_name} ?: s/n "
                )
                if user.lower() in ("n", "no"):
                    subtotal = subtotalCarrito(CARRITO_DE_PRODUCTOS)
                    print(
                        f"\n\t --- El Subtotal del Carrito es de ${
                            subtotal} --- "
                    )
                    agregar_descuento(sucursal, CARRITO_DE_PRODUCTOS)
                    break
            else:
                producto_de_sucursal.stock = sucursal_stock
                CARRITO_DE_PRODUCTOS.append(producto_encontrado)
            if len(CARRITO_DE_PRODUCTOS) > 1:
                print(
                    f"{colors.WARNING}Carrito Actual para {
                        sucursal.sucursal_name}{colors.RESET}: "
                )
                mostrarCarrito(CARRITO_DE_PRODUCTOS)
                print(
                    f"{colors.OK}El Subtotal del Carrito es de ${
                        subtotalCarrito(CARRITO_DE_PRODUCTOS)}\n{colors.RESET}"
                )
            if user == "":
                user = input(
                    f"Desea ingresar mas Productos al Carrito para {
                        sucursal.sucursal_name} ?: s/n "
                )
                if user.lower() in ("n", "no"):
                    subtotal = subtotalCarrito(CARRITO_DE_PRODUCTOS)
                    print(
                        f"\n\t --- El Subtotal del Carrito es de ${
                            subtotal} --- "
                    )
                    agregar_descuento(sucursal, CARRITO_DE_PRODUCTOS)
                    break
        else:
            print(
                colors.FAIL + "El Codigo del Producto no fue encontrado" + colors.RESET
            )


def agregar_descuento(sucursal, CARRITO_DE_PRODUCTOS: list):
    subtotal = subtotalCarrito(CARRITO_DE_PRODUCTOS)
    print("- Si desea hacer un Descuento Ingrese el porcentaje con numero negativo")
    print("(Ejemplo: -5, -15, -20)")
    print("- Si desea un cargo extra Ingrese el porcentaje con numero positivo")
    print("- Si no desea agregar Descuento ni Cargos Extras ingrese '0 (cero)'")
    while True:
        opcion = floatValidate_neg()
        if opcion >= 1000 or opcion <= -100:
            print(
                "No puede haber un descuento mayor al 100%, tampoco un recargo mayor 1000%"
            )
        elif opcion == 0:
            cargo = 0
            total = cargo + subtotal
            print(f"\n\t- El Subtotal es de ${subtotal}")
            print(f"\t- El Cargo es de {opcion}%")
            print(f"\t- El Total es de: ${total}")
            print(sucursal)
            cod = sucursal.id_sucursal
            name = sucursal.sucursal_name
            new_sucursal = clases.Sucursal(
                cod, name, CARRITO_DE_PRODUCTOS, opcion, subtotal, total
            )
            CARRITO_DE_PRODUCTOS = []
            return new_sucursal
        else:
            cargo = subtotal * opcion / 100
            total = cargo + subtotal
            print(f"- El Subtotal es de {subtotal}")
            print(f"- El Cargo es de {opcion}%")
            print(f"- El Total es de: ${total}")

            print(sucursal)
            cod = sucursal.id_sucursal
            name = sucursal.sucursal_name
            new_sucursal = clases.Sucursal(
                cod, name, CARRITO_DE_PRODUCTOS, opcion, subtotal, total
            )
            CARRITO_DE_PRODUCTOS = []
            return new_sucursal
