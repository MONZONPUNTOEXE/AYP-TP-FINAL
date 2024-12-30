# funciones de Orden -----------------
def subtotalCarrito(carrito) -> float:
    suma = 0
    for producto in carrito:
        suma += producto.product_price
    return float(suma)


def mostrarCarrito(carrito: list):
    for producto in carrito:
        print(f"{producto.product_name} ${producto.product_price}")


def buscar_cliente_producto():
    while True:
        cod = clases.gestor_de_pedidos.create_order_cod()
        print("\t ------------ Lista de Clientes -----------------")
        clases.gestor_de_clientes.mostrar_simplificado()
        dni_code = intValidate(
            "\nIngrese DNI del Cliente Para realizar el Pedido o '4' Si desea Salir: "
        )
        client_encontrado = clases.gestor_de_clientes.buscar_por_codigo(
            dni_code)
        if client_encontrado:
            print(f"\n\tSu Cliente es: {
                client_encontrado.surname_name}\n")
            return (cod, client_encontrado.surname_name)
        elif dni_code == 4:
            return (None, None)
        else:
            print(
                colors.WARNING,
                "El DNI ingresado no existe, intentelo nuevamente",
                colors.RESET,
            )


def buscar_sucursal_producto():
    while True:
        print("\t ------------ Lista de Sucursales -----------------")
        clases.gestor_de_sucursal.mostrar_simplificado()
        code = intValidate(
            "\nIngrese el codigo del la Sucursal Para agregar productos: "
        )
        sucursal_encontrado = clases.gestor_de_sucursal.buscar_por_codigo(code)
        if sucursal_encontrado:
            print(f"\n\tSu Sucursal es: {
                sucursal_encontrado.sucursal_name}\n")
            return sucursal_encontrado.sucursal_name
        else:
            print(
                colors.WARNING,
                "El codigo de Sucursal ingresado no existe, intentelo nuevamente",
                colors.RESET,
            )


