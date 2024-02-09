from modulos.Detalle import detalle
from modulos.Partida import partida
from modulos.Saldos import saldos

pathIn = './PDA_Dic.xlsx'
strOut = 'Dicv1.sql'


detalle(pathIn, strOut)
partida(pathIn, strOut)
saldos(pathIn, strOut)
