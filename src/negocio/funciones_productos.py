from clases.producto import Producto
from negocio.gestor_productos import gestor_de_productos
from negocio.negocio import graphi
from utils.validaciones import validateProductName, floatValidate, intValidate
from utils.gestion_archivos import escribir_en_binario_productos
from utils.colors_text import red_text, yellow_text, green_text
from utils.fecha import Fecha


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
        print(green_text("Se ha creado un nuevo Producto"))
        print(new_product)
        user = input(
            yellow_text(
                f"hay un total de ({len(gestor_de_productos.productos)
                                    } Productos desea ingresar mas ?: s/n"
            )
        )
        if user.lower() == "n":
            break


# Update Producto ---------------
def update_all_product():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = intValidate("Ingrese el codigo del Producto que desea modificar: ")
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        print("Nombre del Producto Actual", producto_encontrado.product_name)
        nuevo_nombre = validateProductName("Ingrese el nuevo nombre: ")
        print("Precio de Costo del Producto", producto_encontrado.product_cost_price)
        nuevo_cost_price = floatValidate("Ingrese el nuevo precio de costo: ")
        print("Precio Final del Producto", producto_encontrado.product_price)
        nuevo_precio = floatValidate("Ingrese el nuevo precio: ")
        print("Stock actual del Producto", producto_encontrado.stock)
        nuevo_stock = intValidate("Ingrese el nuevo Stock: ")
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
            producto_encontrado.product_cost_price = float(cost_price_sin_cambio)
            producto_encontrado.product_price = float(precio_sin_cambio)
            producto_encontrado.stock = int(stock_sin_cambio)
            print("El Producto no se ha actualizado")
        else:
            producto_encontrado.date_product_edit = True
            producto_encontrado.date_edit = Fecha()
            escribir_en_binario_productos()
            print("El Producto se ha actualizado correctamente")
            print(producto_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


def update_product_name():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = intValidate(
        "Ingrese el codigo del Producto que desea modificarle el nombre: "
    )
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        print("Nombre Actual:", green_text(f"{producto_encontrado.product_name}"))
        nuevo_nombre = validateProductName("Ingrese el nuevo nombre: ")
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
            producto_encontrado.date_edit = Fecha()
            print("El Producto se ha actualizado correctamente")
            escribir_en_binario_productos()
            print(producto_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


def update_product_cost_price():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = intValidate(
        "Ingrese el codigo del Producto que desea modificar el costo: "
    )
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        print("Costo Actual:", green_text(f"${producto_encontrado.product_cost_price}"))
        nuevo_precio = floatValidate("Ingrese el nuevo Costo del Producto: ")
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
            producto_encontrado.date_edit = Fecha()
            print("El Producto se ha actualizado correctamente")
            escribir_en_binario_productos()
            print(producto_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


def update_product_price():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = intValidate("Ingrese el codigo del Producto que desea modificar: ")
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        print(
            "Precio final actual:", green_text(f"${producto_encontrado.product_price}")
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
            producto_encontrado.date_edit = Fecha()
            print("El Producto se ha actualizado correctamente")
            escribir_en_binario_productos()
            print(producto_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


def update_product_stock():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    product_code = intValidate(
        "Ingrese el codigo del Producto que desea modificar su stock: "
    )
    producto_encontrado = gestor_de_productos.buscar_por_codigo(product_code)
    if producto_encontrado:
        print("Stock Actual:", green_text(f"${producto_encontrado.stock}"))
        print(producto_encontrado.resumenProducto())
        stock_sin_cambios = producto_encontrado.stock
        nuevo_stock = intValidate("Ingrese el nuevo Stock: ")
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
            producto_encontrado.date_edit = Fecha()
            print("El Stock del Producto se ha actualizado correctamente")
            escribir_en_binario_productos()
            print(producto_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


def perdida_productos():
    global gestor_de_productos
    gestor_de_productos.mostrar_simplificado()
    code = intValidate("Ingrese el ID del Producto que desea quitar Stock: ")
    producto_encontrado = gestor_de_productos.buscar_por_codigo(code)
    if producto_encontrado:
        print("Stock Actual:", green_text(f"${producto_encontrado.stock}"))
        print(producto_encontrado.resumenProducto())
        stock_sin_cambios = producto_encontrado.stock
        cantidad_perdida = intValidate("Ingrese la Cantidad que desea Quitar: ")
        # cambios anteriores
        text_sin_cambios = "Sin aplicar Cambios"
        graphi(text_sin_cambios)
        print(producto_encontrado)

        if cantidad_perdida:
            producto_encontrado.stock = producto_encontrado.stock - cantidad_perdida

        text_con_cambios = "Aplicando los cambios... "
        graphi(text_con_cambios)
        print(producto_encontrado)

        decidir_cambios = input("Desea guardar los cambios ? - (Si/no)")
        if decidir_cambios.lower() in ("no", "n"):
            producto_encontrado.stock = stock_sin_cambios
            print("El Stock del Producto no se ha actualizado")
        else:
            producto_encontrado.date_product_edit = True
            producto_encontrado.date_edit = Fecha()
            print("El Stock del Producto se ha actualizado correctamente")
            escribir_en_binario_productos()
            print(producto_encontrado)


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