def createOrder():
    global gestor_de_pedidos
    global gestor_de_clientes
    global gestor_de_productos
    CARRITO_DE_PRODUCTOS = []

    pyfiglet.print_figlet(text="Crear Pedidos", colors="BLUE")
    if (
        clases.gestor_de_clientes.validarListaVacia()
        and clases.gestor_de_productos.validarListaVacia()
    ):
        cod, client_encontrado = buscar_cliente_producto()
        while True:
            if not (cod and client_encontrado):
                break
            if len(CARRITO_DE_PRODUCTOS) > 1:
                print(
                    "\n\n\t----------------------------------------------------------"
                )
                print(
                    f"\tHay ({len(CARRITO_DE_PRODUCTOS)}) Productos en el Carrito para {
                        client_encontrado}\n\tEl Subtotal sin Cargos es de ${subtotalCarrito(CARRITO_DE_PRODUCTOS)}"
                )
                print("\t----------------------------------------------------------")
            print("\n\t--------- Productos Disponibles -------------")
            clases.gestor_de_productos.mostrar_simplificado()
            prod_code = intValidate(
                "Ingrese el Codigo del Producto que desee agregar: "
            )
            producto_encontrado = clases.gestor_de_productos.buscar_por_codigo(
                prod_code
            )
            if producto_encontrado:
                CARRITO_DE_PRODUCTOS.append(producto_encontrado)
                if len(CARRITO_DE_PRODUCTOS) > 1:
                    print(
                        f"{colors.WARNING}Carrito Actual para {
                            client_encontrado}{colors.RESET}: "
                    )
                    mostrarCarrito(CARRITO_DE_PRODUCTOS)
                    print(
                        f"{colors.OK}El Subtotal del Carrito es de ${
                            subtotalCarrito(CARRITO_DE_PRODUCTOS)}\n{colors.RESET}"
                    )
                user = input(
                    f"Desea ingresar mas Productos al Carrito para {
                        client_encontrado} ?: s/n "
                )
                if user.lower() in ("n", "no"):
                    subtotal = subtotalCarrito(CARRITO_DE_PRODUCTOS)
                    print(
                        f"\n\t --- El Subtotal del Carrito es de ${
                            subtotal} --- "
                    )
                    print(
                        "- Si desea hacer un Descuento Ingrese el porcentaje con numero negativo"
                    )
                    print("(Ejemplo: -5, -15, -20)")
                    print(
                        "- Si desea un cargo extra Ingrese el porcentaje con numero positivo"
                    )
                    print(
                        "- Si no desea agregar Descuento ni Cargos Extras ingrese '0 (cero)'"
                    )
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
                            new_pedido = clases.Order(
                                cod,
                                client_encontrado,
                                CARRITO_DE_PRODUCTOS,
                                opcion,
                                subtotal,
                                total,
                            )
                            clases.gestor_de_pedidos.pedidos.append(new_pedido)
                            escribir_en_binario_pedidos()
                            CARRITO_DE_PRODUCTOS = []
                            return createOrder()
                        else:
                            cargo = subtotal * opcion / 100
                            total = cargo + subtotal
                            print(f"- El Subtotal es de {subtotal}")
                            print(f"- El Cargo es de {opcion}%")
                            print(f"- El Total es de: ${total}")
                            new_pedido = clases.Order(
                                cod,
                                client_encontrado,
                                CARRITO_DE_PRODUCTOS,
                                float(opcion),
                                float(subtotal),
                                float(total),
                            )
                            print(new_pedido)
                            clases.gestor_de_pedidos.pedidos.append(new_pedido)
                            escribir_en_binario_pedidos()
                            CARRITO_DE_PRODUCTOS = []
                            return createOrder()
            else:
                print(
                    colors.FAIL
                    + "El Codigo del Producto no fue encontrado"
                    + colors.RESET
                )
    else:
        if len(clases.gestor_de_productos.productos) == 0:
            text = "No hay productos para seleccionar, debe cargar los Productos e intentelo nuevamente"
            graphi(text)
        if len(clases.gestor_de_clientes.clientes) == 0:
            text = "No hay Clientes para seleccionar, debe cargar los Clientes e intentelo nuevamente"
            graphi(text)


def readOrder():
    global gestor_de_pedidos
    while True:
        # simplificado
        clases.gestor_de_pedidos.mostrar_simplificado()
        opcion = intValidate(
            "Ingrese el ID del Pedido para mostrar el Carrito del Cliente | '0' para Salir: "
        )
        order_encontrada = clases.gestor_de_pedidos.buscar_por_codigo(opcion)
        if order_encontrada:
            order_encontrada.mostrarCarritoOrder()
        elif opcion == 0:
            break
        else:
            print(
                colors.FAIL,
                "El ID del Pedido no existe, intentelo nuevamente",
                colors.RESET,
            )


def indexCarrito(carrito, index_busqueda):
    for i in range(len(carrito)):
        i = i + 1
        if index_busqueda == i:
            print("entrado")
            return i
    return -1


def updateCarrito(carrito):
    global gestor_de_productos
    global gestor_de_pedidos
    while True:
        i = 1
        for producto in carrito:
            print(
                f"\t- Indice: {(i)} ID: {producto.ref_code} {
                    producto.product_name} ${producto.product_price}"
            )
            i += 1

        buscar_producto = intValidate(
            "Ingrese el Indice del Producto que desea reemplazar | '0' Para salir: "
        )
        producto_encontrado = indexCarrito(carrito, int(buscar_producto))
        if producto_encontrado != -1:
            print(producto_encontrado)
            clases.gestor_de_productos.mostrar_simplificado()
            buscar_nuevo_producto = intValidate(
                "Ingrese el ID del Producto nuevo: ")
            update_product = clases.gestor_de_productos.buscar_por_codigo(
                buscar_nuevo_producto
            )
            print(update_product)
            if update_product:
                if producto_encontrado:
                    print("-------------- Estos son los cambios ---------------------")
                    carrito[producto_encontrado - 1] = update_product
                    print(carrito)
                    pregunta = input("Desea continuar editando?: S/n")
                    if pregunta in ("n", "no"):
                        return carrito
        elif buscar_producto == 0:
            break
        elif producto_encontrado == -1:
            print(
                colors.FAIL,
                "Algo ha salido mal, no se ha podido actulizar",
                colors.RESET,
            )


