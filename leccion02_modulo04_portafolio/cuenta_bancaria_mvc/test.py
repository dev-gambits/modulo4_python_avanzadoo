# Definir la clase Cliente
class Cliente:
    def __init__(self, id_cliente: int, rut: str, nombre: str,
                 apellido_paterno: str, apellido_materno: str,
                 edad: int, sexo: str, tipo_cuenta: str, saldo: float,
                 direccion: str, email: str, celular: str):
        self.id_cliente = id_cliente
        self.rut = rut
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.edad = edad
        self.sexo = sexo
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo
        self.direccion = direccion
        self.email = email
        self.celular = celular

    def __str__(self) -> str:
        return (f"ID Cliente: {self.id_cliente}\n"
                f"RUT: {self.rut}\n"
                f"Nombre: {self.nombre}\n"
                f"Apellido Paterno: {self.apellido_paterno}\n"
                f"Apellido Materno: {self.apellido_materno}\n"
                f"Edad: {self.edad}\n"
                f"Sexo: {self.sexo}\n"
                f"Tipo de Cuenta: {self.tipo_cuenta}\n"
                f"Saldo: {self.saldo}\n"
                f"Dirección: {self.direccion}\n"
                f"Email: {self.email}\n"
                f"Celular: {self.celular}\n")

# Crear 10 objetos Cliente y guardarlos en una lista
clientes = []
for i in range(10):
    cliente = Cliente(id_cliente=i+1, rut=f"1234567{i}-9", nombre=f"Cliente {i+1}", apellido_paterno="Apellido",
                      apellido_materno="Materno", edad=30 + i, sexo="Masculino", tipo_cuenta="Corriente",
                      saldo=1000.0 + (i * 100), direccion=f"Calle {i+1} #123", email=f"cliente{i+1}@example.com",
                      celular=f"98765432{i}")
    clientes.append(cliente)

# Imprimir la lista de clientes
for cliente in clientes:
    print(cliente)
