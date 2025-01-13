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
                f"Se han agregado {
                    cantidad} unidades del producto con ID {producto_id}."
            )
        else:
            # Si no está, lo agregamos con la cantidad inicial
            self.product_list[producto_id] = int(cantidad)
            print(
                f"Producto con ID {producto_id} agregado al carrito con {
                    cantidad} unidades."
            )

    def mostrar_carrito(self):
        if self.product_list:
            global gestor_de_productos
            # Verificar si el product_list tiene productos
            print("Productos en el product_list:")
            for producto_id, cantidad in self.product_list.items():
                nombre_producto = gestor_de_productos.buscar_por_codigo(
                    producto_id)
                name = nombre_producto.product_name

                print(f"ID: {producto_id} - Nombre: {name} - Cantidad: {
                    cantidad}")
        else:
            print("El carrito está vacío.")

    # def view_product_list(self):
    #     output = ""
    #     if self.sucursal_date_edit:
    #         output += "\t -----------------\n"
    #         output += f"\nID: {self.id_sucursal} - Nombre: {self.sucursal_name} - Fecha: {
    #             self.order_date} - Ult. Modificacion: {self.fecha_edit}\nSubtotal: ${self.subtotal} - TOTAL: ${self.total}\n"
    #         output += "Productos de la Sucursal:\n"
    #         for producto in self.product_list:
    #             output += f"\t- {producto.product_name} ${
    #                 producto.product_price} Stock: ({producto.stock})\n"
    #     else:
    #         output += "\t -----------------\n"
    #         output += f"\nID: {self.id_sucursal} - Nombre: {self.sucursal_name} - Fecha: {
    #             self.order_date}\nSubtotal: ${self.subtotal} - TOTAL: ${self.total}\n"
    #         output += "Productos de la Sucursal:\n"
    #         for producto in self.product_list:
    #             output += f"\t- {producto.product_name} ${
    #                 producto.product_price} Stock: ({producto.stock})\n"
    #     return output

    def resumen_sucursal(self):
        return f"ID: {self.id_sucursal} Nombre: {self.sucursal_name} - Fecha: {self.order_date}"