def updateOrder():
    global gestor_de_pedidos
    global gestor_de_clientes
    clases.gestor_de_pedidos.mostrar_simplificado()
    buscar_pedido = intValidate(
        "Ingrese el ID del Pedido que desea modificar: ")
    pedido_encontrado = clases.gestor_de_pedidos.buscar_por_codigo(
        buscar_pedido)
    if pedido_encontrado:
        clases.gestor_de_clientes.mostrar_simplificado()
        buscar_cliente = intValidate(
            "Ingrese el DNI del si lo quiere reemplazar cliente para remplazar, sino indique el anterior: "
        )
        cliente_encontrado = clases.gestor_de_clientes.buscar_por_codigo(
            buscar_cliente)
        if cliente_encontrado:
            pedido_encontrado.customer = cliente_encontrado.surname_name

            lista_productos = updateCarrito(pedido_encontrado.product_list)
            print(lista_productos)
            subtotal = subtotalCarrito(lista_productos)
            print(
                f"\n\t --- El Subtotal del Carrito es de ${
                    subtotal} --- "
            )
            print(
                "- Si desea hacer un Descuento Ingrese el porcentaje con numero negativo"
            )
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
                    fecha_modificada = clases.Fecha()

                    pedido_encontrado.order_date_edit = True
                    pedido_encontrado.fecha_edit = fecha_modificada
                    pedido_encontrado.subtotal = subtotal
                    pedido_encontrado.extra_charge = opcion
                    pedido_encontrado.total = total
                    escribir_en_binario_pedidos()
                    break

                else:
                    cargo = subtotal * opcion / 100
                    total = cargo + subtotal
                    print(f"- El Subtotal es de {subtotal}")
                    print(f"- El Cargo es de {opcion}%")
                    print(f"- El Total es de: ${total}")
                    fecha_modificada = clases.Fecha()

                    pedido_encontrado.order_date_edit = True
                    pedido_encontrado.fecha_edit = fecha_modificada
                    pedido_encontrado.subtotal = subtotal
                    pedido_encontrado.extra_charge = opcion
                    pedido_encontrado.total = total
                    escribir_en_binario_pedidos()
                    break

        else:
            print(
                colors.FAIL,
                "El DNI cliente no se encontro o no existe, no se ha actualizado",
                colors.RESET,
            )

    else:
        print(
            colors.FAIL,
            "El Pedido no se encontro o no existe, no se ha actualizado",
            colors.RESET,
        )


# Delete Cliente
def deleteOrder():
    global gestor_de_pedidos
    clases.gestor_de_pedidos.mostrar_simplificado()
    code = intValidate("Ingrese el ID del Pedido que desea Eliminar: ")
    pedido_encontrado = clases.gestor_de_pedidos.buscar_por_codigo(code)
    if pedido_encontrado:
        opcion = input(f"\n\tDesea eliminar ?\n\n{pedido_encontrado}\nS/n: ")
        if opcion.lower() in ("si", "s", "y", "yes" "ye"):
            clases.gestor_de_pedidos.pedidos.remove(pedido_encontrado)
            escribir_en_binario_pedidos()
            print(f"\n\tSe ha eliminado de la lista:\n{pedido_encontrado}")
        else:
            print("El pedido no se ha sido eliminado...")
    else:
        print("El codigo no fue encontrado!")
