from MetaTrader5 import *
from datetime import date
from pytz import timezone
import pandas as pd 
import matplotlib.pyplot as plt2
utc_tz = timezone('UTC')

class Correlacion:
    def __init__(self,divisa1,divisa2,divisa3,divisa4):
        self.divisa1 = divisa1
        self.divisa2 = divisa2
        self.divisa3 = divisa3
        self.divisa4 = divisa4


    def showCorrelacion(self):
        self.divisa1 = self.divisa1
        self.divisa2 = self.divisa2
        self.divisa3 = self.divisa3
        self.divisa4 = self.divisa4
        
        MT5Initialize()
        MT5WaitForTerminal()

        sym = [self.divisa1,self.divisa2,self.divisa3,self.divisa4]
        d = pd.DataFrame()

        for i in sym:
            rates = MT5CopyRatesFromPos(i, MT5_TIMEFRAME_M1, 0, 1000)
            d[i] = [y.close for y in rates]
        MT5Shutdown()

        # Compute Percentage Change
        rets = d.pct_change()

        # Compute Correlation
        corr = rets.corr()

        # Plot correlation matrix
        plt2.figure(figsize=(10, 10))
        plt2.imshow(corr, cmap='RdYlGn', interpolation='none', aspect='auto')
        plt2.colorbar()
        plt2.xticks(range(len(corr)), corr.columns, rotation='vertical')
        plt2.yticks(range(len(corr)), corr.columns)
        plt2.suptitle('FOREX Correlations Heat Map', fontsize=15, fontweight='bold')
        plt2.show()
