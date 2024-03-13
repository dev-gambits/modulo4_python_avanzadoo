from leccion02_modulo04_portafolio.cuenta_bancaria_mvc.entity.cliente import *


class CuentaBancaria:
    def __init__(self, id_cliente: Cliente, titular: str, saldo_inicial: float = 0):
        self.id_cliente = id_cliente
        self.titular = titular
        self.saldo_inicial = saldo_inicial

    ########################################################
    ##############    GETTER AND SETTER  ###################
    ########################################################
    def get_id_cliente(self):
        return self.id_cliente

    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_saldo_inicial(self):
        return self.saldo_inicial

    def set_saldo_inicial(self, saldo_inicial):
        self.saldo_inicial = saldo_inicial


    ## TO STRING
    def __str__(self):
        to_string_cuenta_bancaria = \
            (f"\n\t########### DATOS DE LA CUENTA BANCARIA  #############\n\n"
             f"\t\tID Cliente:      {self.get_id_cliente()}\n"
             f"\t\tTitular:         {self.get_titular()}\n"
             f"\t\tSaldo:           {self.get_saldo_inicial()}\n")
        return to_string_cuenta_bancaria
