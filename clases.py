import re
import time
from datetime import datetime

from negocio import floatValidate_neg


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
        self.product_charge = 0
        self.product_price = float(price)
        self.stock = int(stock)
        self.date = Fecha()
        self.date_edit = Fecha()
        self.date_product_edit = False

    def __repr__(self) -> str:
        if self.date_product_edit:
            return (
                f"══════════════════════════════════════════\n"
                f"          Producto: {self.product_name}\n"
                f"══════════════════════════════════════════\n"
                f"  Ref Code:             {self.ref_code}\n"
                f"  Ingreso:              {self.date}\n"
                f"  Ultima Modificacion:  {self.date_edit}\n"
                f"  Costo:                ${self.product_cost_price}\n"
                f"  Cargo:                {self.product_charge}%\n"
                f"  Precio:               ${self.product_price}\n"
                f"  Stock:                ({self.stock})\n"
                f"══════════════════════════════════════════\n"
            )
        else:
            return (
                f"══════════════════════════════════════════\n"
                f"          Producto: {self.product_name}\n"
                f"══════════════════════════════════════════\n"
                f"  Ref Code:     {self.ref_code}\n"
                f"  Ingreso:      {self.date}\n"
                f"  Costo:        ${self.product_cost_price}\n"
                f"  Cargo:        ${self.product_charge}%\n"
                f"  Precio:       ${self.product_price}\n"
                f"  Stock:       ({self.stock})\n"
                f"══════════════════════════════════════════\n"
            )

    def resumenProducto(self):
        if self.date_product_edit:
            return f"{self.ref_code} - {self.product_name} - Costo: ${self.product_cost_price} - Cargo: {self.product_charge}% - Precio: ${self.product_price} Stock: ({self.stock}\nIngreso: {self.date} | Ult. Modificacion: {self.date_edit}\n\t--------------------"
        else:
            return f"{self.ref_code} - {self.product_name} - Costo: ${self.product_cost_price} - Cargo: {self.product_charge}% - Precio: ${self.product_price} Stock: ({self.stock}) Fecha: {self.date}\n\t--------------------"

    def crear_precio_final(self):
        if self.product_charge:
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
                    subtotal = self.product_price
                    total = cargo + subtotal
                    print(f"\n\t- El Subtotal es de ${subtotal}")
                    print(f"\t- El Cargo es de {opcion}%")
                    print(f"\t- El Total es de: ${total}")
                    self.product_price = float(total)
                    self.product_charge = int(0)
                else:
                    subtotal = self.product_price
                    cargo = subtotal * opcion / 100
                    total = cargo + subtotal
                    print(f"- El Subtotal es de {subtotal}")
                    print(f"- El Cargo es de {opcion}%")
                    print(f"- El Total es de: ${total}")
                    self.product_charge = float(opcion)
                    self.product_price = float(total)
        else:
            print(colors.FAIL, "Algo ha fallado intentelo nuevamente", colors.RESET)


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


class Inventory:
    def __init__(
        self,
        cod: int,
        stock: int,
    ):
        self.id_sucursal = int(cod)
        self.sucursal_name = sucursal
        self.product_list = product_list
        self.order_date = Fecha()
        self.fecha_edit = Fecha()
        self.sucursal_date_edit = False
        self.charge = charge
        self.subtotal = float(subtotal)
        self.total = float(total)
        # --------------
        self.len_product_list = len(product_list)

    def __repr__(self) -> str:
        if self.sucursal_date_edit:
            return (
                f"══════════════════════════════════════════\n"
                f"          Sucursal: {self.sucursal_name}\n"
                f"══════════════════════════════════════════\n"
                f" ID :                  {self.id_sucursal}\n"
                f" Ingreso de Sucursal:  {self.order_date}\n"
                f" Ultima Modificacion:  {self.fecha_edit}\n"
                f" Subtotal:             {self.subtotal}\n"
                f" Total:                {self.total}\n"
                f" Productos en Sucursal: ({self.len_product_list})\n"
                f"══════════════════════════════════════════\n"
            )
        else:
            return (
                f"══════════════════════════════════════════\n"
                f"          Sucursal: {self.sucursal_name}\n"
                f"══════════════════════════════════════════\n"
                f" ID :                  {self.id_sucursal}\n"
                f" Ingreso de Sucursal:  {self.order_date}\n"
                f" Total:                {self.total}\n"
                f" Productos en Carrito: ({self.len_product_list})\n"
                f"══════════════════════════════════════════\n"
            )

    def view_product_list(self):
        if self.sucursal_date_edit:
            print("Productos de la Sucursal")
            print(
                f"ID: {
                    self.id_sucursal} - Nombre: {self.sucursal_name} - Fecha: {self.order_date} - Ult. Modificacion: {self.fecha_edit}\nSubtotal: ${self.subtotal} - TOTAL: ${self.total}\n\t -----------------"
            )
            for producto in self.product_list:
                print(f"\t- {producto.product_name} ${producto.product_price}")
        else:
            print("Productos de la Sucursal")
            print(
                f"ID: {
                    self.id_sucursal} - Nombre: {self.sucursal_name} - Fecha: {self.order_date}\nSubtotal: ${self.subtotal} - TOTAL: ${self.total}\n\t -----------------"
            )
            for producto in self.product_list:
                print(f"\t- {producto.product_name} ${producto.product_price}")

    def resumen_sucursal(self):
        return f"ID: {
            self.id_sucursal} - Fecha: {self.order_date}"


