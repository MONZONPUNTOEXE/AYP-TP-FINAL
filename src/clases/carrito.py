from utils.colors_text import green_text, red_text


class CarritoDeCompras:
    def __init__(self):
        # Diccionario donde las claves son los ID de productos y los valores son diccionarios con detalles
        self.product_list = {}

    def agregar_producto(self, producto_id, nombre, stock):
        # Verificar si el producto ya está en el carrito
        if producto_id in self.product_list:
            # Si ya está en el carrito, solo actualizamos la stock
            self.product_list[producto_id]["stock"] += stock
            print(
                green_text(f"Se han agregado {stock} unidades del producto '{
                    nombre}' al carrito.")
            )
        else:
            # Si no está, agregamos avisamos que el producto_id no existe
            print(red_text("El producto que selecciono no existe! "))
            # self.product_list[producto_id] = {
            #     "nombre": nombre,
            #     "stock": stock,
            #     "precio": precio,
            #     "descuento": descuento,
            #     "fecha": fecha,
            # }
            # print(f"Producto '{nombre}' agregado al carrito con {
            #       stock} unidades.")

    # def mostrar_carrito(self):
    #     # Verificar si el carrito tiene productos
    #     if self.product_list:
    #         print("Productos en el carrito:")
    #         for producto_id, detalles in self.product_list.items():
    #             nombre = detalles["nombre"]
    #             stock = detalles["stock"]
    #             precio = detalles["precio"]
    #             descuento = detalles["descuento"]
    #             fecha = detalles["fecha"]
    #
    #             # Calcular el precio con el descuento aplicado
    #             precio_con_descuento = precio * (
    #                 1 - descuento / 100
    #             )  # Aplicar el descuento
    #             total = precio_con_descuento * stock  # Total por el producto
    #
    #             print(
    #                 f"ID: {producto_id}, Nombre: {nombre}, stock: {
    #                     stock}, Precio: ${precio}, "
    #                 f"Descuento: {descuento}%, Fecha: {
    #                     fecha}, Total: ${total:.2f}"
    #             )
    #     else:
    #         print("El carrito está vacío.")


# # Ejemplo de uso
# carrito = CarritoDeCompras()
#
# # Agregar productos con nombre, stock, precio y descuento
# carrito.agregar_producto(1, "Camiseta", 2, 20,
#                          descuento=10)  # 10% de descuento
# carrito.agregar_producto(2, "Pantalón", 1, 40)
# carrito.agregar_producto(1, "Camiseta", 1, 20)  # Agregar 1 unidad más
#
# # Mostrar el carrito
# carrito.mostrar_carrito()
