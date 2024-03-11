from leccion04_modulo04_portafolio.entidad.empleado import Empleado


class Gerente(Empleado):
    def __init__(self, cargo, nombre):
        super().__init__(nombre)
        self.cargo = cargo
