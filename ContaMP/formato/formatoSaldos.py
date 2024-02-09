from string import Template
from classes.ContaDatos import datosContabilidad
from classes.cuentas import cuentasContables

def crearPlantillaSaldos(arraySaldos, path_out):

    flag = 0

    for i in cuentasContables:
        if str(arraySaldos.get_cuenta()) == str(i[0]):
            flag = 1
            for j in i:
                crearPlantillaSQL(arraySaldos, j, path_out)

    if flag == 0:
        print('================================================')
        print('Cuenta no coincide: ' + str(arraySaldos.get_cuenta()))
        print('Partida: ' + arraySaldos.get_numPartida())
        print(arraySaldos.get_tipopar())
        print('================================================')


def crearPlantillaSQL(arraySaldos, cuenta, path_out):

    if str(cuenta)[0:1] == '1' or str(cuenta)[0:1] == '5':
        template_file = open('template/formatoActivo.txt')
    else:
        template_file = open('template/formatoPasivo.txt')


    values_dict = {
        'tipopar': arraySaldos.get_tipopar(),
        'numPartida': arraySaldos.get_numPartida(),
        'detallePartida': arraySaldos.get_detallePartida(),
        'detalleFecha': arraySaldos.get_detalleFecha(),
        'salFecha': arraySaldos.get_salFecha(),
        'cuenta': cuenta,
        'cargo': arraySaldos.get_cargo(),
        'abono': arraySaldos.get_abono(),
        'movimiento': arraySaldos.get_movimiento()
    }

    base_template = Template(template_file.read())

    result = base_template.substitute(values_dict)

    output_file = open(path_out, 'a')
    output_file.write(result)
