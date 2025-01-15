from negocio.negocio import graphi
from utils.colors_text import green_text
from utils.fecha import Fecha
from negocio.gestor_productos import gestor_de_productos


class Sucursal:
    def __init__(
        self,
        cod: int,
        sucursal: str,
        # charge: float,
        # subtotal: float,
        # total: float,
    ):
        self.id_sucursal = int(cod)
        self.sucursal_name = sucursal
        self.product_list = {}
        self.order_date = Fecha()
        self.fecha_edit = Fecha()
        self.sucursal_date_edit = False
        # self.charge = charge
        # self.subtotal = float(subtotal)
        # self.total = float(total)
        # --------------

    def __repr__(self) -> str:
        if self.sucursal_date_edit:
            return (
                f"══════════════════════════════════════════\n"
                f"          Sucursal: {self.sucursal_name}\n"
                f"══════════════════════════════════════════\n"
                f" ID :                  {self.id_sucursal}\n"
                f" Ingreso de Sucursal:  {self.order_date}\n"
                f" Ultima Modificacion:  {self.fecha_edit}\n"
                # f" Subtotal:             {self.subtotal}\n"
                # f" Total:                {self.total}\n"
                f" Productos en Sucursal: ({len(self.product_list)})\n"
                f"══════════════════════════════════════════\n"
            )
        else:
            return (
                f"══════════════════════════════════════════\n"
                f"          Sucursal: {self.sucursal_name}\n"
                f"══════════════════════════════════════════\n"
                f" ID :                  {self.id_sucursal}\n"
                f" Ingreso de Sucursal:  {self.order_date}\n"
                # f" Total:                {self.total}\n"
                f" Productos en Sucursal: ({len(self.product_list)})\n"
                f"══════════════════════════════════════════\n"
            )

    def agregar_producto(self, producto_id, cantidad: int):
        # Si el producto ya está en el carrito, sumamos la cantidad
        if producto_id in self.product_list:
            self.product_list[producto_id] += int(cantidad)
            print(
                green_text(f"Se han agregado {
                    cantidad} unidades del producto con ID {producto_id}.")
            )
        else:
            # Si no está, lo agregamos con la cantidad inicial
            self.product_list[producto_id] = int(cantidad)
            print(
                green_text(f"Producto con ID {producto_id} agregado al carrito con {
                    cantidad} unidades.")
            )

    # def mostrar_carrito(self):
    #     if self.product_list:
    #         global gestor_de_productos
    #         # Verificar si el product_list tiene productos
    #         print("Productos en la Sucursal:")
    #         for producto_id, cantidad in self.product_list.items():
    #             nombre_producto = gestor_de_productos.buscar_por_codigo(
    #                 producto_id)
    #             name = nombre_producto.product_name
    #             costo = nombre_producto.product_cost_price
    #             precio_final = nombre_producto.product_price
    #             descuento = nombre_producto.product_charge
    #             stock_inventario = nombre_producto.stock
    #             fecha = None
    #
    #             print(f"ID: {producto_id} - {name} - Fecha: {fecha} - Cantidad: {
    #                 cantidad}")
    #     else:
    #         print("El carrito está vacío.")

    def view_product_list(self):
        output = ""
        global gestor_de_productos
        if self.sucursal_date_edit:
            output += "\t -----------------\n"
            output += f"\nID: {self.id_sucursal} - Nombre: {self.sucursal_name} - Fecha: {
                self.order_date} - Ult. Modificacion: {self.fecha_edit}\n"
            output += "Productos de la Sucursal:\n"
            if self.product_list:
                # Verificar si el product_list tiene productos
                print("Productos en la Sucursal:")
                for producto_id, cantidad in self.product_list.items():
                    nombre_producto = gestor_de_productos.buscar_por_codigo(
                        producto_id)
                    name = nombre_producto.product_name
                    costo = nombre_producto.product_cost_price
                    precio_final = nombre_producto.product_price
                    stock_inventario = nombre_producto.stock

                    # Escapados ANSI
                    # output += "\033[4m"  # Activa el subrayado
                    output += (
                        "\n----------------------------\n"  # Línea de guiones al inicio
                    )
                    output += f"ID: {producto_id} - {name} - Stock en Sucursal: {cantidad} Costo: {
                        costo} Precio: {precio_final} - Stock de Inventario:{stock_inventario}\n"
                    output += (
                        "----------------------------\n"  # Línea de guiones al final
                    )
                    output += "\033[0m"  # Restablece el formato
            else:
                output += "El carrito está vacío."

        else:
            output += f"\nSucursal: {self.sucursal_name} - Fecha: {
                self.order_date}\n"
            if self.product_list:
                # Verificar si el product_list tiene productos
                output += "Productos en la Sucursal:\n"
                costo_total = 0
                precio_total = 0
                for producto_id, cantidad in self.product_list.items():
                    nombre_producto = gestor_de_productos.buscar_por_codigo(
                        producto_id)
                    name = nombre_producto.product_name
                    costo = nombre_producto.product_cost_price
                    precio_final = nombre_producto.product_price
                    stock_inventario = nombre_producto.stock

                    output += f"\nID: {producto_id} - {name} | Stock en Sucursal: {cantidad} | Costo: {
                        costo} | Precio: {precio_final} | Stock de Inventario:{stock_inventario}\n"
                    output += f"\t ------------------------------------------------ "
                    costo_subtotal = costo * cantidad
                    precio_subtotal = precio_final * cantidad

                    costo_total += costo_subtotal
                    precio_total += precio_subtotal

                output += f"\n\n\t- El Costo total del Carrito es de: {
                    costo_total}"
                output += f"\n\t- El Precio final total del Carrito es de: {
                    precio_total}\n"

            else:
                output += "El carrito está vacío."
        return output

    def resumen_sucursal(self):
        return f"ID: {self.id_sucursal} Nombre: {self.sucursal_name} - Fecha: {self.order_date}"
