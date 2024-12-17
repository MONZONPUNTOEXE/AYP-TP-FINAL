from pickle import dumps, load
import copy
import os

# external library
import pyfiglet

# code internal
import negocio
import utils as menu_text
import clases
from clases import colors
from negocio import graphi

# Creacion de los objetos "Gestores de Entidades" -----------------------------
gestor_de_productos = clases.gestorProductos()
gestor_de_clientes = clases.gestorClientes()
gestor_de_pedidos = clases.orderGestor()
gestor_de_sucursal = clases.gestorSucursal()


# Escribir en binario
def escribir_en_binario_productos():
    global gestor_de_productos
    with open("./bin/productos.bin", "wb") as bin_file:
        bin_file.write(dumps(gestor_de_productos.productos))


def escribir_en_binario_clientes():
    global gestor_de_clientes
    with open("./bin/clientes.bin", "wb") as bin_file:
        bin_file.write(dumps(gestor_de_clientes.clientes))


def escribir_en_binario_pedidos():
    global gestor_de_pedidos
    with open("./bin/pedidos.bin", "wb") as bin_file:
        bin_file.write(dumps(gestor_de_pedidos.pedidos))


def escribir_en_binario_sucursales():
    global gestor_de_productos
    with open("./bin/sucursales.bin", "wb") as bin_file:
        bin_file.write(dumps(gestor_de_sucursal.sucursales))


# Cargar binarios
def cargar_desde_binario_productos():
    global gestor_de_productos
    with open("productos.bin", "rb") as bin_file:
        gestor_de_productos.productos = load(bin_file)


def cargar_desde_binario_clientes():
    global gestor_de_clientes
    with open("clientes.bin", "rb") as bin_file:
        gestor_de_clientes.clientes = load(bin_file)


def cargar_desde_binario_pedidos():
    global gestor_de_pedidos
    with open("pedidos.bin", "rb") as bin_file:
        gestor_de_pedidos.pedidos = load(bin_file)


def permanenciaDeArchivos():
    dirs = os.listdir()
    for directory in dirs:
        if directory == "bin":
            print("La carpeta bin existe")
            print("Cargando la carpeta 'bin'...")
            break
    else:
        print("La Carpeta 'bin' no existe")
        print("Creando la Carpeta 'bin'...")
        os.mkdir("bin")
        print("La Carpeta 'bin' ha sido creada")
    os.chdir("./bin")
    files = os.listdir()
    for bin in files:
        print(bin)
        print("Cargando los binarios...")
        if bin == "productos.bin":
            print("Cargando 'productos.bin'...")
            cargar_desde_binario_productos()
            print("'productos.bin' Se ha cargado exitosamente.")
        elif bin == "clientes.bin":
            print("Cargando 'clientes.bin'...")
            cargar_desde_binario_clientes()
            print("'clientes.bin' Se haa cargado exitosamente.")
        elif bin == "pedidos.bin":
            print("Cargando 'pedidos.bin'...")
            cargar_desde_binario_pedidos()
            print("'pedidos.bin' Se ha cargado exitosamente.")
    os.chdir("..")


# Create Producto
def createProduct():
    global gestor_de_productos
    while True:
        cod = gestor_de_productos.obtener_nuevo_codigo()
        name = negocio.validateProductName()
        cost_price = negocio.floatValidate("Ingrese el costo del Producto : ")
        price = negocio.floatValidate(
            "Ingrese el precio de venta del Producto : ")
        stock = negocio.intValidate("Ingrese el Stock del Producto: ")
        new_product = clases.Producto(cod, name, cost_price, price, stock)
        gestor_de_productos.productos.append(new_product)
        escribir_en_binario_productos()
        print(colors.OK, "Se ha creado un nuevo Producto", colors.RESET)
        print(new_product)
        user = input(f"{colors.WARNING}hay un total de ({
                     len(gestor_de_productos.productos)}) Productos desea ingresar mas ?: s/n {colors.RESET}")
        if user.lower() == "n":
            break


