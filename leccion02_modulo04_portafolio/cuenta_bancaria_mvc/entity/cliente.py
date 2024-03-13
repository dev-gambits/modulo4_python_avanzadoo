class Cliente():
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

    ########################################################
    ##############    GETTER AND SETTER  ###################
    ########################################################
    def get_id_cliente(self):
        return self.id_cliente

    def set_id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    def get_rut(self):
        return self.rut

    def set_rut(self, rut):
        self.rut = rut

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido_paterno(self):
        return self.apellido_paterno

    def set_apellido_paterno(self, apellido_paterno):
        self.apellido_paterno = apellido_paterno

    def get_apellido_materno(self):
        return self.apellido_materno

    def set_apellido_materno(self, apellido_materno):
        self.apellido_materno = apellido_materno

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_sexo(self):
        return self.sexo

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_tipo_cuenta(self):
        return self.tipo_cuenta

    def set_tipo_cuenta(self, tipo_cuenta):
        self.tipo_cuenta = tipo_cuenta

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_celular(self):
        return self.celular

    def set_celular(self, celular):
        self.celular = celular

    ########################################################
    #####################    METHODS  ######################
    ########################################################
    def nombre_completo(self):
        nombre_completo = f"{self.get_nombre()} {self.get_apellido_paterno()} {self.get_apellido_materno()}"
        return nombre_completo


    ########################################################
    #####################    TO STRING  ####################
    ########################################################
    def __str__(self) -> str:
        to_string_cliente =\
            (f"\n\t########### DATOS DEL CLIENTE  #############\n\n"
                f"\t\tID Cliente:       {self.get_id_cliente()}\n"
                f"\t\tRUT:              {self.get_rut()}\n"
                f"\t\tNombre:           {self.get_nombre()}\n"
                f"\t\tApellido Paterno: {self.get_apellido_paterno()}\n"
                f"\t\tApellido Materno: {self.get_apellido_materno()}\n"
                f"\t\tEdad:             {self.get_edad()}\n"
                f"\t\tSexo:             {self.get_sexo()}\n"
                f"\t\tTipo de Cuenta:   {self.get_tipo_cuenta()}\n"
                f"\t\tSaldo:            $ {self.get_saldo()}\n"
                f"\t\tDirección:        {self.get_direccion()}\n"
                f"\t\tEmail:            {self.get_email()}\n"
                f"\t\tCelular:          {self.get_celular()}\n")
        return to_string_cliente