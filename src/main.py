# external library
import utils.menu as utils
import pyfiglet

# internal modules
from utils.gestion_archivos import permanenciaDeArchivos
from utils.validaciones import intValidate
from utils.colors_text import red_text, green_text

# funciones de productos
from negocio.gestor_productos import gestor_de_productos
from negocio.funciones_productos import (
    createProduct,
    update_all_product,
    update_product_name,
    update_product_price,
    update_product_cost_price,
    update_product_stock,
    removeProduct,
)

# funciones de clientes
from negocio.gestor_clientes import gestor_de_clientes
from negocio.funciones_clientes import createClient, updateClient, deleteClient

# funciones de pedidos
from negocio.gestor_pedidos import gestor_de_pedidos
from negocio.funciones_pedidos import createOrder, updateOrder, readOrder, deleteOrder
from negocio.negocio import ordenar_por_merge_sort_por_total

# funciones de Sucursal
from negocio.gestor_sucursales import gestor_de_sucursal
from negocio.funciones_sucursales import (
    create_sucursal,
    add_sucursal_product,
    delete_sucursal,
)

# Creacion de los objetos "Gestores de Entidades" -----------------------------


def menuProductos():
    pyfiglet.print_figlet(text="\tMenu\nProductos", colors="GREEN")
    global menu_text
    global gestor_de_productos
    while True:
        print(utils.product_menu_text)
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
        print(utils.update_product_menu_text)
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
            print(red_text("Opcion incorrecta, intentelo nuecamente"))


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
        print(utils.pedidos_menu_text)
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
                    green_text(
                        "Para mas detalles sobre el pedido, elija la opcion 'Mostrar simplificado'"
                    )
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
            create_sucursal()
        elif opcion == "modificar sucursal":
            if gestor_de_sucursal.validarListaVacia():
                print("la opcion no esta lista aun")
            else:
                print("\n\tLa lista esta vacia no se puede modificar sucursales")
        elif opcion == "agregar productos":
            if gestor_de_sucursal.validarListaVacia():
                add_sucursal_product()
            else:
                print("\n\tLa lista esta vacia no se puede modificar sucursales")
        elif opcion == "mostrar todo":
            if gestor_de_sucursal.validarListaVacia():
                gestor_de_sucursal.mostrar_todos()
                print(
                    green_text(
                        "Para mas detalles sobre la sucursal, elija la opcion 'Mostrar simplificado'"
                    )
                )
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar sucursales")
        elif opcion == "mostrar simplificado":
            if gestor_de_sucursal.validarListaVacia():
                gestor_de_sucursal.mostrar_simplificado()
            else:
                print("\n\tLa lista esta vacia no se pueden mostrar sucursales")
        elif opcion == "eliminar sucursal":
            if gestor_de_sucursal.validarListaVacia():
                delete_sucursal()
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
            menuSucursal()
        if opcion == 5:
            pyfiglet.print_figlet(
                text="Gracias !!! \nVuelva Pronto", font="slant", colors="BLUE"
            )
            break


permanenciaDeArchivos()
mainMenu()
