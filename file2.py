import requests
import csv

class GetStockFinance(object):

    def __init__(self, url, stockindex):
        self.url = url
        self.stockindex = stockindex

    def get_stock_finance(self):
        download = requests.get(self.url+self.stockindex+'.csv')
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return list(cr)

    def new_met(self , csv_de_scris2):
       for i in csv_de_scris2:

class WriteToCsv(object):

    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, continut):
        with open(self.filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(continut)

class StockItem(object):
    def __init__(self,first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


# a = GetStockFinance('https://www.quandl.com/api/v3/datasets/WIKI/','AAPL')
# csv_de_scris = a.get_stock_finance()

        a2 = GetStockFinance('https://www.quandl.com/api/v3/datasets/WIKI/' , 'apple')
        csv_de_scris2 = a2.get_stock_finance()
        print(a2.new_met(csv_de_scris2))


q=set()
l=set()
m=set()
n=set()