from clases.producto import Producto
from utils.colors_text import yellow_text, red_text, green_text


class gestorProductos:
    def __init__(self):
        self.productos: list[Producto] = []

    def __str__(self):
        if len(self.productos) > 0:
            return str(self.productos)
        else:
            return yellow_text("No hay productos Cargados actualmente")

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
                print(green_text(producto))
        else:
            print(red_text("No hay productos cargados hasta el momento"))

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


gestor_de_productos = gestorProductos()
