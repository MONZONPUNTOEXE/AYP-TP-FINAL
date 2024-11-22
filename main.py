from pickle import dumps, load
import pyfiglet
import os


class Producto:
    def __init__(self, cod, name, price):
        self.ean_code = int(cod)
        self.product_name = name
        self.product_price = float(price)

    def __repr__(self) -> str:
        return (
            f"══════════════════════════════════════════\n"
            f"          Producto: {self.product_name}\n"
            f"══════════════════════════════════════════\n"
            f"  Ean Code:      {self.ean_code}\n"
            f"  Precio:       ${self.product_price}\n"
            f"══════════════════════════════════════════\n"
        )

    def resumenProducto(self):
        return f"Codigo Ean: {self.ean_code} - Nombre del Producto: {self.product_name}"


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
    def __init__(self, cod: int, product_orders: list, date: str, charge: float):
        self.id_order = int(cod)
        self.list_orders = product_orders
        self.order_date = date
        self.extra_charge = float(charge)

    def __repr__(self) -> str:
        return (
            f"══════════════════════════════════════════\n"
            f"          ID de la Orden: {self.id_order}\n"
            f"══════════════════════════════════════════\n"
            f" Fecha de Orden:  {self.order_date}\n"
            f" Cargos:          {self.extra_charge}%\n"
            f" Lista de Orden:  {self.list_orders}\n"
            f"══════════════════════════════════════════\n"
        )

    def resumenOrden(self):
        return f"ID: {self.id_order} - Fecha: {self.order_date} - Lista: {self.list_orders}"


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
            return "No hay productos Cargados actualmente"

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
                print(producto)
        else:
            print("No hay productos cargados hasta el momento")

    def mostrar_simplificado(self):
        if self.productos:
            for producto in self.productos:
                print(producto.resumenProducto())
        else:
            print("La lista esta Vacia")

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for producto in self.productos:
            if producto.ean_code == codigo_a_buscar:
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
            return "No hay clientes cargados actualmente"

    def validarListaVacia(self):
        if len(self.clientes) > 0:
            return True
        else:
            return None

    def eliminar_cliente(self, cliente_a_eliminar: Cliente):
        self.clientes.remove(cliente_a_eliminar)

    def mostrar_todos(self):
        if self.clientes:
            print("Listando los Clientes disponibles")
            for cliente in self.clientes:
                print(cliente)
        else:
            print("No hay Clientes cargados hasta el momento")

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
            return "No hay pedidos cargados actualmente"

    def eliminar_pedido(self, pedido_a_eliminar: Order):
        self.pedidos.remove(pedido_a_eliminar)

    def mostrar_todos(self):
        if self.pedidos:
            print("Listando los Pedidos disponibles")
            for pedido in self.pedidos:
                print(pedido)
        else:
            print("No hay pedidos cargados hasta el momento")

    def mostrar_simplificado(self):
        if self.pedidos:
            for pedido in self.pedidos:
                print(pedido.resumenOrden())
        else:
            print("La lista esta Vacia")

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for pedido in self.pedidos:
            if pedido.id_order == codigo_a_buscar:
                return pedido
        return None


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
            print("'clientes.bin' Se ha cargado exitosamente.")
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
            print("Debe ingresar un numero entero! ")
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


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def validateName():
    while True:
        name = input("Ingrese el nombre del producto :")
        if len(name) < 61:
            return name
        else:
            print("El nombre debe tener menos de 60 caracteres")


def DNIValidate() -> int:
    dni = intValidate("Ingrese su DNI, sin coma ni puntos: ")
    while len(str(dni)) != 8:
        print("El DNI ingresado no es valido, Intentelo nuevamente!")
        dni = intValidate("Ingrese su DNI, sin coma ni puntos: ")
    print(f"Su DNI ({dni}) se guardo satisfactoriamente!")
    return int(dni)


# preba de validacion
# opcion = floatValidate("Ingrese su peso: ")
# print(opcion)
# DNIValidate()
# funciones de Producto --------------


# Create Producto
def createProduct():
    global gestor_de_productos
    while True:
        cod = gestor_de_productos.obtener_nuevo_codigo()
        name = validateName()
        price = floatValidate("Ingrese el precio del Producto : ")
        new_product = Producto(cod, name, price)
        gestor_de_productos.productos.append(new_product)
        escribir_en_binario_productos()
        print("Se ha creado un nuevo Producto")
        print(new_product)
        user = input(f"hay un total de ({
                     len(gestor_de_productos.productos)}) Productos desea ingresar mas ?: s/n ")
        if user.lower() == "n":
            break


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
        cod = DNIValidate()
        name = input("Ingrese el nombre del Cliente: ")
        print("Ingrese la fecha de Nacimiento en este formato DD/MM/AAAA")
        date = input("DIA/MES/ANIO: ")
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
        dni_confirm = input("Desea cambiar el DNI del Cliente ? S/n ")
        if dni_confirm.lower() in ("no", "n"):
            nuevo_id = ""
        else:
            nuevo_id = intValidate("Ingrese el nuevo DNI: ")
        nuevo_fecha = input(
            "Ingrese la Fecha de Nacimiento DD/MM/AAAA - (Enter para dejar actual): "
        )

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
    code = intValidate("Ingrese el codigo del Cliente que desea Eliminar: ")
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


# menu de Producto
product_menu_text = """
------------------- Menu Productos ---------------------------

crear producto - Para crear un producto nuevo
modificar producto - Para modificar un producto
mostrar todo - Para listar todos los productos cargados en memoria
eliminar producto - Para eliminar un producto por codigo
mostrar binario - Para mostrar desde archivo binario

salir - Para Salir del programa
"""

# menu de Cliente
client_menu_text = """
------------------- Menu Cliente ---------------------------

crear cliente - Para crear un cliente nuevo
modificar cliente - Para modificar un cliente
mostrar todo - Para listar todos los clientes cargados en memoria
eliminar cliente - Para eliminar un cliente por codigo
mostrar binario - Para mostrar desde archivo binario

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
        elif opcion == "mostrar binario":
            if gestor_de_productos.validarListaVacia():
                pass
            else:
                print("\n\tLa lista esta vacia no se puede mostrar binarios")
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
        elif opcion == "mostrar binario":
            if gestor_de_clientes.validarListaVacia():
                pass
            else:
                print("\n\tLa lista esta vacia no se puede mostrar binarios")
        elif opcion == "salir":
            break


# menu de gestor de Orden


def mainMenu():
    menu = """
    1 - Gestión de Productos
    2 - Gestión de Clientes
    3 - Gestión de Pedidos (sin realizar)
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
            pass
        if opcion == 4:
            pyfiglet.print_figlet(
                text="Gracias !!! \nVuelva Pronto", font="slant", colors="BLUE"
            )
            break


permanenciaDeArchivos()
mainMenu()
