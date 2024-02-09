from string import Template
from classes.ContaDatos import datosContabilidad


def crearPlantillaDetalle(arrayDetalle, path_out):

    detamv = 1

    if arrayDetalle.get_cargo() == 0:
        detamv = 2
    else:
        detamv = 1



    template_file = open('template/formatoDetalle.txt')

    values_dict = {
        'tipopar': arrayDetalle.get_tipopar(),
        'numPartida': arrayDetalle.get_numPartida(),
        'detallePartida': arrayDetalle.get_detallePartida(),
        'detalleFecha': arrayDetalle.get_detalleFecha(),
        'salFecha': arrayDetalle.get_salFecha(),
        'cuenta': arrayDetalle.get_cuenta(),
        'cargo': arrayDetalle.get_cargo(),
        'abono': arrayDetalle.get_abono(),
        'movimiento': detamv
    }

    base_template = Template(template_file.read())

    result = base_template.substitute(values_dict)

    output_file = open(path_out, 'a')
    output_file.write(result)

