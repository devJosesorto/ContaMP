import openpyxl
from classes.ContaDatos import datosContabilidad
from formato.formatoDetalle import crearPlantillaDetalle


def detalle(pathIn, strOut):
    """
    Esta funcion procesa un archivo de Excel y genera un archivo de salida en formato detallado.

    :param pathIn: La ruta de entrada del archivo de Excel.
    :type pathIn: str
    :param strOut: La ruta de salida para el archivo generado.
    :type strOut: str
    """
    # Almacena las rutas de entrada y salida
    path = pathIn
    path_out = strOut

    # Carga el libro de Excel especificado en la ruta de entrada
    book = openpyxl.load_workbook(path.strip(), data_only=True)
    sheet = book['Detalle']  # Selecciona la hoja llamada 'Detalle'

    # Inicializa variables
    cont = 0
    fila = 2
    contaData = list()  # Lista para almacenar objetos de datosContabilidad

    # Inicia un bucle while que se ejecuta mientras "cont" sea igual a 0
    while cont == 0:
        # Crea un objeto datosContabilidad para almacenar los datos de cada fila en Excel
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

        # Agrega el objeto datosContabilidad a la lista contaData
        contaData.append(datosExcel)
        fila = fila + 1

        # Comprueba si el valor en la columna A de la siguiente fila es None para salir del bucle
        if sheet['A' + str(fila)].value is None:
            cont = 1

    # Itera a través de los objetos datosContabilidad en la lista
    for i in contaData:
        # Abre el archivo de salida en modo de anexar
        output_file = open(path_out, 'a')
        # Escribe una línea de separación en el archivo
        output_file.write(
            '/****** ============================================================================================== ******/\n')
        output_file.close()

        # Llama a la función crearPlantillaDetalle para procesar el objeto i y escribir en el archivo de salida
        crearPlantillaDetalle(i, path_out)

    # Imprime un mensaje de finalización
    print('Detalle finalizado')
