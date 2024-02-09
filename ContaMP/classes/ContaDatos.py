class datosContabilidad(object):

    def __init__(self):
        self.tipopar = ''
        self.numPartida = ''
        self.detallePartida = ''
        self.detalleFecha = ''
        self.salFecha = ''
        self.cuenta = ''
        self.cargo = ''
        self.abono = ''
        self.movimiento = ''
        self.fecha = ''

    def get_tipopar(self):
        return self.tipopar

    def get_numPartida(self):
        return self.numPartida

    def get_detallePartida(self):
        return self.detallePartida

    def get_detalleFecha(self):
        return self.detalleFecha

    def get_salFecha(self):
        return self.salFecha

    def get_cuenta(self):
        return self.cuenta

    def get_cargo(self):
        return self.cargo

    def get_abono(self):
        return self.abono

    def get_movimiento(self):
        return self.movimiento

    def get_fecha(self):
        return self.fecha2


    def set_tipopar(self, x):
        self.tipopar=x

    def set_numPartida(self, x):
        if x > 999:
            self.numPartida = '0' + str(x)
        elif x > 99:
            self.numPartida = '00'+str(x)
        elif x > 9:
            self.numPartida = '000' + str(x)
        else:
            self.numPartida = '0000' + str(x)

    def set_detallePartida(self, x):
        self.detallePartida = x

    def set_detalleFecha(self, x):
        self.detalleFecha = str(x).replace(' 00:00:00', '')

    def set_salFecha(self, x):
        self.salFecha = str(str(str(x).replace(' 00:00:00', '')).replace('-', ''))[0:6]

    def set_cuenta(self, x):
        self.cuenta=x

    def set_cargo(self, x):
        self.cargo=x

    def set_abono(self, x):
        self.abono=x

    def set_movimiento(self, x):
        self.movimiento=x

    def set_fecha(self, x):
        self.fecha2=x