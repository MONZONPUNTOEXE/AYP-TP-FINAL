from clases.pedido import Order
from utils.colors_text import yellow_text


class GestorPedidos:
    def __init__(self) -> None:
        self.pedidos: list[Order] = []

    def __str__(self) -> str:
        if len(self.pedidos) > 0:
            return str(self.pedidos)
        else:
            return yellow_text("No hay pedidos cargados actualmente")

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
            print(yellow_text("No hay pedidos cargados actualmente"))

    def mostrar_simplificado(self):
        if self.pedidos:
            for pedido in self.pedidos:
                print(pedido.resumenOrden())
        else:
            print(yellow_text("la Lista esta Vacia"))

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for pedido in self.pedidos:
            if pedido.id_order == codigo_a_buscar:
                return pedido
        return None

    def create_order_cod(self):
        return len(self.pedidos) + 1


gestor_de_pedidos = GestorPedidos()
