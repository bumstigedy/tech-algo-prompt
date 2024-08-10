A few notes: I had to force it write the code using Adj Close instead of close  sometimes it uses self.sell() instead of self.position.close() so I had to specify that in the prompt.  The first time it never closed the position I told this to chatGPT and it revised the code correctly.   


I have a python data frame with "Open", "High", "Low", and "Adj Close" data.  The close price is ["Adj Close"] not Close 
write python code using the following libraries: """backtesting.py and ta-lib.py"""  to create a backtest strategy to buy when the following conditions are met: """MACD crosses above the signal line and the 20 day ema is above the 100 day ema"""  and to close the position when the following conditions are met: """MACD crosses below the signal line or the 20 day ema crosses below the 100 day ema"""  make the MACD fast, slow, and signal periods class variables and set them to the default values


I have a python data frame with "Open", "High", "Low", and "Adj Close" data.  
write python code using the following libraries: """backtesting.py and ta-lib.py"""  to create a backtest strategy to buy when the following conditions are met: """RSI is below buy_threshold AND the 14 day ATR is below the 100 day ATR"""  and to close the position using self.positoin.close () when the following conditions are met: """RSI is above sell_threshold OR the 14 day ATR is above the 100 day ATR  make the atr time periods class variables  set buy_threshold to 30 and sell_threshold to 70"""