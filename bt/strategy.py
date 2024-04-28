


class Strategy:

    def __init__(self,market,nearby,feature_generator, params):

        self.market = market
        self.nearby = nearby
        self.feature_generator = feature_generator #this is a function that takes output features and targets

    def on_data(self, datapath):
        ...

    def on_strategy(self):
        #To be implemented in child class
        ...

    def on_signal(self):
        # Signal is generated here, output is a dataframe containing daily signals (TimeStamp as index and Product Ticker as columns)

        ...


    def on_backtest(self):

        ...

    def run(self):

        ...



