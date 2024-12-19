# Clients Class
class Cliente:
    def __init__(self, cod, surname_name, fecha):
        self.dni = int(cod)
        self.surname_name = surname_name
        self.fecha_nacimiento = fecha

    def __repr__(self) -> str:
        return (
            f"══════════════════════════════════════════\n"
            f"          Cliente: {self.surname_name}\n"
            f"══════════════════════════════════════════\n"
            f"  DNI:                    {self.dni}\n"
            f"  Fecha de Nacimiento:    {self.fecha_nacimiento}\n"
            f"══════════════════════════════════════════\n"
        )

    def resumenClient(self):
        return f"DNI: {self.dni} - Nombre y Apellido: {self.surname_name}"
