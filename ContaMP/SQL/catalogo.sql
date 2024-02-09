-- Selecciona las filas numeradas y la cuenta en la tabla Catalogo con es_detalle = 1 y las guarda en una tabla temporal #Cuentas
SELECT ROW_NUMBER() OVER (ORDER BY cuenta) [Numero], cuenta
INTO #Cuentas
FROM [PHDATA_SBA].[dbo].[Catalogo]
WHERE es_detalle = 1

-- Declaración de variables
DECLARE @i INT = 1
DECLARE @Total INT = (SELECT COUNT(*) FROM #Cuentas)

-- Comienza un bucle WHILE que se ejecuta mientras @i sea menor o igual a @Total
WHILE @i <= @Total
BEGIN
    -- Obtiene la cuenta en la posición @i de la tabla temporal
    DECLARE @cuenta VARCHAR(300) = (SELECT cuenta FROM #Cuentas WHERE [Numero] = @i)

    -- Declaración de variables para construir una cadena
    DECLARE @StrNAME VARCHAR(300) = '	['
    DECLARE @var0 VARCHAR(100)
    DECLARE @var1 VARCHAR(300)
    DECLARE @var2 VARCHAR(300)
    DECLARE @flag INT = 0

    -- Obtiene el valor de 'nombrecta' desde la tabla Catalogo donde la cuenta coincide con @cuenta
    SELECT @var0 = nombrecta
    FROM [PHDATA_SBA].[dbo].[Catalogo]
    WHERE cuenta = @cuenta

    -- Comienza un bucle WHILE anidado que se ejecuta mientras @flag sea menor o igual a 9
    WHILE @flag <= 9
    BEGIN
        -- Obtiene la cuenta desde la tabla Catalogo donde la cuenta coincide con @cuenta
        SELECT @var1 = cuenta
        FROM [PHDATA_SBA].[dbo].[Catalogo]
        WHERE cuenta = @cuenta

        -- Obtiene el valor de 'anterior' desde la tabla Catalogo donde la cuenta coincide con @cuenta
        SELECT @var2 = anterior
        FROM [PHDATA_SBA].[dbo].[Catalogo]
        WHERE cuenta = @cuenta

        -- Concatena @var1 a la cadena @StrNAME
        SET @StrNAME = CONCAT(@StrNAME, @var1, ',')

        -- Si @var2 es menor que 10, establece @flag en 100 para salir del bucle interno
        IF @var2 < 10
            SET @flag = 100

        -- Actualiza @cuenta con el valor de @var2
        SET @cuenta = @var2
    END

    -- Concatena @var2 y ']' a la cadena @StrNAME
    SET @StrNAME = CONCAT(@StrNAME, @var2, ']')

    -- Imprime el valor de @var0 (nombrecta)
    PRINT(CONCAT('#', @var0))

    -- Imprime la cadena construida @StrNAME
    PRINT @StrNAME

    -- Incrementa @i en 1 para pasar a la siguiente fila en la tabla temporal #Cuentas
    SET @i = @i + 1
END

-- Elimina la tabla temporal #Cuentas
DROP TABLE #Cuentas
