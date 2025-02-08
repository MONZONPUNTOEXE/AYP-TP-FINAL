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


from utils.gestion_archivos import (
    escribir_en_binario_productos,
    escribir_en_binario_sucursales,
)


# Funcionalidades de Sucursal
def create_sucursal():
    global gestor_de_sucursal
    global gestor_de_productos
    pyfiglet.print_figlet(text="Crear Sucursal", colors="BLUE")
    while True:
        cod = gestor_de_sucursal.create_sucursal_cod()
        name = validateProductName()
        new_sucursal = Sucursal(cod, name)
        user = input(yellow_text("Desea ingresar Productos a esta Sucursal ?: s/n: "))
        if (
            user.lower() in ("s", "si", "yes", "y")
            and gestor_de_productos.validarListaVacia()
        ):
            # Sucursal con productos
            new_sucursal_with_products = carrito_add_product(new_sucursal)
            gestor_de_sucursal.sucursales.append(new_sucursal_with_products)
            escribir_en_binario_sucursales()
            escribir_en_binario_productos()
            print(green_text("Se ha creado una nueva Sucursal con Productos"))
            print(new_sucursal_with_products)
        else:
            # Sucursal sin productos
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
        print("\t -------- Lista de Sucursales ---------")
        gestor_de_sucursal.mostrar_simplificado()
        code = intValidate(
            "\nIngrese el codigo del la Sucursal Para agregar productos: "
        )
        sucursal_encontrado = gestor_de_sucursal.buscar_por_codigo(code)
        if sucursal_encontrado:
            print(f"\n\tSu Sucursal es: {sucursal_encontrado.sucursal_name}\n")
            print(sucursal_encontrado)
            return sucursal_encontrado
        else:
            print(
                yellow_text(
                    "El codigo de Sucursal ingresado no existe, intentelo nuevamente"
                )
            )


# sumar todos los stock que tiene el Producto
def carrito_add_product(sucursal):
    global gestor_de_productos

    while True:
        print("\n\t------ Productos Disponibles en el Inventario -------")
        gestor_de_productos.mostrar_simplificado()
        prod_code = intValidate("Ingrese el Codigo del Producto que desee agregar: ")
        producto_encontrado = gestor_de_productos.buscar_por_codigo(prod_code)
        if producto_encontrado:
            producto_de_sucursal = copy.deepcopy(producto_encontrado)
            stock_validate = "Ingrese el Stock que desea destinar a la Sucursal: "
            sucursal_stock = updateStock(
                producto_de_sucursal, stock_validate, False, True
            )
            producto_encontrado.stock -= sucursal_stock
            user = ""
            if producto_encontrado.stock == 0:
                print(red_text("No hay mas Stock para este Producto"))
                user = input(
                    f"Desea ingresar mas Productos al Carrito para {
                        sucursal.sucursal_name} ?: s/n "
                )
                if user.lower() in ("n", "no"):
                    escribir_en_binario_sucursales()
                    escribir_en_binario_productos()
                    return sucursal
            else:
                sucursal.agregar_producto(producto_de_sucursal.ref_code, sucursal_stock)
                print(
                    green_text(
                        f"Se han agregado {sucursal_stock} unidades del Producto ({producto_de_sucursal.ref_code}) {
                            producto_de_sucursal.product_name}.\n"
                    )
                )
                print(
                    yellow_text(
                        f"Carrito Actual para {
                            sucursal.sucursal_name}"
                    )
                )
                print(sucursal.view_product_list())
            if user == "":
                user = input(
                    f"Desea ingresar mas Productos al Carrito para {
                        sucursal.sucursal_name} ?: s/n "
                )
                if user.lower() in ("n", "no"):
                    # aca podriamos agregar el descuento
                    # new_sucursal = agregar_descuento(
                    #     sucursal, CARRITO_DE_PRODUCTOS.carrito
                    # )
                    escribir_en_binario_sucursales()
                    escribir_en_binario_productos()
                    return sucursal

        else:
            print(red_text("El Codigo del Producto no fue encontrado"))


def agregar_descuento(sucursal, CARRITO_DE_PRODUCTOS: list):
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
            total = 0
            subtotal = 0
            print(f"\n\t- El Subtotal es de ${subtotal}")
            print(f"\t- El Cargo es de {opcion}%")
            print(f"\t- El Total es de: ${total}")
            cod = sucursal.id_sucursal
            name = sucursal.sucursal_name
            new_sucursal = Sucursal(
                cod, name, CARRITO_DE_PRODUCTOS, opcion, subtotal, total
            )
            return new_sucursal
        else:
            total = 0
            subtotal = 0
            print(f"- El Subtotal es de {subtotal}")
            print(f"- El Cargo es de {opcion}%")
            print(f"- El Total es de: ${total}")

            cod = sucursal.id_sucursal
            name = sucursal.sucursal_name
            new_sucursal = Sucursal(
                cod, name, CARRITO_DE_PRODUCTOS, opcion, subtotal, total
            )
            return new_sucursal


