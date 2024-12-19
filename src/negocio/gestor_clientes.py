class GestorClientes:
    def __init__(self) -> None:
        self.clientes: list[Cliente] = []

    def __str__(self):
        if len(self.clientes) > 0:
            return str(self.clientes)
        else:
            return (
                colors.WARNING + "No hay clientes cargados actualmente" + colors.RESET
            )

    def validarListaVacia(self):
        if len(self.clientes) > 0:
            return True
        else:
            return None

    def eliminar_cliente(self, cliente_a_eliminar: Cliente):
        self.clientes.remove(cliente_a_eliminar)

    def _es_fecha_nacimiento_valida(self, fecha_str: str) -> bool:
        try:
            Fecha(fecha_str)
            return True
        except ValueError:
            return False

    def _pedir_fecha_nacimiento_valida(self):
        fecha_nacimiento = "NO_VALIDA"
        while not self._es_fecha_nacimiento_valida(fecha_nacimiento):
            fecha_nacimiento = input(
                "Ingrese la fecha de nacimiento del Cliente (dd/mm/aaaa): "
            )
            if not self._es_fecha_nacimiento_valida(fecha_nacimiento):
                print("Formato de fecha no válido. Debe ser DIA/MES/ANIO (dd/mm/aaaa)")
        return Fecha(fecha_nacimiento)

    def mostrar_todos(self):
        if self.clientes:
            print("Listando los Clientes disponibles")
            for cliente in self.clientes:
                print(colors.OK, cliente, colors.RESET)
        else:
            print(
                colors.WARNING
                + "No hay Clientes cargados hasta el momento"
                + colors.RESET
            )

    def mostrar_simplificado(self):
        if self.clientes:
            for cliente in self.clientes:
                print(cliente.resumenClient())
        else:
            print("La lista esta Vacia")

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for cliente in self.clientes:
            if cliente.dni == codigo_a_buscar:
                return cliente
        return None