# Update Producto ---------------
def update_all_product():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = negocio.intValidate(
        "Ingrese el codigo del Producto que desea modificar: "
    )
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        print("Nombre del Producto Actual", producto_encontrado.product_name)
        nuevo_nombre = negocio.validateProductName("Ingrese el nuevo nombre: ")
        print("Precio de Costo del Producto",
              producto_encontrado.product_cost_price)
        nuevo_cost_price = negocio.floatValidate(
            "Ingrese el nuevo precio de costo: ")
        print("Precio Final del Producto", producto_encontrado.product_price)
        nuevo_precio = negocio.floatValidate("Ingrese el nuevo precio: ")
        print("Stock actual del Producto", producto_encontrado.stock)
        nuevo_stock = negocio.intValidate("Ingrese el nuevo Stock: ")
        # cambios anteriores
        nombre_sin_cambio = producto_encontrado.product_name
        cost_price_sin_cambio = producto_encontrado.product_cost_price
        precio_sin_cambio = producto_encontrado.product_price
        stock_sin_cambio = producto_encontrado.stock

        text_sin_cambios = "Sin aplicar Cambios"
        graphi(text_sin_cambios)
        print(producto_encontrado)

        if nuevo_nombre:
            producto_encontrado.product_name = nuevo_nombre
        if nuevo_cost_price:
            producto_encontrado.product_cost_price = float(nuevo_cost_price)
        if nuevo_precio:
            producto_encontrado.product_price = float(nuevo_precio)
        if nuevo_stock:
            producto_encontrado.stock = int(nuevo_stock)

        text_con_cambios = "Aplicando los cambios... "
        graphi(text_con_cambios)
        print(producto_encontrado)

        decidir_cambios = input("Desea guardar los cambios ? - (Si/no)")
        if decidir_cambios.lower() in ("no", "n"):
            producto_encontrado.product_name = nombre_sin_cambio
            producto_encontrado.product_cost_price = float(
                cost_price_sin_cambio)
            producto_encontrado.product_price = float(precio_sin_cambio)
            producto_encontrado.stock = int(stock_sin_cambio)
            print("El Producto no se ha actualizado")
        else:
            producto_encontrado.date_product_edit = True
            producto_encontrado.date_edit = clases.Fecha()
            escribir_en_binario_productos()
            print("El Producto se ha actualizado correctamente")
            print(producto_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


def update_product_name():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = negocio.intValidate(
        "Ingrese el codigo del Producto que desea modificarle el nombre: "
    )
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        print(
            "Nombre Actual:", colors.OK, producto_encontrado.product_name, colors.RESET
        )
        nuevo_nombre = negocio.validateProductName("Ingrese el nuevo nombre: ")
        # cambios anteriores
        nombre_sin_cambio = producto_encontrado.product_name

        text_sin_cambios = "Sin aplicar Cambios"
        graphi(text_sin_cambios)
        print(producto_encontrado)

        if nuevo_nombre:
            producto_encontrado.product_name = nuevo_nombre

        text_con_cambios = "Aplicando los cambios... "
        graphi(text_con_cambios)
        print(producto_encontrado)

        decidir_cambios = input("Desea guardar los cambios ? - (Si/no)")
        if decidir_cambios.lower() in ("no", "n"):
            producto_encontrado.product_name = nombre_sin_cambio
            print("El Producto no se ha actualizado")
        else:
            producto_encontrado.date_product_edit = True
            producto_encontrado.date_edit = clases.Fecha()
            print("El Producto se ha actualizado correctamente")
            escribir_en_binario_productos()
            print(producto_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


def update_product_cost_price():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = negocio.intValidate(
        "Ingrese el codigo del Producto que desea modificar el costo: "
    )
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        print(
            f"Costo Actual: {colors.OK}${
                producto_encontrado.product_cost_price}{colors.RESET}"
        )
        nuevo_precio = negocio.floatValidate(
            "Ingrese el nuevo Costo del Producto: ")
        # cambios anteriores
        precio_sin_cambio = producto_encontrado.product_cost_price

        text_sin_cambios = "Sin aplicar Cambios"
        graphi(text_sin_cambios)
        print(producto_encontrado)

        if nuevo_precio:
            producto_encontrado.product_cost_price = float(nuevo_precio)

        text_con_cambios = "Aplicando los cambios... "
        graphi(text_con_cambios)
        print(producto_encontrado)

        decidir_cambios = input("Desea guardar los cambios ? - (Si/no)")
        if decidir_cambios.lower() in ("no", "n"):
            producto_encontrado.product_cost_price = precio_sin_cambio
            print("El Producto no se ha actualizado")
        else:
            producto_encontrado.date_product_edit = True
            producto_encontrado.date_edit = clases.Fecha()
            print("El Producto se ha actualizado correctamente")
            escribir_en_binario_productos()
            print(producto_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


def update_product_price():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = negocio.intValidate(
        "Ingrese el codigo del Producto que desea modificar: "
    )
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        print(
            f"Precio final actual: {colors.OK}${
                producto_encontrado.product_price}{colors.RESET}"
        )
        nuevo_precio = input("Ingrese el nuevo Precio Final: ")
        # cambios anteriores
        precio_sin_cambio = producto_encontrado.product_price

        text_sin_cambios = "Sin aplicar Cambios"
        graphi(text_sin_cambios)
        print(producto_encontrado)

        if nuevo_precio:
            producto_encontrado.product_price = float(nuevo_precio)

        text_con_cambios = "Aplicando los cambios... "
        graphi(text_con_cambios)
        print(producto_encontrado)

        decidir_cambios = input("Desea guardar los cambios ? - (Si/no)")
        if decidir_cambios.lower() in ("no", "n"):
            producto_encontrado.product_price = precio_sin_cambio
            print("El Producto no se ha actualizado")
        else:
            producto_encontrado.date_product_edit = True
            producto_encontrado.date_edit = clases.Fecha()
            print("El Producto se ha actualizado correctamente")
            escribir_en_binario_productos()
            print(producto_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


def update_product_stock():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = negocio.intValidate(
        "Ingrese el codigo del Producto que desea modificar su stock: "
    )
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        print(f"Stock Actual: {colors.OK}${
              producto_encontrado.stock}{colors.RESET}")
        print(producto_encontrado.resumenProducto())
        stock_sin_cambios = producto_encontrado.stock
        nuevo_stock = negocio.intValidate("Ingrese el nuevo Stock: ")
        # cambios anteriores
        text_sin_cambios = "Sin aplicar Cambios"
        graphi(text_sin_cambios)
        print(producto_encontrado)

        if nuevo_stock:
            producto_encontrado.stock = nuevo_stock

        text_con_cambios = "Aplicando los cambios... "
        graphi(text_con_cambios)
        print(producto_encontrado)

        decidir_cambios = input("Desea guardar los cambios ? - (Si/no)")
        if decidir_cambios.lower() in ("no", "n"):
            producto_encontrado.stock = stock_sin_cambios
            print("El Stock del Producto no se ha actualizado")
        else:
            producto_encontrado.date_product_edit = True
            producto_encontrado.date_edit = clases.Fecha()
            print("El Stock del Producto se ha actualizado correctamente")
            escribir_en_binario_productos()
            print(producto_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


# Delete Producto
def removeProduct():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    code = negocio.intValidate(
        "Ingrese el codigo del Producto que desea Eliminar: ")
    producto_encontrado = gestor_de_productos.buscar_por_codigo(code)
    if producto_encontrado:
        opcion = input(f"\n\tDesea eliminar ?\n\n{producto_encontrado}\nS/n: ")
        if opcion.lower() in ("si", "s", "y", "yes" "ye"):
            gestor_de_productos.productos.remove(producto_encontrado)
            escribir_en_binario_productos()
            print(f"\n\tSe ha eliminado de la lista:\n{producto_encontrado}")
        else:
            print("El Producto no ha sido eliminado...")
    else:
        print("El codigo no fue encontrado!")


# Funciones de Stock -------------
def updateStock(product, msg="Ingrese el Stock", entrada=False, salida=False):
    while True:
        stock_validate = negocio.intValidate(msg)
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


# funciones de Cliente ---------------


# create Cliente
def createClient():
    global gestor_de_clientes
    while True:
        cod = negocio.dniValidate()
        name = negocio.validateClientName()
        print("Ingrese la fecha de Nacimiento en este formato DD/MM/AAAA")
        date = gestor_de_clientes._pedir_fecha_nacimiento_valida()
        new_client = clases.Cliente(cod, name, date)
        gestor_de_clientes.clientes.append(new_client)
        escribir_en_binario_clientes()
        print("Se ha creado un nuevo Cliente")
        print(new_client)
        user = input(f"hay un total de ({
                     len(gestor_de_clientes.clientes)}) Clientes desea ingresar mas ?: s/n ")
        if user.lower() == "n":
            break


# Update Cliente
def updateClient():
    global gestor_de_clientes
    gestor_de_clientes.mostrar_simplificado()
    client_code = negocio.intValidate(
        "Ingrese el DNI del Cliente que desea modificar: "
    )
    client_encontrado = gestor_de_clientes.buscar_por_codigo(client_code)
    if client_encontrado:
        nuevo_nombre = input(
            "Ingrese el nuevo nombre - (Enter para dejar el actual): ")
        dni_confirm = input(
            "Desea cambiar el DNI y Fecha de Nacimiento del Cliente ? S/n "
        )
        if dni_confirm.lower() in ("no", "n"):
            nuevo_id = ""
        else:
            nuevo_id = negocio.dniValidate()
        nuevo_fecha = gestor_de_clientes._pedir_fecha_nacimiento_valida()

        # cambios anteriores
        nombre_sin_cambio = client_encontrado.surname_name
        id_sin_cambio = client_encontrado.dni
        date_sin_cambio = client_encontrado.fecha_nacimiento

        text_sin_cambios = "Sin aplicar Cambios"
        graphi(text_sin_cambios)
        print(client_encontrado)

        if nuevo_nombre:
            client_encontrado.surname_name = nuevo_nombre
        if nuevo_id:
            client_encontrado.dni = nuevo_id
        if nuevo_fecha:
            client_encontrado.fecha_nacimiento = nuevo_fecha

        text_con_cambios = "Aplicando los cambios... "
        graphi(text_con_cambios)
        print(client_encontrado)

        decidir_cambios = input("Desea guardar los cambios ? - (Si/no)")
        if decidir_cambios.lower() in ("no", "n"):
            client_encontrado.surname_name = nombre_sin_cambio
            client_encontrado.dni = id_sin_cambio
            client_encontrado.fecha_nacimiento = date_sin_cambio
            print("El Cliente no se ha actualizado")
            escribir_en_binario_clientes()
        else:
            print("El Cliente se ha actualizado correctamente")
            escribir_en_binario_clientes()
            print(client_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


# Delete Cliente
def deleteClient():
    global gestor_de_clientes
    gestor_de_clientes.mostrar_simplificado()
    code = negocio.intValidate(
        "Ingrese el DNI del Cliente que desea Eliminar: ")
    client_encontrado = gestor_de_clientes.buscar_por_codigo(code)
    if client_encontrado:
        opcion = input(f"\n\tDesea eliminar ?\n\n{client_encontrado}\nS/n: ")
        if opcion.lower() in ("si", "s", "y", "yes" "ye"):
            gestor_de_clientes.clientes.remove(client_encontrado)
            escribir_en_binario_clientes()
            print(f"\n\tSe ha eliminado de la lista:\n{client_encontrado}")
        else:
            print("El cliente no ha sido eliminado...")
    else:
        print("El codigo no fue encontrado!")


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
        cod = gestor_de_pedidos.create_order_cod()
        print("\t ------------ Lista de Clientes -----------------")
        gestor_de_clientes.mostrar_simplificado()
        dni_code = negocio.intValidate(
            "\nIngrese DNI del Cliente Para realizar el Pedido o '4' Si desea Salir: "
        )
        client_encontrado = gestor_de_clientes.buscar_por_codigo(dni_code)
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
        gestor_de_sucursal.mostrar_simplificado()
        code = negocio.intValidate(
            "\nIngrese el codigo del la Sucursal Para agregar productos: "
        )
        sucursal_encontrado = gestor_de_sucursal.buscar_por_codigo(code)
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
        gestor_de_clientes.validarListaVacia()
        and gestor_de_productos.validarListaVacia()
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
            gestor_de_productos.mostrar_simplificado()
            prod_code = negocio.intValidate(
                "Ingrese el Codigo del Producto que desee agregar: "
            )
            producto_encontrado = gestor_de_productos.buscar_por_codigo(
                prod_code)
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
                        opcion = negocio.floatValidate_neg()
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
                            gestor_de_pedidos.pedidos.append(new_pedido)
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
                            gestor_de_pedidos.pedidos.append(new_pedido)
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
        if len(gestor_de_productos.productos) == 0:
            text = "No hay productos para seleccionar, debe cargar los Productos e intentelo nuevamente"
            graphi(text)
        if len(gestor_de_clientes.clientes) == 0:
            text = "No hay Clientes para seleccionar, debe cargar los Clientes e intentelo nuevamente"
            graphi(text)


def readOrder():
    global gestor_de_pedidos
    while True:
        # simplificado
        gestor_de_pedidos.mostrar_simplificado()
        opcion = negocio.intValidate(
            "Ingrese el ID del Pedido para mostrar el Carrito del Cliente | '0' para Salir: "
        )
        order_encontrada = gestor_de_pedidos.buscar_por_codigo(opcion)
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

        buscar_producto = negocio.intValidate(
            "Ingrese el Indice del Producto que desea reemplazar | '0' Para salir: "
        )
        producto_encontrado = indexCarrito(carrito, int(buscar_producto))
        if producto_encontrado != -1:
            print(producto_encontrado)
            gestor_de_productos.mostrar_simplificado()
            buscar_nuevo_producto = negocio.intValidate(
                "Ingrese el ID del Producto nuevo: "
            )
            update_product = gestor_de_productos.buscar_por_codigo(
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
    gestor_de_pedidos.mostrar_simplificado()
    buscar_pedido = negocio.intValidate(
        "Ingrese el ID del Pedido que desea modificar: "
    )
    pedido_encontrado = gestor_de_pedidos.buscar_por_codigo(buscar_pedido)
    if pedido_encontrado:
        gestor_de_clientes.mostrar_simplificado()
        buscar_cliente = negocio.intValidate(
            "Ingrese el DNI del si lo quiere reemplazar cliente para remplazar, sino indique el anterior: "
        )
        cliente_encontrado = gestor_de_clientes.buscar_por_codigo(
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
                opcion = negocio.floatValidate_neg()
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
    gestor_de_pedidos.mostrar_simplificado()
    code = negocio.intValidate("Ingrese el ID del Pedido que desea Eliminar: ")
    pedido_encontrado = gestor_de_pedidos.buscar_por_codigo(code)
    if pedido_encontrado:
        opcion = input(f"\n\tDesea eliminar ?\n\n{pedido_encontrado}\nS/n: ")
        if opcion.lower() in ("si", "s", "y", "yes" "ye"):
            gestor_de_pedidos.pedidos.remove(pedido_encontrado)
            escribir_en_binario_pedidos()
            print(f"\n\tSe ha eliminado de la lista:\n{pedido_encontrado}")
        else:
            print("El pedido no se ha sido eliminado...")
    else:
        print("El codigo no fue encontrado!")


# Funcionalidades de Sucursal
def create_sucursal():
    global gestor_de_sucursal
    global gestor_de_productos
    pyfiglet.print_figlet(text="Crear Sucursal", colors="BLUE")
    while True:
        cod = gestor_de_sucursal.create_sucursal_cod()
        name = negocio.validateProductName()
        new_sucursal = clases.Sucursal(cod, name, [], 0, 0, 0)
        user = input(
            f"{colors.WARNING}Desea ingresar Productos a esta Sucursal ?: s/n {colors.RESET}"
        )
        if (
            user.lower() in ("s", "si", "yes", "y")
            and gestor_de_productos.validarListaVacia()
        ):
            new_sucursal_with_products = carrito_add_product(new_sucursal)
            gestor_de_sucursal.sucursales.append(new_sucursal_with_products)
        else:
            gestor_de_sucursal.sucursales.append(new_sucursal)
            escribir_en_binario_sucursales()
            print(colors.OK, "Se ha creado una nueva Sucursal", colors.RESET)
            print(new_sucursal)
        if not gestor_de_productos.validarListaVacia() and user.lower() in (
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
                     len(gestor_de_sucursal.sucursales)}) Sucursales, desea ingresar mas Sucursales ?: s/n {colors.RESET}")
        if user.lower() == "n":
            break


def add_sucursal_product():
    global gestor_de_productos
    global gestor_de_sucursal
    pyfiglet.print_figlet(text="Agregar Productos a Sucursal", colors="BLUE")
    gestor_de_sucursal.mostrar_simplificado()
    if (
        gestor_de_sucursal.validarListaVacia()
        and gestor_de_productos.validarListaVacia()
    ):
        sucursal_encontrado = buscar_sucursal_producto()
        while True:
            if not (sucursal_encontrado):
                break
            carrito_add_product(sucursal_encontrado)
    else:
        if len(gestor_de_productos.productos) == 0:
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
        gestor_de_productos.mostrar_simplificado()
        prod_code = negocio.intValidate(
            "Ingrese el Codigo del Producto que desee agregar: "
        )
        producto_encontrado = gestor_de_productos.buscar_por_codigo(prod_code)
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
        opcion = negocio.floatValidate_neg()
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


# ordenar por TOTAL


def mezclar_por_total(lista, inicio, medio, fin):
    izquierda = lista[inicio: medio + 1]
    derecha = lista[medio + 1: fin + 1]

    i = j = 0
    k = inicio

    # Mezcla las dos mitades
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i].total <= derecha[j].total:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    # Copia los elementos restantes de la mitad izquierda, si los hay
    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    # Copia los elementos restantes de la mitad derecha, si los hay
    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1


def marge_sort_total_order(lista, inicio, fin):
    if inicio < fin:
        medio = (inicio + fin) // 2  # Encuentra el punto medio
        marge_sort_total_order(lista, inicio, medio)
        marge_sort_total_order(lista, medio + 1, fin)

        mezclar_por_total(lista, inicio, medio, fin)


def ordenar_por_merge_sort_por_total():
    global gestor_de_pedidos
    lista_de_pedidos = gestor_de_pedidos.pedidos
    marge_sort_total_order(lista_de_pedidos, 0, len(lista_de_pedidos) - 1)
    print(lista_de_pedidos)


def menuProductos():
    pyfiglet.print_figlet(text="\tMenu\nProductos", colors="GREEN")
    global menu_text
    global gestor_de_productos
    while True:
        print(menu_text.product_menu_text)
        opcion = input("Escriba la opcion que desea seleccionar: ")
        opcion = opcion.lower()
        if opcion == "crear producto":
            createProduct()
        elif opcion == "modificar producto":
            if gestor_de_productos.validarListaVacia():
                update_product_menu()
            else:
                print("\n\tLa lista esta vacia no se puede modificar productos")
        elif opcion == "mostrar todo":
            if gestor_de_productos.validarListaVacia():
                gestor_de_productos.mostrar_todos()
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar productos")
        elif opcion == "eliminar producto":
            if gestor_de_productos.validarListaVacia():
                removeProduct()
            else:
                print("\n\tLa lista esta vacia no se puede eliminar productos")
        elif opcion == "salir":
            break


def update_product_menu():
    pyfiglet.print_figlet(text="\tMenu\nModificar Productos", colors="GREEN")
    global menu_text
    global gestor_de_productos
    while True:
        print(menu_text.update_product_menu_text)
        opcion = input("Escriba la opcion que desea seleccionar: ")
        opcion = opcion.lower()
        if opcion == "cambiar nombre":
            update_product_name()
        elif opcion == "cambiar costo":
            update_product_cost_price()
        elif opcion == "cambiar precio":
            update_product_price()
        elif opcion == "cambiar stock":
            update_product_stock()
        elif opcion == "cambiar todo":
            update_all_product()
        elif opcion == "atras":
            break
        else:
            print(colors.FAIL, "Opcion incorrecta, intentelo nuecamente", colors.RESET)


# menu gestor de cliente
def menuCliente():
    pyfiglet.print_figlet(text="\tMenu\nClientes", colors="GREEN")
    global menu_text
    global gestor_de_clientes
    while True:
        print(menu_text.client_menu_text)
        opcion = input("Escriba la opcion que desea seleccionar: ")
        opcion = opcion.lower()
        if opcion == "crear cliente":
            createClient()
        elif opcion == "modificar cliente":
            if gestor_de_clientes.validarListaVacia():
                updateClient()
            else:
                print("\n\tLa lista esta vacia no se puede modificar clientes")
        elif opcion == "mostrar todo":
            if gestor_de_clientes.validarListaVacia():
                gestor_de_clientes.mostrar_todos()
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar clientes")
        elif opcion == "eliminar cliente":
            if gestor_de_clientes.validarListaVacia():
                deleteClient()
            else:
                print("\n\tLa lista esta vacia no se puede eliminar clientes")
        elif opcion == "salir":
            break


# menu de gestor de Orden
def menuPedidos():
    pyfiglet.print_figlet(text="\tMenu\nPedidos", colors="YELLOW")
    global menu_text
    global gestor_de_pedidos
    while True:
        print(menu_text.pedidos_menu_text)
        opcion = input("Escriba la opcion que desea seleccionar: ")
        opcion = opcion.lower()
        if opcion == "crear pedido":
            createOrder()
        elif opcion == "modificar pedido":
            if gestor_de_pedidos.validarListaVacia():
                updateOrder()
            else:
                print("\n\tLa lista esta vacia no se puede modificar pedidos")
        elif opcion == "mostrar todo":
            if gestor_de_pedidos.validarListaVacia():
                gestor_de_pedidos.mostrar_todos()
                print(
                    colors.OK,
                    "Para mas detalles sobre el pedido, elija la opcion 'Mostrar simplificado'",
                    colors.RESET,
                )
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar pedidos")
        elif opcion == "mostrar simplificado":
            if gestor_de_pedidos.validarListaVacia():
                readOrder()
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar pedidos")
        elif opcion == "total margesort":
            if gestor_de_pedidos.validarListaVacia():
                ordenar_por_merge_sort_por_total()
                permanenciaDeArchivos()
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar pedidos")
        elif opcion == "eliminar pedido":
            if gestor_de_pedidos.validarListaVacia():
                deleteOrder()
            else:
                print("\n\tLa lista esta vacia no se puede eliminar pedidos")
        elif opcion == "salir":
            break


def mainMenu():
    menu = """
    1 - Gestión de Productos
    2 - Gestión de Clientes
    3 - Gestión de Pedidos
    4 - Salir
    """

    while True:
        # grafico ASCII
        pyfiglet.print_figlet(
            text="La Despensita\nby Franco Monzon", colors="RED")
        # Imprimir Menu
        print(menu)
        opcion = negocio.intValidate(
            "A continuacion ingrese el numero de la opcion que desea realizar: "
        )
        if opcion == 1:
            menuProductos()
        if opcion == 2:
            menuCliente()
        if opcion == 3:
            menuPedidos()
        if opcion == 4:
            pyfiglet.print_figlet(
                text="Gracias !!! \nVuelva Pronto", font="slant", colors="BLUE"
            )
            break


permanenciaDeArchivos()
mainMenu()
