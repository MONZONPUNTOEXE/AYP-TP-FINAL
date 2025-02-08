from clases.perdidas import Perdidas
from utils.colors_text import yellow_text, red_text, green_text


class GestorPerdidas:
    def __init__(self) -> None:
        self.perdidas_list = [Perdidas]

    def __str__(self):
        if len(self.perdidas_list) > 0:
            return str(self.perdidas_list)
        else:
            return yellow_text("No hay Perdidas Cargadas actualmente")

    def validarListaVacia(self):
        if len(self.perdidas_list) > 0:
            return True
        else:
            return None

    def eliminar_producto(self, producto_a_eliminar: Perdidas):
        self.perdidas_list.remove(producto_a_eliminar)

    def mostrar_todos(self):
        if self.perdidas_list:
            print("Listando los Productos disponibles")
            for perdida in self.perdidas_list:
                print(green_text(perdida))
        else:
            print(red_text("No hay Perdidas cargadas hasta el momento"))

    # Verificar esto!
    def mostrar_simplificado(self):
        if self.perdidas_list:
            for perdida in self.perdidas_list:
                print(perdida.resumenPerdida())
        else:
            print("La lista esta Vacia")

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for perdida in self.perdidas_list:
            if perdida.id_perdida == codigo_a_buscar:
                return perdida
        return None

    def obtener_nuevo_codigo(self):
        return len(self.perdidas_list) + 1


gestor_perdidas = GestorPerdidas()
