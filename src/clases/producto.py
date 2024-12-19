class Producto:
    def __init__(self, cod, name: str, cost_price: float, price: float, stock: int):
        self.ref_code = int(cod)
        self.product_name = name
        self.product_cost_price = float(cost_price)
        self.product_charge = 0
        self.product_price = float(price)
        self.stock = int(stock)
        self.date = Fecha()
        self.date_edit = Fecha()
        self.date_product_edit = False

    def __repr__(self) -> str:
        if self.date_product_edit:
            return (
                f"══════════════════════════════════════════\n"
                f"          Producto: {self.product_name}\n"
                f"══════════════════════════════════════════\n"
                f"  Ref Code:             {self.ref_code}\n"
                f"  Ingreso:              {self.date}\n"
                f"  Ultima Modificacion:  {self.date_edit}\n"
                f"  Costo:                ${self.product_cost_price}\n"
                f"  Cargo:                {self.product_charge}%\n"
                f"  Precio:               ${self.product_price}\n"
                f"  Stock:                ({self.stock})\n"
                f"══════════════════════════════════════════\n"
            )
        else:
            return (
                f"══════════════════════════════════════════\n"
                f"          Producto: {self.product_name}\n"
                f"══════════════════════════════════════════\n"
                f"  Ref Code:     {self.ref_code}\n"
                f"  Ingreso:      {self.date}\n"
                f"  Costo:        ${self.product_cost_price}\n"
                f"  Cargo:        ${self.product_charge}%\n"
                f"  Precio:       ${self.product_price}\n"
                f"  Stock:       ({self.stock})\n"
                f"══════════════════════════════════════════\n"
            )

    def resumenProducto(self):
        if self.date_product_edit:
            return f"{self.ref_code} - {self.product_name} - Costo: ${self.product_cost_price} - Cargo: {self.product_charge}% - Precio: ${self.product_price} Stock: ({self.stock}\nIngreso: {self.date} | Ult. Modificacion: {self.date_edit}\n\t--------------------"
        else:
            return f"{self.ref_code} - {self.product_name} - Costo: ${self.product_cost_price} - Cargo: {self.product_charge}% - Precio: ${self.product_price} Stock: ({self.stock}) Fecha: {self.date}\n\t--------------------"

    def crear_precio_final(self):
        if self.product_charge:
            print(
                "- Si desea hacer un Descuento Ingrese el porcentaje con numero negativo"
            )
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
                    subtotal = self.product_price
                    total = cargo + subtotal
                    print(f"\n\t- El Subtotal es de ${subtotal}")
                    print(f"\t- El Cargo es de {opcion}%")
                    print(f"\t- El Total es de: ${total}")
                    self.product_price = float(total)
                    self.product_charge = int(0)
                else:
                    subtotal = self.product_price
                    cargo = subtotal * opcion / 100
                    total = cargo + subtotal
                    print(f"- El Subtotal es de {subtotal}")
                    print(f"- El Cargo es de {opcion}%")
                    print(f"- El Total es de: ${total}")
                    self.product_charge = float(opcion)
                    self.product_price = float(total)
        else:
            print(colors.FAIL, "Algo ha fallado intentelo nuevamente", colors.RESET)
