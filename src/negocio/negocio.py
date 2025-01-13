from negocio.gestor_pedidos import gestor_de_pedidos


# fucion de Carrito
def subtotalCarrito(carrito) -> float:
    suma = 0
    for producto in carrito:
        suma += producto.product_price
    return float(suma)


def mostrarCarrito(carrito: list):
    for producto in carrito:
        print(f"{producto.product_name} ${producto.product_price}")


# Subrrayado de texto
def graphi(text):
    width = len(text)
    print("-" * width)
    print(text)


# ordenar por TOTAL (marge sort)
def mezclar_por_total(lista, inicio, medio, fin):
    izquierda = lista[inicio: medio + 1]
    derecha = lista[medio + 1: fin + 1]

    i = j = 0
    k = inicio

    # Mezcla las dos mitades
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i].total <= derecha[j].total:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    # Copia los elementos restantes de la mitad izquierda, si los hay
    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    # Copia los elementos restantes de la mitad derecha, si los hay
    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1


def marge_sort_total_order(lista, inicio, fin):
    if inicio < fin:
        medio = (inicio + fin) // 2  # Encuentra el punto medio
        marge_sort_total_order(lista, inicio, medio)
        marge_sort_total_order(lista, medio + 1, fin)

        mezclar_por_total(lista, inicio, medio, fin)


def ordenar_por_merge_sort_por_total():
    global gestor_de_pedidos
    lista_de_pedidos = gestor_de_pedidos.pedidos
    marge_sort_total_order(lista_de_pedidos, 0, len(lista_de_pedidos) - 1)
    print(lista_de_pedidos)
