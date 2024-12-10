from pickle import dumps, load
import pyfiglet
import os
import re
from datetime import datetime


class colors:
    OK = "\033[92m"  # GREEN
    WARNING = "\033[93m"  # YELLOW
    FAIL = "\033[91m"  # RED
    RESET = "\033[0m"  # RESET COLOR


class Producto:
    def __init__(self, cod, name: str, cost_price: float, price: float, stock: int):
        self.ref_code = int(cod)
        self.product_name = name
        self.product_cost_price = float(cost_price)
        self.product_price = float(price)
        self.stock = int(stock)

    def __repr__(self) -> str:
        return (
            f"══════════════════════════════════════════\n"
            f"          Producto: {self.product_name}\n"
            f"══════════════════════════════════════════\n"
            f"  Ref Code:      {self.ref_code}\n"
            f"  Costo:        ${self.product_cost_price}\n"
            f"  Precio:       ${self.product_price}\n"
            f"  Stock:         ({self.stock})\n"
            f"══════════════════════════════════════════\n"
        )

    def resumenProducto(self):
        return f"{self.ref_code} - {self.product_name} - ${self.product_cost_price} ${self.product_price} Stock: ({self.stock})"


# Clients Class
class Cliente:
    def __init__(self, cod, surname_name, fecha):
        self.dni = int(cod)
        self.surname_name = surname_name
        self.fecha_nacimiento = fecha

    def __repr__(self) -> str:
        return (
            f"══════════════════════════════════════════\n"
            f"          Cliente: {self.surname_name}\n"
            f"══════════════════════════════════════════\n"
            f"  DNI:                    {self.dni}\n"
            f"  Fecha de Nacimiento:    {self.fecha_nacimiento}\n"
            f"══════════════════════════════════════════\n"
        )

    def resumenClient(self):
        return f"DNI: {self.dni} - Nombre y Apellido: {self.surname_name}"


class Order:
    def __init__(
        self,
        cod: int,
        customer: str,
        product_list: list,
        charge: float,
        subtotal: float,
        total: float,
    ):
        self.id_order = int(cod)
        self.customer = customer
        self.product_list = product_list
        self.order_date = Fecha()
        self.fecha_edit = Fecha()
        self.order_date_edit = False
        self.extra_charge = float(charge)
        self.subtotal = float(subtotal)
        self.total = float(total)
        # --------------
        self.len_product_list = len(product_list)

    def __repr__(self) -> str:
        if self.order_date_edit:
            return (
                f"══════════════════════════════════════════\n"
                f"          ID del Pedido: {self.id_order}\n"
                f"══════════════════════════════════════════\n"
                f" Fecha del Pedido:     {self.order_date}\n"
                f" Ultima Modificacion:  {self.fecha_edit}\n"
                f" Cliente:              {self.customer}\n"
                f" Subtotal:             {self.subtotal}\n"
                f" Cargos:               {self.extra_charge}%\n"
                f" Total:                {self.total}\n"
                f" Productos en Carrito: ({self.len_product_list})\n"
                f"══════════════════════════════════════════\n"
            )
        else:
            return (
                f"══════════════════════════════════════════\n"
                f"          ID del Pedido: {self.id_order}\n"
                f"══════════════════════════════════════════\n"
                f" Fecha del Pedido:  {self.order_date}\n"
                f" Cliente:         {self.customer}\n"
                f" Subtotal:        {self.subtotal}\n"
                f" Cargos:          {self.extra_charge}%\n"
                f" Total:           {self.total}\n"
                f" Productos en Carrito: ({self.len_product_list})\n"
                f"══════════════════════════════════════════\n"
            )

    def mostrarCarritoOrder(self):
        if self.order_date_edit:
            print("Carrito del Cliente")
            print(
                f"DNI: {
                    self.id_order} - Fecha: {self.order_date} - Ult. Modificacion: {self.fecha_edit} - Cliente: {self.customer} - Subtotal: ${self.subtotal} - Cargo: - {self.extra_charge}% - TOTAL: ${self.total} :"
            )
            for producto in self.product_list:
                print(f"\t- {producto.product_name} ${producto.product_price}")
        else:
            print("Carrito del Cliente")
            print(
                f"DNI: {
                    self.id_order} - Fecha: {self.order_date} - Cliente: {self.customer} - Subtotal: ${self.subtotal} - Cargo: - {self.extra_charge}% - TOTAL: ${self.total} :"
            )
            for producto in self.product_list:
                print(f"\t- {producto.product_name} ${producto.product_price}")

    def resumenOrden(self):
        return f"ID: {
            self.id_order} - Fecha: {self.order_date} - Cliente: {self.customer}"


# Subrrayado de texto
def graphi(text):
    width = len(text)
    print("-" * width)
    print(text)


