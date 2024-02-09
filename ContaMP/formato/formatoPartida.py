from string import Template
from classes.ContaDatos import datosContabilidad


def crearPlantillaPartida(arrayPartida, path_out):

    template_file = open('template/formatoPartida.txt')

    values_dict = {
        'tipopar': arrayPartida.get_tipopar(),
        'numPartida': arrayPartida.get_numPartida(),
        'detallePartida': arrayPartida.get_detallePartida(),
        'detalleFecha': arrayPartida.get_detalleFecha(),
        'salFecha': arrayPartida.get_salFecha(),
        'fechacreacion': arrayPartida.get_detalleFecha()
    }

    base_template = Template(template_file.read())

    result = base_template.substitute(values_dict)

    output_file = open(path_out, 'a')
    output_file.write(result)
