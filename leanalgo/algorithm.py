"""
Basic QuantConnect Algorithm Example
"""

from AlgorithmImports import *

class BasicAlgorithm(QCAlgorithm):
    """
    Basic algorithm that initializes and sets up a simple AAPL trading strategy.
    """
    
    def Initialize(self):
        """
        Initialize the algorithm with required settings.
        """
        self.SetStartDate(2020, 1, 1)    # Set Start Date
        self.SetEndDate(2021, 1, 1)      # Set End Date
        self.SetCash(100000)             # Set Strategy Cash
        
        # Add equity data
        self.symbol = self.AddEquity("AAPL", Resolution.Daily).Symbol
        
        # Use Simple Moving Average indicator
        self.sma = self.SMA(self.symbol, 14, Resolution.Daily)
        
        # Set warmup to allow indicators to be ready
        self.SetWarmUp(14)
    
    def OnData(self, data):
        """
        OnData event is the primary entry point for algorithm logic.
        """
        if self.IsWarmingUp:
            return
        
        # Simple strategy: buy when price > SMA, sell when price < SMA
        if not self.Portfolio.Invested:
            if data[self.symbol].Close > self.sma.Current.Value:
                self.SetHoldings(self.symbol, 1.0)
                self.Log(f"Buying {self.symbol} at {data[self.symbol].Close}")
        elif data[self.symbol].Close < self.sma.Current.Value:
            self.Liquidate(self.symbol)
            self.Log(f"Selling {self.symbol} at {data[self.symbol].Close}") 