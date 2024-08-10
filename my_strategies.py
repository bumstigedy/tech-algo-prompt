from backtesting import Backtest, Strategy
import pandas as pd
import talib
from backtesting.lib import crossover
#

def custom_ind(indicator):
    """ use to create a custom indicator"""
    return indicator
################### MACD crossover #######################################################################################################################
class MACDStrategy(Strategy):
    # MACD default parameters
    fastperiod = 12
    slowperiod = 26
    signalperiod = 9
    
    def init(self):
        # Compute MACD and MACD Signal
        macd, macdsignal, macdhist = self.I(talib.MACD, self.data['Adj Close'], 
                                            fastperiod=self.fastperiod, 
                                            slowperiod=self.slowperiod, 
                                            signalperiod=self.signalperiod)
        self.macd = macd
        self.macdsignal = macdsignal

        # Compute 20-day and 100-day EMA
        self.ema20 = self.I(talib.EMA, self.data['Adj Close'], timeperiod=20)
        self.ema100 = self.I(talib.EMA, self.data['Adj Close'], timeperiod=100)

    def next(self):
        if (crossover(self.macd, self.macdsignal) and 
            self.ema20[-1] > self.ema100[-1]):
            self.buy()

        if (crossover(self.macdsignal, self.macd) or 
            self.ema20[-1] < self.ema100[-1]):
            self.position.close()
####################### RSI with low volatility##########################################################################################################
class ATRRSIStrategy(Strategy):
    atr_short_period = 14
    atr_long_period = 100
    buy_threshold = 30
    sell_threshold = 70

    def init(self):
        # Initialize RSI
        self.rsi = self.I(talib.RSI, self.data['Adj Close'], timeperiod=14)
        # Initialize ATR
        self.atr_short = self.I(talib.ATR, self.data['High'], self.data['Low'], self.data['Adj Close'], timeperiod=self.atr_short_period)
        self.atr_long = self.I(talib.ATR, self.data['High'], self.data['Low'], self.data['Adj Close'], timeperiod=self.atr_long_period)

    def next(self):
        # Buy condition
        if self.rsi[-1] < self.buy_threshold and self.atr_short[-1] < self.atr_long[-1]:
            self.buy()
        # Sell condition
        elif self.position and (self.rsi[-1] > self.sell_threshold or self.atr_short[-1] > self.atr_long[-1]):
            self.position.close()

############## test strategies ##########################################################################################################################
if __name__ == "__main__":
    df=pd.read_csv(r'BTC-USD.csv', index_col='Date',parse_dates=True)
    df=df.dropna()    
    df=df[df.index >= pd.to_datetime('2023-01-01')]
    print("----------MACD----------------")
    bt =Backtest(df, MACDStrategy, cash=100_000)
    stats = bt.run()
    print(stats)
    bt.plot(filename='test_plot.html')
    #
    print("----------rsi----------------")
    bt =Backtest(df, ATRRSIStrategy, cash=100_000)
    stats = bt.run()
    print(stats)
    bt.plot(filename='test_plot.html')

