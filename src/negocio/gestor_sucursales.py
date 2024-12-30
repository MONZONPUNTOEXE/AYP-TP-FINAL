from clases.sucursal import Sucursal
from utils.colors_text import yellow_text


class GestorSucursales:
    def __init__(self) -> None:
        self.sucursales: list[Sucursal] = []

    def __str__(self) -> str:
        if len(self.sucursales) > 0:
            return str(self.sucursales)
        else:
            return yellow_text("No hay sucursales actualmente")

    def validarListaVacia(self):
        if len(self.sucursales) > 0:
            return True
        else:
            return None

    def mostrar_todos(self):
        if self.sucursales:
            print("Listando las Sucursales disponibles")
            for sucursal in self.sucursales:
                print(sucursal)
        else:
            print(yellow_text("No hay Sucursales cargados hasta el momento"))

    def mostrar_simplificado(self):
        if self.sucursales:
            for sucursal in self.sucursales:
                print(sucursal.resumen_sucursal())
        else:
            print(yellow_text("La lista esta Vacia"))

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for sucursal in self.sucursales:
            if sucursal.id_sucursal == codigo_a_buscar:
                return sucursal
        return None

    def create_sucursal_cod(self):
        return len(self.sucursales) + 1


gestor_de_sucursal = GestorSucursales()
