from pickle import dumps, load
import os


def escribir_en_binario_productos():
    global gestor_de_productos
    with open("./bin/productos.bin", "wb") as bin_file:
        bin_file.write(dumps(clases.gestor_de_productos.productos))


def escribir_en_binario_clientes():
    global gestor_de_clientes
    with open("./bin/clientes.bin", "wb") as bin_file:
        bin_file.write(dumps(clases.gestor_de_clientes.clientes))


def escribir_en_binario_pedidos():
    global gestor_de_pedidos
    with open("./bin/pedidos.bin", "wb") as bin_file:
        bin_file.write(dumps(clases.gestor_de_pedidos.pedidos))


def escribir_en_binario_sucursales():
    global gestor_de_productos
    with open("./bin/sucursales.bin", "wb") as bin_file:
        bin_file.write(dumps(clases.gestor_de_sucursal.sucursales))


# Cargar binarios
def cargar_desde_binario_productos():
    global gestor_de_productos
    with open("productos.bin", "rb") as bin_file:
        clases.gestor_de_productos.productos = load(bin_file)


def cargar_desde_binario_clientes():
    global gestor_de_clientes
    with open("clientes.bin", "rb") as bin_file:
        clases.gestor_de_clientes.clientes = load(bin_file)


def cargar_desde_binario_pedidos():
    global gestor_de_pedidos
    with open("pedidos.bin", "rb") as bin_file:
        clases.gestor_de_pedidos.pedidos = load(bin_file)


def permanenciaDeArchivos():
    dirs = os.listdir()
    for directory in dirs:
        if directory == "bin":
            print("La carpeta bin existe")
            print("Cargando la carpeta 'bin'...")
            break
    else:
        print("La Carpeta 'bin' no existe")
        print("Creando la Carpeta 'bin'...")
        os.mkdir("bin")
        print("La Carpeta 'bin' ha sido creada")
    os.chdir("./bin")
    files = os.listdir()
    for bin in files:
        print(bin)
        print("Cargando los binarios...")
        if bin == "productos.bin":
            print("Cargando 'productos.bin'...")
            cargar_desde_binario_productos()
            print("'productos.bin' Se ha cargado exitosamente.")
        elif bin == "clientes.bin":
            print("Cargando 'clientes.bin'...")
            cargar_desde_binario_clientes()
            print("'clientes.bin' Se haa cargado exitosamente.")
        elif bin == "pedidos.bin":
            print("Cargando 'pedidos.bin'...")
            cargar_desde_binario_pedidos()
            print("'pedidos.bin' Se ha cargado exitosamente.")
    os.chdir("..")
