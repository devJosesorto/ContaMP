import openpyxl
from classes.ContaDatos import datosContabilidad
from formato.formatoPartida import crearPlantillaPartida


def partida(pathIn, strOut):
    """
    Esta funcion procesa un archivo de Excel que contiene datos de contabilidad y crea una serie de plantillas de partida
    en un archivo de salida especificado.

    Args:
        pathIn (str): La ruta al archivo de Excel de entrada.
        strOut (str): La ruta al archivo de salida donde se guardaran las plantillas de partida.

    Returns:
        None

    Example:
        partida('entrada.xlsx', 'salida.txt')
    """
    path = pathIn
    path_out = strOut

    book = openpyxl.load_workbook(path.strip(), data_only=True)
    sheet = book['Partidas']

    cont = 0
    fila = 2
    contaData = list()

    while cont == 0:
        datosExcel = datosContabilidad()
        datosExcel.set_tipopar(sheet['A' + str(fila)].value)
        datosExcel.set_numPartida(sheet['B' + str(fila)].value)
        datosExcel.set_detallePartida(sheet['C' + str(fila)].value)
        datosExcel.set_detalleFecha(sheet['D' + str(fila)].value)
        datosExcel.set_salFecha(sheet['E' + str(fila)].value)
        datosExcel.set_cuenta(sheet['F' + str(fila)].value)
        datosExcel.set_cargo(sheet['G' + str(fila)].value)
        datosExcel.set_abono(sheet['H' + str(fila)].value)
        datosExcel.set_movimiento(sheet['I' + str(fila)].value)
        datosExcel.set_fecha(sheet['J' + str(fila)].value)
        contaData.append(datosExcel)
        fila = fila + 1
        if sheet['A' + str(fila)].value is None:
            cont = 1

    for i in contaData:
        output_file = open(path_out, 'a')
        output_file.write(
            '/****** ============================================================================================== ******/\n')
        output_file.close()

        crearPlantillaPartida(i, path_out)

    print('Partida finalizado')
