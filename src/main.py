# external library
import pyfiglet
from src.clases.gestor_pedidos import GestorPedidos
import utils

from src.negocio import (
    gestor_productos,
    gestor_clientes,
    gestor_pedidos,
    gestor_sucursales,
)

# Creacion de los objetos "Gestores de Entidades" -----------------------------
gestor_de_productos = gestor_productos.gestorProductos()
gestor_de_clientes = gestor_clientes.GestorClientes()
gestor_de_pedidos = gestor_pedidos.GestorPedidos()
gestor_de_sucursal = gestor_sucursales.GestorSucursales()


def menuProductos():
    pyfiglet.print_figlet(text="\tMenu\nProductos", colors="GREEN")
    global menu_text
    global gestor_de_productos
    while True:
        print(utils.product_menu_text)
        opcion = input("Escriba la opcion que desea seleccionar: ")
        opcion = opcion.lower()
        if opcion == "crear producto":
            negocio.createProduct()
        elif opcion == "modificar producto":
            if clases.gestor_de_productos.validarListaVacia():
                update_product_menu()
            else:
                print("\n\tLa lista esta vacia no se puede modificar productos")
        elif opcion == "mostrar todo":
            if clases.gestor_de_productos.validarListaVacia():
                clases.gestor_de_productos.mostrar_todos()
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar productos")
        elif opcion == "eliminar producto":
            if clases.gestor_de_productos.validarListaVacia():
                negocio.removeProduct()
            else:
                print("\n\tLa lista esta vacia no se puede eliminar productos")
        elif opcion == "salir":
            break


def update_product_menu():
    pyfiglet.print_figlet(text="\tMenu\nModificar Productos", colors="GREEN")
    global menu_text
    global gestor_de_productos
    while True:
        print(utils.update_product_menu_text)
        opcion = input("Escriba la opcion que desea seleccionar: ")
        opcion = opcion.lower()
        if opcion == "cambiar nombre":
            negocio.update_product_name()
        elif opcion == "cambiar costo":
            negocio.update_product_cost_price()
        elif opcion == "cambiar precio":
            negocio.update_product_price()
        elif opcion == "cambiar stock":
            negocio.update_product_stock()
        elif opcion == "cambiar todo":
            negocio.update_all_product()
        elif opcion == "atras":
            break
        else:
            print(
                colors.FAIL,
                "Opcion incorrecta, intentelo nuecamente",
                colors.RESET,
            )


# menu gestor de cliente
def menuCliente():
    pyfiglet.print_figlet(text="\tMenu\nClientes", colors="GREEN")
    global utils
    global gestor_de_clientes
    while True:
        print(utils.client_menu_text)
        opcion = input("Escriba la opcion que desea seleccionar: ")
        opcion = opcion.lower()
        if opcion == "crear cliente":
            negocio.createClient()
        elif opcion == "modificar cliente":
            if clases.gestor_de_clientes.validarListaVacia():
                negocio.updateClient()
            else:
                print("\n\tLa lista esta vacia no se puede modificar clientes")
        elif opcion == "mostrar todo":
            if clases.gestor_de_clientes.validarListaVacia():
                clases.gestor_de_clientes.mostrar_todos()
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar clientes")
        elif opcion == "eliminar cliente":
            if clases.gestor_de_clientes.validarListaVacia():
                negocio.deleteClient()
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
        print(utils.pedidos_menu_text)
        opcion = input("Escriba la opcion que desea seleccionar: ")
        opcion = opcion.lower()
        if opcion == "crear pedido":
            negocio.createOrder()
        elif opcion == "modificar pedido":
            if clases.gestor_de_pedidos.validarListaVacia():
                negocio.updateOrder()
            else:
                print("\n\tLa lista esta vacia no se puede modificar pedidos")
        elif opcion == "mostrar todo":
            if clases.gestor_de_pedidos.validarListaVacia():
                clases.gestor_de_pedidos.mostrar_todos()
                print(
                    colors.OK,
                    "Para mas detalles sobre el pedido, elija la opcion 'Mostrar simplificado'",
                    colors.RESET,
                )
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar pedidos")
        elif opcion == "mostrar simplificado":
            if clases.gestor_de_pedidos.validarListaVacia():
                negocio.readOrder()
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar pedidos")
        elif opcion == "total margesort":
            if clases.gestor_de_pedidos.validarListaVacia():
                negocio.ordenar_por_merge_sort_por_total()
                negocio.permanenciaDeArchivos()
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar pedidos")
        elif opcion == "eliminar pedido":
            if clases.gestor_de_pedidos.validarListaVacia():
                negocio.deleteOrder()
            else:
                print("\n\tLa lista esta vacia no se puede eliminar pedidos")
        elif opcion == "salir":
            break


# menu Sucursal
def menuSucursal():
    pyfiglet.print_figlet(text="\tMenu\nSucursal", colors="YELLOW")
    global menu_text
    global gestor_de_sucursal
    while True:
        print(utils.sucursal_menu_text)
        opcion = input("Escriba la opcion que desea seleccionar: ")
        opcion = opcion.lower()
        if opcion == "crear sucursal":
            negocio.create_sucursal()
        elif opcion == "modificar sucursal":
            if clases.gestor_de_sucursal.validarListaVacia():
                print("la opcion no esta lista aun")
            else:
                print("\n\tLa lista esta vacia no se puede modificar sucursales")
        elif opcion == "mostrar todo":
            if clases.gestor_de_sucursal.validarListaVacia():
                clases.gestor_de_sucursal.mostrar_todos()
                print(
                    colors.OK,
                    "Para mas detalles sobre la sucursal, elija la opcion 'Mostrar simplificado'",
                    colors.RESET,
                )
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar sucursales")
        elif opcion == "mostrar simplificado":
            if clases.gestor_de_sucursal.validarListaVacia():
                print("la opcion no esta lista aun")
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar sucursales")
        elif opcion == "eliminar sucursal":
            if clases.gestor_de_sucursal.validarListaVacia():
                print("la opcion no esta lista aun")
            else:
                print("\n\tLa lista esta vacia no se puede eliminar sucursales")
        elif opcion == "salir":
            break


def mainMenu():
    menu = """
    1 - Gestión de Productos
    2 - Gestión de Clientes
    3 - Gestión de Pedidos
    4 - Gestión de Sucursales
    5 - Salir
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
            menuSucursal()
        if opcion == 5:
            pyfiglet.print_figlet(
                text="Gracias !!! \nVuelva Pronto", font="slant", colors="BLUE"
            )
            break


negocio.permanenciaDeArchivos()
mainMenu()
