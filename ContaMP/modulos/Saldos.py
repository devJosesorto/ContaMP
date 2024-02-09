import openpyxl
from classes.ContaDatos import datosContabilidad


from formato.formatoSaldos import crearPlantillaSaldos


def saldos(pathIn, strOut):
    path = pathIn
    path_out = strOut

    book = openpyxl.load_workbook(path.strip(), data_only=True)
    sheet = book['Saldos']

    cont = 0
    fila = 2
    contaData = list()

    print()
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

        crearPlantillaSaldos(i, path_out)

    print('Saldos finalizado')
