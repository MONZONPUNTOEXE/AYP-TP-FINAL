class GestorPedidos:
    def __init__(self) -> None:
        self.pedidos: list[Order] = []

    def __str__(self) -> str:
        if len(self.pedidos) > 0:
            return str(self.pedidos)
        else:
            return colors.WARNING + "No hay pedidos cargados actualmente" + colors.RESET

    def validarListaVacia(self):
        if len(self.pedidos) > 0:
            return True
        else:
            return None

    def mostrar_todos(self):
        if self.pedidos:
            print("Listando los Pedidos disponibles")
            for pedido in self.pedidos:
                print(pedido)
        else:
            print(
                colors.WARNING
                + "No hay pedidos cargados hasta el momento"
                + colors.RESET
            )

    def mostrar_simplificado(self):
        if self.pedidos:
            for pedido in self.pedidos:
                print(pedido.resumenOrden())
        else:
            print(colors.WARNING + "La lista esta Vacia" + colors.RESET)

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for pedido in self.pedidos:
            if pedido.id_order == codigo_a_buscar:
                return pedido
        return None

    def create_order_cod(self):
        return len(self.pedidos) + 1