def add_sucursal_product():
    global gestor_de_productos
    global gestor_de_sucursal
    pyfiglet.print_figlet(text="Agregar Productos a Sucursal", colors="BLUE")
    if (
        gestor_de_sucursal.validarListaVacia()
        and gestor_de_productos.validarListaVacia()
    ):
        sucursal_encontrado = buscar_sucursal_producto()
        if sucursal_encontrado:
            carrito_add_product(sucursal_encontrado)
    else:
        if len(gestor_de_productos.productos) == 0:
            text = "No hay productos para seleccionar, debe cargar los Productos e intentelo nuevamente"
            graphi(text)
        if len(gestor_de_sucursal.sucursales) == 0:
            text = "No hay Sucursal para seleccionar, debe cargar las sucursales e intentelo nuevamente"
            graphi(text)


# modificar nombre de sucursal
def update_sucursal_name():
    global gestor_de_sucursal
    gestor_de_sucursal.mostrar_todos()
    code = intValidate("Ingrese el ID de la Sucursal que desea Cambiar el nombre: ")
    sucursal_encontrado = gestor_de_sucursal.buscar_por_codigo(code)
    if sucursal_encontrado:
        new_name = input("Ingrese el Nuevo nombre de la Sucursal: ")
        opcion = input(
            yellow_text(f"\n\tAcepta los cambios ?\n\nNombre Anterior: {
                sucursal_encontrado.sucursal_name}\nNombre Actual: {new_name}  \nS/n: ")
        )
        if opcion.lower() in ("si", "s", "y", "yes"):
            sucursal_encontrado.sucursal_name = opcion
            escribir_en_binario_sucursales()
            print(green_text("Se ha actualizado el nombre exitosamente!"))
        else:
            print(red_text("El nombre no ha sido Actualizado"))
    else:
        print("El codigo no fue encontrado!")


# modificar Stock de sucursal (MAL PLANTEADO, esto puede servir para actualizar el stock y no para los productos de la Sucursal)
def update_sucursal_stock():
    global gestor_de_sucursal
    global gestor_de_productos
    gestor_de_sucursal.mostrar_todos()
    code = intValidate("Ingrese el ID de la Sucursal que desea Cambiar el Stock: ")
    sucursal_encontrado = gestor_de_sucursal.buscar_por_codigo(code)
    if sucursal_encontrado and sucursal_encontrado.verify_empty_product_list():
        print(green_text(sucursal_encontrado.view_product_list()))
        opcion = intValidate("Ingrese el ID del producto que desea cambiar el Stock: ")
        id_product_list = sucursal_encontrado.iterar_product_list(opcion)
        if id_product_list:
            cantidad_anterior = sucursal_encontrado.product_list_get_cantidad(opcion)
            new_stock = intValidate("Ingrese el nuevo Stock del producto: ")
            producto_inventario = gestor_de_productos.buscar_por_codigo(opcion)
            producto_stock = updateStock(producto_inventario, new_stock, True, False)
            if producto_inventario.stock == 0:
                print(red_text("No hay mas Stock para este Producto"))
            else:
                producto_inventario.stock -= producto_stock
                sucursal_encontrado.sucursal_update_stock_product(
                    id_product_list, new_stock
                )
                print(f"Se ha actualizado el Producto: {
                      producto_inventario.product_name} de {cantidad_anterior} a {new_stock}")
    else:
        print("El codigo no fue encontrado!")

    #     new_name = input("Ingrese el Nuevo nombre de la Sucursal: ")
    #     opcion = input(
    #         yellow_text(f"\n\tAcepta los cambios ?\n\nNombre Anterior: {
    #             sucursal_encontrado.sucursal_name}\nNombre Actual: {new_name}  \nS/n: ")
    #     )
    #     if opcion.lower() in ("si", "s", "y", "yes"):
    #         sucursal_encontrado.sucursal_name = opcion
    #         escribir_en_binario_sucursales()
    #         print(green_text("Se ha actualizado el nombre exitosamente!"))
    #     else:
    #         print(red_text("El nombre no ha sido Actualizado"))
    # else:
    #     print("El codigo no fue encontrado!")


# eliminar Producto de Sucursal


# eliminar sucursal
def delete_sucursal():
    global gestor_de_sucursal
    gestor_de_sucursal.mostrar_simplificado()
    code = intValidate(
        "Ingrese el ID del Pedido que desea Eliminar\n(Una vez seleccionado, Puede Cancelar): "
    )
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
