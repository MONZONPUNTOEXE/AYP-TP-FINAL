class gestorProductos:
    def __init__(self):
        self.productos: list[Producto] = []

    def __str__(self):
        if len(self.productos) > 0:
            return str(self.productos)
        else:
            return (
                colors.WARNING + "No hay productos Cargados actualmente" + colors.RESET
            )

    def validarListaVacia(self):
        if len(self.productos) > 0:
            return True
        else:
            return None

    def eliminar_producto(self, producto_a_eliminar: Producto):
        self.productos.remove(producto_a_eliminar)

    def mostrar_todos(self):
        if self.productos:
            print("Listando los Productos disponibles")
            for producto in self.productos:
                print(colors.OK, producto, colors.RESET)
        else:
            print(
                colors.FAIL, "No hay productos cargados hasta el momento", colors.RESET
            )

    def mostrar_simplificado(self):
        if self.productos:
            for producto in self.productos:
                print(producto.resumenProducto())
        else:
            print("La lista esta Vacia")

    def buscar_por_codigo(self, codigo_a_buscar: int):
        for producto in self.productos:
            if producto.ref_code == codigo_a_buscar:
                return producto
        return None

    def obtener_nuevo_codigo(self):
        return len(self.productos) + 1
