from leccion02_modulo04_portafolio.cuenta_bancaria_mvc.repository.cuenta_bancaria_repository import *


def imprimir_cuenta_bancaria_cliente():
    imprimir = base_datos_cuenta_bancaria().__str__()
    print(imprimir)
    return imprimir


def imprimir_todos_los_clientes():
    all_clientes = base_datos_cuenta_bancaria().__str__()
    return all_clientes

def main():
    #imprimir_cuenta_bancaria_cliente()
    #imprimir_todos_los_clientes()
    return imprimir_cuenta_bancaria_cliente()
