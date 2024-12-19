class Order:
    def __init__(
        self,
        cod: int,
        customer: str,
        product_list: list,
        charge: float,
        subtotal: float,
        total: float,
    ):
        self.id_order = int(cod)
        self.customer = customer
        self.product_list = product_list
        self.order_date = Fecha()
        self.fecha_edit = Fecha()
        self.order_date_edit = False
        self.extra_charge = float(charge)
        self.subtotal = float(subtotal)
        self.total = float(total)
        # --------------
        self.len_product_list = len(product_list)

    def __repr__(self) -> str:
        if self.order_date_edit:
            return (
                f"══════════════════════════════════════════\n"
                f"          ID del Pedido: {self.id_order}\n"
                f"══════════════════════════════════════════\n"
                f" Fecha del Pedido:     {self.order_date}\n"
                f" Ultima Modificacion:  {self.fecha_edit}\n"
                f" Cliente:              {self.customer}\n"
                f" Subtotal:             {self.subtotal}\n"
                f" Cargos:               {self.extra_charge}%\n"
                f" Total:                {self.total}\n"
                f" Productos en Carrito: ({self.len_product_list})\n"
                f"══════════════════════════════════════════\n"
            )
        else:
            return (
                f"══════════════════════════════════════════\n"
                f"          ID del Pedido: {self.id_order}\n"
                f"══════════════════════════════════════════\n"
                f" Fecha del Pedido:  {self.order_date}\n"
                f" Cliente:         {self.customer}\n"
                f" Subtotal:        {self.subtotal}\n"
                f" Cargos:          {self.extra_charge}%\n"
                f" Total:           {self.total}\n"
                f" Productos en Carrito: ({self.len_product_list})\n"
                f"══════════════════════════════════════════\n"
            )
