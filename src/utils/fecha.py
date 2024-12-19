import re
import time
from datetime import datetime


class Fecha:
    def __init__(self, fecha_str: str = None):
        if not fecha_str:
            hoy = datetime.now()
            hora = time.localtime()
            self.hora = time.strftime("%H:%M:%S", hora)
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            # validar formato de fecha dd/mm/aaaa con expresiones regulres
            if not self.es_fecha_valida(fecha_str):
                raise ValueError(
                    colors.FAIL
                    + "Formato de fecha no válido. Debe ser dd/mm/aaaa"
                    + colors.RESET
                )
            partes = str(fecha_str).split("/")
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def es_fecha_valida(self, fecha: str):
        patron = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        return re.match(patron, fecha)

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anio} {self.hora}"
