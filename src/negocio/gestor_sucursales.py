class GestorSucursales:
    def __init__(self) -> None:
        self.sucursales: list[Sucursal] = []

    def __str__(self) -> str:
        if len(self.sucursales) > 0:
            return str(self.sucursales)
        else:
            return colors.WARNING + "No hay sucursales actualmente" + colors.RESET

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
            print(
                colors.WARNING
                + "No hay Sucursales cargados hasta el momento"
                + colors.RESET
            )

    def mostrar_simplificado(self):
        if self.sucursales:
            for sucursal in self.sucursales:
                print(sucursal.resumen_sucursal())
        else:
            print(colors.WARNING + "La lista esta Vacia" + colors.RESET)

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for sucursal in self.sucursales:
            if sucursal.id_sucursal == codigo_a_buscar:
                return sucursal
        return None

    def create_sucursal_cod(self):
        return len(self.sucursales) + 1
