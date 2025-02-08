from utils.fecha import Fecha


class Perdidas:
    def __init__(self, id_perdidas, perdida_id_product):
        self.id_perdidas = id_perdidas
        self.perdida_id_product = perdida_id_product
        self.date_perdidas = Fecha()