class Sucursal:
    def __init__(
        self,
        cod: int,
        sucursal: str,
        product_list: list,
        charge: float,
        subtotal: float,
        total: float,
    ):
        self.id_sucursal = int(cod)
        self.sucursal_name = sucursal
        self.product_list = product_list
        self.order_date = Fecha()
        self.fecha_edit = Fecha()
        self.sucursal_date_edit = False
        self.charge = charge
        self.subtotal = float(subtotal)
        self.total = float(total)
        # --------------
        self.len_product_list = len(product_list)

    def __repr__(self) -> str:
        if self.sucursal_date_edit:
            return (
                f"══════════════════════════════════════════\n"
                f"          Sucursal: {self.sucursal_name}\n"
                f"══════════════════════════════════════════\n"
                f" ID :                  {self.id_sucursal}\n"
                f" Ingreso de Sucursal:  {self.order_date}\n"
                f" Ultima Modificacion:  {self.fecha_edit}\n"
                f" Subtotal:             {self.subtotal}\n"
                f" Total:                {self.total}\n"
                f" Productos en Sucursal: ({self.len_product_list})\n"
                f"══════════════════════════════════════════\n"
            )
        else:
            return (
                f"══════════════════════════════════════════\n"
                f"          Sucursal: {self.sucursal_name}\n"
                f"══════════════════════════════════════════\n"
                f" ID :                  {self.id_sucursal}\n"
                f" Ingreso de Sucursal:  {self.order_date}\n"
                f" Total:                {self.total}\n"
                f" Productos en Carrito: ({self.len_product_list})\n"
                f"══════════════════════════════════════════\n"
            )

    def view_product_list(self):
        if self.sucursal_date_edit:
            print("Productos de la Sucursal")
            print(
                f"ID: {
                    self.id_sucursal} - Nombre: {self.sucursal_name} - Fecha: {self.order_date} - Ult. Modificacion: {self.fecha_edit}\nSubtotal: ${self.subtotal} - TOTAL: ${self.total}\n\t -----------------"
            )
            for producto in self.product_list:
                print(f"\t- {producto.product_name} ${producto.product_price}")
        else:
            print("Productos de la Sucursal")
            print(
                f"ID: {
                    self.id_sucursal} - Nombre: {self.sucursal_name} - Fecha: {self.order_date}\nSubtotal: ${self.subtotal} - TOTAL: ${self.total}\n\t -----------------"
            )
            for producto in self.product_list:
                print(f"\t- {producto.product_name} ${producto.product_price}")

    def resumen_sucursal(self):
        return f"ID: {
            self.id_sucursal} - Fecha: {self.order_date}"


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


class gestorSucursal:
    def __init__(self) -> None:
        self.sucursales: list[Sucursal] = []

    def __str__(self) -> str:
        if len(self.sucursales) > 0:
            return str(self.sucursales)
        else:
            return colors.WARNING + "No hay sucursales actualmente" + colors.RESET

    def validarListaVacia(self):
        if len(self.sucursales) > 0:
            return True
        else:
            return None

    def mostrar_todos(self):
        if self.sucursales:
            print("Listando las Sucursales disponibles")
            for sucursal in self.sucursales:
                print(sucursal)
        else:
            print(
                colors.WARNING
                + "No hay Sucursales cargados hasta el momento"
                + colors.RESET
            )

    def mostrar_simplificado(self):
        if self.sucursales:
            for sucursal in self.sucursales:
                print(sucursal.resumen_sucursal())
        else:
            print(colors.WARNING + "La lista esta Vacia" + colors.RESET)

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for sucursal in self.sucursales:
            if sucursal.id_sucursal == codigo_a_buscar:
                return sucursal
        return None

    def create_sucursal_cod(self):
        return len(self.sucursales) + 1


class Fecha:
    def __init__(self, fecha_str: str = None):
        if not fecha_str:
            hoy = datetime.now()
            hora = time.localtime()
            self.hora = time.strftime("%H:%M:%S", hora)
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
        return f"{self.dia}/{self.mes}/{self.anio} {self.hora}"


# Creacion de los objetos "Gestores de Entidades" -----------------------------
gestor_de_productos = gestorProductos()
gestor_de_clientes = gestorClientes()
gestor_de_pedidos = orderGestor()
gestor_de_sucursal = gestorSucursal()
