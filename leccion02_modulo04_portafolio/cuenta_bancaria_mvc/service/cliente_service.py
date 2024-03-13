from leccion02_modulo04_portafolio.cuenta_bancaria_mvc.repository.cliente_repository import *


def imprimir_cliente():
    imprimir = base_datos_cliente().__str__()
    print(imprimir)
    return imprimir


def imprimir_todos_los_clientes():
    all_clientes = base_datos_cliente().__str__()
    return all_clientes

def main():
    imprimir_cliente()
    imprimir_todos_los_clientes()
    return imprimir_cliente()