# Gestores de entidades
class gestorProductos:
    def __init__(self):
        self.productos: list[Producto] = []

    def __str__(self):
        if len(self.productos) > 0:
            return str(self.productos)
        else:
            return (
                colors.WARNING + "No hay productos Cargados actualmente" + colors.RESET
            )

    def validarListaVacia(self):
        if len(self.productos) > 0:
            return True
        else:
            return None

    def eliminar_producto(self, producto_a_eliminar: Producto):
        self.productos.remove(producto_a_eliminar)

    def mostrar_todos(self):
        if self.productos:
            print("Listando los Productos disponibles")
            for producto in self.productos:
                print(colors.OK, producto, colors.RESET)
        else:
            print(
                colors.FAIL, "No hay productos cargados hasta el momento", colors.RESET
            )

    def mostrar_simplificado(self):
        if self.productos:
            for producto in self.productos:
                print(producto.resumenProducto())
        else:
            print("La lista esta Vacia")

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for producto in self.productos:
            if producto.ref_code == codigo_a_buscar:
                return producto
        return None

    def obtener_nuevo_codigo(self):
        return len(self.productos) + 1


class gestorClientes:
    def __init__(self) -> None:
        self.clientes: list[Cliente] = []

    def __str__(self):
        if len(self.clientes) > 0:
            return str(self.clientes)
        else:
            return (
                colors.WARNING + "No hay clientes cargados actualmente" + colors.RESET
            )

    def validarListaVacia(self):
        if len(self.clientes) > 0:
            return True
        else:
            return None

    def eliminar_cliente(self, cliente_a_eliminar: Cliente):
        self.clientes.remove(cliente_a_eliminar)

    def _es_fecha_nacimiento_valida(self, fecha_str: str) -> bool:
        try:
            Fecha(fecha_str)
            return True
        except ValueError:
            return False

    def _pedir_fecha_nacimiento_valida(self):
        fecha_nacimiento = "NO_VALIDA"
        while not self._es_fecha_nacimiento_valida(fecha_nacimiento):
            fecha_nacimiento = input(
                "Ingrese la fecha de nacimiento del Cliente (dd/mm/aaaa): "
            )
            if not self._es_fecha_nacimiento_valida(fecha_nacimiento):
                print("Formato de fecha no válido. Debe ser DIA/MES/ANIO (dd/mm/aaaa)")
        return Fecha(fecha_nacimiento)

    def mostrar_todos(self):
        if self.clientes:
            print("Listando los Clientes disponibles")
            for cliente in self.clientes:
                print(colors.OK, cliente, colors.RESET)
        else:
            print(
                colors.WARNING
                + "No hay Clientes cargados hasta el momento"
                + colors.RESET
            )

    def mostrar_simplificado(self):
        if self.clientes:
            for cliente in self.clientes:
                print(cliente.resumenClient())
        else:
            print("La lista esta Vacia")

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for cliente in self.clientes:
            if cliente.dni == codigo_a_buscar:
                return cliente
        return None


class orderGestor:
    def __init__(self) -> None:
        self.pedidos: list[Order] = []

    def __str__(self) -> str:
        if len(self.pedidos) > 0:
            return str(self.pedidos)
        else:
            return colors.WARNING + "No hay pedidos cargados actualmente" + colors.RESET

    def validarListaVacia(self):
        if len(self.pedidos) > 0:
            return True
        else:
            return None

    def mostrar_todos(self):
        if self.pedidos:
            print("Listando los Pedidos disponibles")
            for pedido in self.pedidos:
                print(pedido)
        else:
            print(
                colors.WARNING
                + "No hay pedidos cargados hasta el momento"
                + colors.RESET
            )

    def mostrar_simplificado(self):
        if self.pedidos:
            for pedido in self.pedidos:
                print(pedido.resumenOrden())
        else:
            print(colors.WARNING + "La lista esta Vacia" + colors.RESET)

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for pedido in self.pedidos:
            if pedido.id_order == codigo_a_buscar:
                return pedido
        return None

    def create_order_cod(self):
        return len(self.pedidos) + 1


class Fecha:
    def __init__(self, fecha_str: str = None):
        if not fecha_str:
            hoy = datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            # validar formato de fecha dd/mm/aaaa con expresiones regulres
            if not self.es_fecha_valida(fecha_str):
                raise ValueError(
                    colors.FAIL
                    + "Formato de fecha no válido. Debe ser dd/mm/aaaa"
                    + colors.RESET
                )
            partes = str(fecha_str).split("/")
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def es_fecha_valida(self, fecha: str):
        patron = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        return re.match(patron, fecha)

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anio}"


# Creacion de los objetos "Gestores de Entidades" -----------------------------
gestor_de_productos = gestorProductos()
gestor_de_clientes = gestorClientes()
gestor_de_pedidos = orderGestor()


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


