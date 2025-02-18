from negocio.negocio import graphi
from utils.colors_text import green_text, red_text
from utils.fecha import Fecha
from negocio.gestor_productos import gestor_de_productos


class Venta:
    def __init__(self, cod: int, sucursal: str, venta_cliente: str):
        self.id_venta = int(cod)
        self.venta_sucursal_name = sucursal
        self.venta_cliente = str(venta_cliente)
        self.product_list = {}
        self.venta_date = Fecha()

    def __repr__(self) -> str:
        return (
            f"══════════════════════════════════════════\n"
            f"          Venta en: {self.venta_sucursal_name}\n"
            f"══════════════════════════════════════════\n"
            f" ID :                  {self.id_venta}\n"
            f" Fecha de Venta:  {self.venta_date}\n"
            # f" Total:                {self.total}\n"
            f" Productos en el Carrito:({len(self.product_list)})\n"
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
        output += f"\nID Venta: ({self.id_venta}) - {self.venta_sucursal_name} - Fecha: {
            self.venta_date}\n"
        output += f"\t ------------------------------------------------ \n"
        if self.product_list:
            # Verificar si el product_list tiene productos
            output += "Productos de la Venta: \n"
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
        return f"ID: {self.id_venta} Venta en Sucursal: {self.venta_sucursal_name} - Fecha: {self.venta_date}"
