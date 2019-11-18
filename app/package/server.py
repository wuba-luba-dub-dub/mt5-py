from datetime import datetime
from MetaTrader5 import *
from pytz import timezone
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
utc_tz = timezone('UTC')

class conexionMT5:
    
    def __init__(self,divisa):
        self.divisa=divisa
        self.ticks = ''
        self.rates = ''

    def getTicksFromMT5(
                        self,
                        startYear,
                        startMonth,
                        startDay,
                        startHour,
                        endYear,
                        endMonth,
                        endDay,
                        endHour):

        self.divisa = self.divisa
        self.startYear = startYear
        self.startMonth = startMonth
        self.startDay = startDay
        self.startHour = startHour
        self.endYear = endYear
        self.endMonth = endMonth
        self.endDay = endDay
        self.endHour = endHour

        MT5Initialize()
        MT5WaitForTerminal()
        ticks = MT5CopyTicksRange(self.divisa, 
                                datetime(self.startYear,
                                self.startMonth,
                                self.startDay,
                                self.startHour), 
                                datetime(self.endYear,
                                self.endMonth,
                                self.endDay,
                                self.endHour), 
                                MT5_COPY_TICKS_ALL)
        rates = MT5CopyRatesRange(self.divisa,
                                MT5_TIMEFRAME_M1, 
                                datetime(self.startYear,
                                self.startMonth,
                                self.startDay,
                                self.startHour),
                                datetime(self.endYear,
                                self.endMonth,
                                self.endDay,
                                self.endHour), 
                                )
        self.ticks = ticks
        MT5Shutdown()
        return self.ticks

    def getRatesFromMT5(
                        self,
                        startYear,
                        startMonth,
                        startDay,
                        startHour,
                        endYear,
                        endMonth,
                        endDay,
                        endHour):

        self.divisa = self.divisa
        self.startYear = startYear
        self.startMonth = startMonth
        self.startDay = startDay
        self.startHour = startHour
        self.endYear = endYear
        self.endMonth = endMonth
        self.endDay = endDay
        self.endHour = endHour

        MT5Initialize()
        MT5WaitForTerminal()
        rates = MT5CopyRatesRange(self.divisa,
                                MT5_TIMEFRAME_M1, 
                                datetime(self.startYear,
                                self.startMonth,
                                self.startDay,
                                self.startHour),
                                datetime(self.endYear,
                                self.endMonth,
                                self.endDay,
                                self.endHour), 
                                )
        self.rates = rates
        MT5Shutdown()
        return self.rates


    def showPlottingGraficaLineal(self,divisa,ticks,rates):
        self.divisa = divisa
        self.ticks = ticks
        self.rates = rates
        
        x_time = [x.time.astimezone(utc_tz) for x in self.ticks]
        # prepare Bid and Ask arrays
        bid = [y.bid for y in self.ticks]
        ask = [y.ask for y in self.ticks]
 
        # draw ticks on the chart
        plt.figure(1)
        plt.plot(x_time, ask,'r-', label='ask')
        plt.plot(x_time, bid,'g-', label='bid')
        # display legends 
        plt.legend(loc='upper left')
            # display header 
        plt.title(self.divisa+ ' ticks')
        # display the chart
        plt.show()

    
divisaEURUSD=conexionMT5('EURUSD')
divisaEURUSD.getTicksFromMT5(2019,11,14,5,2019,11,14,6)
divisaEURUSD.getRatesFromMT5(2019,11,14,5,2019,11,14,6)
print(divisaEURUSD.divisa + '_ticks(', len(divisaEURUSD.ticks), ')')
for val in divisaEURUSD.ticks[:10]: print(val)
print(divisaEURUSD.divisa + '_rates(', len(divisaEURUSD.rates), ')')
for val in divisaEURUSD.rates[:10]: print (val)