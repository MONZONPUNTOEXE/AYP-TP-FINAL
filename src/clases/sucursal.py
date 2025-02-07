from negocio.negocio import graphi
from utils.colors_text import green_text, red_text
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
            return cantidad
        else:
            # Si no está, lo agregamos con la cantidad inicial
            self.product_list[producto_id] = int(cantidad)
            return cantidad

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
            output += f"\nID Sucursal: ({self.id_sucursal}) - {self.sucursal_name} - Fecha: {
                self.order_date} - Ult. Modificacion: {self.fecha_edit}\n"
            output += f"\t ------------------------------------------------ \n"
            output += "Productos de la Sucursal:\n"
            if self.product_list:
                # Verificar si el product_list tiene productos
                output += "Productos en la Sucursal: \n"
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
                output += f"\t ------------------------------------------------ \n"

            else:
                output += "El carrito está vacío."
        else:
            output += f"\nID Sucursal: ({self.id_sucursal}) - {self.sucursal_name} - Fecha: {
                self.order_date}\n"
            output += f"\t ------------------------------------------------ \n"
            if self.product_list:
                # Verificar si el product_list tiene productos
                output += "Productos en la Sucursal: \n"
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
                output += f"\t ------------------------------------------------ \n"

            else:
                output += "El carrito está vacío."
        return output

    def verify_empty_product_list(self):
        if len(self.product_list) > 0:
            return True
        else:
            return False

    def iterar_product_list(self, search_id_product):
        for producto_id in self.product_list:
            if producto_id == search_id_product:
                return producto_id
        print(
            red_text(
                "El codigo ingresado no se encuentra en los productos de la Sucursal"
            )
        )

    def product_list_get_cantidad(self, search_id_product):
        for producto_id in self.product_list:
            if producto_id == search_id_product:
                cantidad = self.product_list[producto_id]
                return cantidad
        print(
            red_text(
                "El codigo ingresado no se encuentra en los productos de la Sucursal"
            )
        )

    def sucursal_update_stock_product(self, search_id_product, update_stock_product):
        for producto_id in self.product_list:
            if search_id_product == producto_id:
                self.product_list[producto_id] = update_stock_product
                return update_stock_product
            else:
                print("No se pudo actualizar correctamente, hubo un error")

    def resumen_sucursal(self):
        return f"ID: {self.id_sucursal} Nombre: {self.sucursal_name} - Fecha: {self.order_date}"