# --------------------- Validaciones -------------------------------------
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


def validateProductName() -> str:
    while True:
        name = input("Ingrese el nombre del Ptroducto : ")
        if len(name) < 51:
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


# preba de validacion
# opcion = floatValidate("Ingrese su peso: ")
# print(opcion)
# dniValidate()
# funciones de Producto --------------


# Create Producto
def createProduct():
    global gestor_de_productos
    while True:
        cod = gestor_de_productos.obtener_nuevo_codigo()
        name = validateProductName()
        cost_price = floatValidate("Ingrese el costo del Producto : ")
        price = floatValidate("Ingrese el precio de venta del Producto : ")
        stock = intValidate("Ingrese el Stock del Producto: ")
        new_product = Producto(cod, name, cost_price, price, stock)
        gestor_de_productos.productos.append(new_product)
        escribir_en_binario_productos()
        print(colors.OK, "Se ha creado un nuevo Producto", colors.RESET)
        print(new_product)
        user = input(f"{colors.WARNING}hay un total de ({
                     len(gestor_de_productos.productos)}) Productos desea ingresar mas ?: s/n {colors.RESET}")
        if user.lower() == "n":
            break


def updateStock(product, update_stock, entrada=False, salida=False):
    if entrada:
        product += update_stock
        return product
    elif salida:
        # Verifica los valores de product y update_stock
        print(f"Producto: {product}, Stock a actualizar: {update_stock}")
        if product < update_stock:
            print(f"El stock actual es ({product})")
            print(f"Y quiere egresar ({update_stock})")
            print("Su Stock es menor al monto que desea egresar")
            print("Intentelo nuevamente")
            return None
        else:
            product -= update_stock
            return product
    else:
        print(f"{colors.FAIL} Hubo un error, no hay entrada ni salida verdadera {
              colors.RESET}")


alfajores = 100
empanadas = 80
ciruelas = 560

ingresan_alfajores = 47
ingresan_empanadas = 560
ingresan_ciruelas = 570

alfajores = updateStock(alfajores, ingresan_alfajores, entrada=True)
empanadas = updateStock(empanadas, ingresan_empanadas, entrada=True)
ciruelas = updateStock(ciruelas, ingresan_ciruelas, entrada=False, salida=True)

print("Ingresan")
print(alfajores)
print(empanadas)
print(ciruelas)

print("Egresan")
ingresan_alfajores = -5
ingresan_empanadas = -650
ingresan_ciruelas = 650

alfajores = updateStock(alfajores, ingresan_alfajores)
empanadas = updateStock(empanadas, ingresan_empanadas)
ciruelas = updateStock(ciruelas, ingresan_ciruelas)

print(alfajores)
print(empanadas)
print(ciruelas)


def manualUpdateStock():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = intValidate(
        "Ingrese el codigo del Producto que desea modificar su stock: "
    )
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        nuevo_nombre = input("Ingrese el nuevo nombre - (Enter para dejar el actual): ")
        precio_confirm = input("Desea cambiar el Precio del Producto ? S/n ")
        if precio_confirm.lower() in ("no", "n"):
            nuevo_precio = ""


