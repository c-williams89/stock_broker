#!usr/bin/env python3
from typing import List, Tuple
from random import gauss
import json

class Broker:
    def __init__(self, ticker, name, start_price, std_dev, av_vol):
        self._ticker = ticker
        self._name = name
        self._start_price = start_price
        self._volatility : Tuple(float) = (av_vol, std_dev)
        self._price : List(float) = [start_price]

    @property
    def ticker(self):
        return self._ticker
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price[-1]
    
    @property
    def history(self):
        return self._price
    
    def increment_price(self):
        price_change = gauss(self._volatility[0], self._volatility[1])
        new_price = self._price[-1] + price_change
        self._price.append(new_price)

    def __str__(self) -> str:
        return f"Ticker: {self.ticker}\tCurrent Price: {self.price}"