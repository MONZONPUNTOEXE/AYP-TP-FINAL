from negocio.gestor_clientes import gestor_de_clientes
from utils.gestion_archivos import escribir_en_binario_clientes
from clases.cliente import Cliente
from negocio.negocio import graphi
from utils.validaciones import dniValidate, validateClientName, intValidate


# create Cliente
def createClient():
    global gestor_de_clientes
    while True:
        cod = dniValidate()
        name = validateClientName()
        print("Ingrese la fecha de Nacimiento en este formato DD/MM/AAAA")
        date = gestor_de_clientes._pedir_fecha_nacimiento_valida()
        new_client = Cliente(cod, name, date)
        gestor_de_clientes.clientes.append(new_client)
        escribir_en_binario_clientes()
        print("Se ha creado un nuevo Cliente")
        print(new_client)
        user = input(f"hay un total de ({
                     len(gestor_de_clientes.clientes)}) Clientes desea ingresar mas ?: s/n ")
        if user.lower() == "n":
            break


# Update Cliente
def updateClient():
    global gestor_de_clientes
    gestor_de_clientes.mostrar_simplificado()
    client_code = intValidate("Ingrese el DNI del Cliente que desea modificar: ")
    client_encontrado = gestor_de_clientes.buscar_por_codigo(client_code)
    if client_encontrado:
        nuevo_nombre = input("Ingrese el nuevo nombre - (Enter para dejar el actual): ")
        dni_confirm = input(
            "Desea cambiar el DNI y Fecha de Nacimiento del Cliente ? S/n "
        )
        if dni_confirm.lower() in ("no", "n"):
            nuevo_id = ""
        else:
            nuevo_id = dniValidate()
        nuevo_fecha = gestor_de_clientes._pedir_fecha_nacimiento_valida()

        # cambios anteriores
        nombre_sin_cambio = client_encontrado.surname_name
        id_sin_cambio = client_encontrado.dni
        date_sin_cambio = client_encontrado.fecha_nacimiento

        text_sin_cambios = "Sin aplicar Cambios"
        graphi(text_sin_cambios)
        print(client_encontrado)

        if nuevo_nombre:
            client_encontrado.surname_name = nuevo_nombre
        if nuevo_id:
            client_encontrado.dni = nuevo_id
        if nuevo_fecha:
            client_encontrado.fecha_nacimiento = nuevo_fecha

        text_con_cambios = "Aplicando los cambios... "
        graphi(text_con_cambios)
        print(client_encontrado)

        decidir_cambios = input("Desea guardar los cambios ? - (Si/no)")
        if decidir_cambios.lower() in ("no", "n"):
            client_encontrado.surname_name = nombre_sin_cambio
            client_encontrado.dni = id_sin_cambio
            client_encontrado.fecha_nacimiento = date_sin_cambio
            print("El Cliente no se ha actualizado")
            escribir_en_binario_clientes()
        else:
            print("El Cliente se ha actualizado correctamente")
            escribir_en_binario_clientes()
            print(client_encontrado)
    else:
        print("El codigo no fue encontrado, intentelo nuevamente...")


# Delete Cliente
def deleteClient():
    global gestor_de_clientes
    gestor_de_clientes.mostrar_simplificado()
    code = intValidate("Ingrese el DNI del Cliente que desea Eliminar: ")
    client_encontrado = gestor_de_clientes.buscar_por_codigo(code)
    if client_encontrado:
        opcion = input(f"\n\tDesea eliminar ?\n\n{client_encontrado}\nS/n: ")
        if opcion.lower() in ("si", "s", "y", "yes" "ye"):
            gestor_de_clientes.clientes.remove(client_encontrado)
            escribir_en_binario_clientes()
            print(f"\n\tSe ha eliminado de la lista:\n{client_encontrado}")
        else:
            print("El cliente no ha sido eliminado...")
    else:
        print("El codigo no fue encontrado!")
