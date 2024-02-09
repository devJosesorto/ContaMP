SELECT ROW_NUMBER() over(order by cuenta) [Numero], cuenta
INTO #Cuentas
FROM [PHDATA_SBA].[dbo].[Catalogo]
where es_detalle = 1

DECLARE @i INT = 1
DECLARE @Total INT = (Select COUNT(*) from #Cuentas)

WHILE @i <= @Total
BEGIN
DECLARE @cuenta VARCHAR(300) = (Select cuenta from #Cuentas WHERE [Numero]=@i)



DECLARE @StrNAME VARCHAR(300) = '	['
DECLARE @var0 VARCHAR(100)
DECLARE @var1 VARCHAR(300)
DECLARE @var2 VARCHAR(300)
DECLARE @flag INT = 0

  SELECT @var0 = nombrecta
  FROM [PHDATA_SBA].[dbo].[Catalogo]
  where cuenta=@cuenta
	
  WHILE @flag<=9
  BEGIN

  SELECT @var1 = cuenta
  FROM [PHDATA_SBA].[dbo].[Catalogo]
  where cuenta=@cuenta  
  
  SELECT @var2 = anterior
  FROM [PHDATA_SBA].[dbo].[Catalogo]
  where cuenta=@cuenta

  SET @StrNAME = CONCAT(@StrNAME,@var1,',')

  IF @var2 <10
  SET @flag = 100
  
  SET @cuenta = @var2
  END

  SET @StrNAME = CONCAT(@StrNAME,@var2,'],')

 
  Print(CONCAT('#',@var0))
  PRINT @StrNAME


SET @i = @i + 1
END

DROP table #Cuentas