# Update Producto
def modificarProducto():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = intValidate("Ingrese el codigo del Producto que desea modificar: ")
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        nuevo_nombre = input("Ingrese el nuevo nombre - (Enter para dejar el actual): ")
        precio_confirm = input("Desea cambiar el Precio del Producto ? S/n ")
        if precio_confirm.lower() in ("no", "n"):
            nuevo_precio = ""
        else:
            nuevo_precio = floatValidate("Ingrese el nuevo precio: ")
        # cambios anteriores
        nombre_sin_cambio = producto_encontrado.product_name
        precio_sin_cambio = producto_encontrado.product_price

        text_sin_cambios = "Sin aplicar Cambios"
        graphi(text_sin_cambios)
        print(producto_encontrado)

        if nuevo_nombre:
            producto_encontrado.product_name = nuevo_nombre
        if nuevo_precio:
            producto_encontrado.product_price = float(nuevo_precio)

        text_con_cambios = "Aplicando los cambios... "
        graphi(text_con_cambios)
        print(producto_encontrado)

        decidir_cambios = input("Desea guardar los cambios ? - (Si/no)")
        if decidir_cambios.lower() in ("no", "n"):
            producto_encontrado.product_name = nombre_sin_cambio
            producto_encontrado.product_price = float(precio_sin_cambio)
            print("El Producto no se ha actualizado")
            escribir_en_binario_productos()
        else:
            print("El Producto se ha actualizado correctamente")
            escribir_en_binario_productos()
            print(producto_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


# Delete Producto
def removeProduct():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    code = intValidate("Ingrese el codigo del Producto que desea Eliminar: ")
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


# funciones de Cliente ---------------


# create Cliente
def createClient():
    global gestor_de_clientes
    while True:
        cod = dniValidate()
        name = validateClientName()
        print("Ingrese la fecha de Nacimiento en este formato DD/MM/AAAA")
        date = gestor_de_clientes._pedir_fecha_nacimiento_valida()
        new_client = Cliente(cod, name, date)
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
    client_code = intValidate("Ingrese el DNI del Cliente que desea modificar: ")
    client_encontrado = gestor_de_clientes.buscar_por_codigo(client_code)
    if client_encontrado:
        nuevo_nombre = input("Ingrese el nuevo nombre - (Enter para dejar el actual): ")
        dni_confirm = input(
            "Desea cambiar el DNI y Fecha de Nacimiento del Cliente ? S/n "
        )
        if dni_confirm.lower() in ("no", "n"):
            nuevo_id = ""
        else:
            nuevo_id = dniValidate()
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
    code = intValidate("Ingrese el DNI del Cliente que desea Eliminar: ")
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
        dni_code = intValidate(
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
            prod_code = intValidate(
                "Ingrese el Codigo del Producto que desee agregar: "
            )
            producto_encontrado = gestor_de_productos.buscar_por_codigo(prod_code)
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
                            new_pedido = Order(
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
                            new_pedido = Order(
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
        opcion = intValidate(
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

        buscar_producto = intValidate(
            "Ingrese el Indice del Producto que desea reemplazar | '0' Para salir: "
        )
        producto_encontrado = indexCarrito(carrito, int(buscar_producto))
        if producto_encontrado != -1:
            print(producto_encontrado)
            gestor_de_productos.mostrar_simplificado()
            buscar_nuevo_producto = intValidate("Ingrese el ID del Producto nuevo: ")
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
    buscar_pedido = intValidate("Ingrese el ID del Pedido que desea modificar: ")
    pedido_encontrado = gestor_de_pedidos.buscar_por_codigo(buscar_pedido)
    if pedido_encontrado:
        gestor_de_clientes.mostrar_simplificado()
        buscar_cliente = intValidate(
            "Ingrese el DNI del si lo quiere reemplazar cliente para remplazar, sino indique el anterior: "
        )
        cliente_encontrado = gestor_de_clientes.buscar_por_codigo(buscar_cliente)
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
                    fecha_modificada = Fecha()

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
                    fecha_modificada = Fecha()

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
    code = intValidate("Ingrese el ID del Pedido que desea Eliminar: ")
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


# ordenar por TOTAL
def mezclar_por_total(lista, inicio, medio, fin):
    izquierda = lista[inicio : medio + 1]
    derecha = lista[medio + 1 : fin + 1]

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


# menu de Producto
product_menu_text = """
------------------- Menu Productos ---------------------------

crear producto - Para crear un producto nuevo
modificar producto - Para modificar un producto
mostrar todo - Para listar todos los productos
eliminar producto - Para eliminar un producto por codigo

salir - Para Salir del programa
"""

# menu de Cliente
client_menu_text = """
------------------- Menu Cliente ---------------------------

crear cliente - Para crear un cliente nuevo
modificar cliente - Para modificar un cliente
mostrar todo - Para listar todos los clientes
eliminar cliente - Para eliminar un cliente por codigo

salir - Para Salir del programa
"""

# menu de Pedidos
pedidos_menu_text = """
------------------- Menu Pedidos ---------------------------

crear pedido - Para crear un pedido nuevo
modificar pedido - Para modificar un pedido
total margesort - Mostrar totales con ordenamiento MARGE SORT
mostrar todo - Para listar todos los pedidos
mostrar simplificado - Para mas detalles de los pedidos
eliminar pedido - Para eliminar un pedido por codigo

salir - Para Salir del programa
"""


def menuProductos():
    pyfiglet.print_figlet(text="\tMenu\nProductos", colors="GREEN")
    global product_menu_text
    global gestor_de_productos
    while True:
        print(product_menu_text)
        opcion = input("Escriba la opcion que desea seleccionar: ")
        opcion = opcion.lower()
        if opcion == "crear producto":
            createProduct()
        elif opcion == "modificar producto":
            if gestor_de_productos.validarListaVacia():
                modificarProducto()
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


# menu gestor de cliente
def menuCliente():
    pyfiglet.print_figlet(text="\tMenu\nClientes", colors="GREEN")
    global client_menu_text
    global gestor_de_clientes
    while True:
        print(client_menu_text)
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
    global pedidos_menu_text
    global gestor_de_pedidos
    while True:
        print(pedidos_menu_text)
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
        pyfiglet.print_figlet(text="La Despensita\nby Franco Monzon", colors="RED")
        # Imprimir Menu
        print(menu)
        opcion = intValidate(
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
