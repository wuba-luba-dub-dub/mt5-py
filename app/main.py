from package import server
from package import correlacion

#view
correlacionDivisas =correlacion.Correlacion('EURUSD','USDCHF','GBPUSD','USDJPY')
correlacionDivisas.showCorrelacion()

#Instancia
divisaEURUSD=server.conexionMT5('EURUSD')
divisaEURUSD.getTicksFromMT5(2019,11,14,5,2019,11,14,6)
divisaEURUSD.getRatesFromMT5(2019,11,14,5,2019,11,14,6)
divisaEURUSD.showPlottingGraficaLineal(divisaEURUSD.divisa,divisaEURUSD.ticks,divisaEURUSD.rates)
#DATA
print(divisaEURUSD.divisa + '_ticks(', len(divisaEURUSD.ticks), ')')
for val in divisaEURUSD.ticks[:10]: print(val)
print(divisaEURUSD.divisa + '_rates(', len(divisaEURUSD.rates), ')')
for val in divisaEURUSD.rates[:10]: print (val)

