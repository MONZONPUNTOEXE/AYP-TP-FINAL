class Sucursal:
    def __init__(
        self,
        cod: int,
        sucursal: str,
        product_list: list,
        charge: float,
        subtotal: float,
        total: float,
    ):
        self.id_sucursal = int(cod)
        self.sucursal_name = sucursal
        self.product_list = product_list
        self.order_date = Fecha()
        self.fecha_edit = Fecha()
        self.sucursal_date_edit = False
        self.charge = charge
        self.subtotal = float(subtotal)
        self.total = float(total)
        # --------------
        self.len_product_list = len(product_list)

    def __repr__(self) -> str:
        if self.sucursal_date_edit:
            return (
                f"══════════════════════════════════════════\n"
                f"          Sucursal: {self.sucursal_name}\n"
                f"══════════════════════════════════════════\n"
                f" ID :                  {self.id_sucursal}\n"
                f" Ingreso de Sucursal:  {self.order_date}\n"
                f" Ultima Modificacion:  {self.fecha_edit}\n"
                f" Subtotal:             {self.subtotal}\n"
                f" Total:                {self.total}\n"
                f" Productos en Sucursal: ({self.len_product_list})\n"
                f"══════════════════════════════════════════\n"
            )
        else:
            return (
                f"══════════════════════════════════════════\n"
                f"          Sucursal: {self.sucursal_name}\n"
                f"══════════════════════════════════════════\n"
                f" ID :                  {self.id_sucursal}\n"
                f" Ingreso de Sucursal:  {self.order_date}\n"
                f" Total:                {self.total}\n"
                f" Productos en Carrito: ({self.len_product_list})\n"
                f"══════════════════════════════════════════\n"
            )

    def view_product_list(self):
        if self.sucursal_date_edit:
            print("Productos de la Sucursal")
            print(
                f"ID: {
                    self.id_sucursal} - Nombre: {self.sucursal_name} - Fecha: {self.order_date} - Ult. Modificacion: {self.fecha_edit}\nSubtotal: ${self.subtotal} - TOTAL: ${self.total}\n\t -----------------"
            )
            for producto in self.product_list:
                print(f"\t- {producto.product_name} ${producto.product_price}")
        else:
            print("Productos de la Sucursal")
            print(
                f"ID: {
                    self.id_sucursal} - Nombre: {self.sucursal_name} - Fecha: {self.order_date}\nSubtotal: ${self.subtotal} - TOTAL: ${self.total}\n\t -----------------"
            )
            for producto in self.product_list:
                print(f"\t- {producto.product_name} ${producto.product_price}")

    def resumen_sucursal(self):
        return f"ID: {
            self.id_sucursal} - Fecha: {self.order_date}"
