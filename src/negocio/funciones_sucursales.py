import pyfiglet
import copy

from utils.colors_text import red_text, green_text, yellow_text
from utils.validaciones import intValidate, floatValidate_neg
from negocio.negocio import graphi, subtotalCarrito, mostrarCarrito
from clases.sucursal import Sucursal
from negocio.funciones_productos import validateProductName
from negocio.funciones_stock import updateStock
from negocio.gestor_sucursales import gestor_de_sucursal
from negocio.gestor_productos import gestor_de_productos

from utils.gestion_archivos import escribir_en_binario_sucursales


# Funcionalidades de Sucursal
def create_sucursal():
    global gestor_de_sucursal
    global gestor_de_productos
    pyfiglet.print_figlet(text="Crear Sucursal", colors="BLUE")
    while True:
        cod = gestor_de_sucursal.create_sucursal_cod()
        name = validateProductName()
        new_sucursal = Sucursal(cod, name, [], 0, 0, 0)
        user = input(yellow_text("Desea ingresar Productos a esta Sucursal ?: s/n: "))
        if (
            user.lower() in ("s", "si", "yes", "y")
            and gestor_de_productos.validarListaVacia()
        ):
            new_sucursal_with_products = carrito_add_product(new_sucursal)
            gestor_de_sucursal.sucursales.append(new_sucursal_with_products)
        else:
            gestor_de_sucursal.sucursales.append(new_sucursal)
            escribir_en_binario_sucursales()
            print(green_text("Se ha creado una nueva Sucursal"))
            print(new_sucursal)
        if not gestor_de_productos.validarListaVacia() and user.lower() in (
            "s",
            "si",
            "yes",
            "y",
        ):
            print(red_text("Lista de Productos Vacia"))
            print(
                red_text(
                    "Si deseas agregar productos a esta Sucursal, agregue Productos en el Gestor de Productos e intentelo nuevamente"
                )
            )
        user = input(
            yellow_text(
                f"hay un total de ({len(
                    gestor_de_sucursal.sucursales)}) Sucursales, desea ingresar mas Sucursales ?: s/n"
            )
        )
        if user.lower() == "n":
            break


def buscar_sucursal_producto():
    while True:
        print("\t ------------ Lista de Sucursales -----------------")
        gestor_de_sucursal.mostrar_simplificado()
        code = intValidate(
            "\nIngrese el codigo del la Sucursal Para agregar productos: "
        )
        sucursal_encontrado = gestor_de_sucursal.buscar_por_codigo(code)
        if sucursal_encontrado:
            print(f"\n\tSu Sucursal es: {sucursal_encontrado.sucursal_name}\n")
            return sucursal_encontrado
        else:
            print(
                yellow_text(
                    "El codigo de Sucursal ingresado no existe, intentelo nuevamente"
                )
            )


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
        prod_code = intValidate("Ingrese el Codigo del Producto que desee agregar: ")
        producto_encontrado = gestor_de_productos.buscar_por_codigo(prod_code)
        if producto_encontrado:
            producto_de_sucursal = copy.deepcopy(producto_encontrado)
            stock_validate = "Ingrese el Stock que desea destinar a la Sucursal: "
            sucursal_stock = updateStock(
                producto_encontrado, stock_validate, False, True
            )
            user = ""
            if producto_de_sucursal.stock == 0 or None:
                print(red_text("No hay mas Stock para este Producto"))
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
                    print("llegaste al brake")
                    break
            else:
                producto_de_sucursal.stock = sucursal_stock
                CARRITO_DE_PRODUCTOS.append(producto_encontrado)
            if len(CARRITO_DE_PRODUCTOS) > 1:
                print(
                    yellow_text(
                        f"Carrito Actual para {
                            sucursal.sucursal_name}"
                    )
                )
                mostrarCarrito(CARRITO_DE_PRODUCTOS)
                print(
                    green_text(
                        f"El Subtotal del Carrito es de ${
                            subtotalCarrito(CARRITO_DE_PRODUCTOS)}\n"
                    )
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
            print(red_text("El Codigo del Producto no fue encontrado"))


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
            new_sucursal = Sucursal(
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
            new_sucursal = Sucursal(
                cod, name, CARRITO_DE_PRODUCTOS, opcion, subtotal, total
            )
            CARRITO_DE_PRODUCTOS = []
            return new_sucursal


def delete_sucursal():
    global gestor_de_sucursal
    gestor_de_sucursal.mostrar_simplificado()
    code = intValidate("Ingrese el ID del Pedido que desea Eliminar: ")
    sucursal_encontrado = gestor_de_sucursal.buscar_por_codigo(code)
    if sucursal_encontrado:
        opcion = input(f"\n\tDesea eliminar ?\n\n{sucursal_encontrado}\nS/n: ")
        if opcion.lower() in ("si", "s", "y", "yes" "ye"):
            gestor_de_sucursal.sucursales.remove(sucursal_encontrado)
            escribir_en_binario_sucursales()
            print(f"\n\tSe ha eliminado de la lista:\n{sucursal_encontrado}")
        else:
            print("El pedido no se ha sido eliminado...")
    else:
        print("El codigo no fue encontrado!")
