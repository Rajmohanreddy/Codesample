import csv
import collections
def data_company():
    with open('data.csv') as f:  ## data.csv is a samplefile containing companies data in csv format 
        info = csv.reader(f)
        tup = collections.namedtuple('tup', ['price', 'year', 'month'])
        dic = collections.OrderedDict()
        names = next(info)[2:]
        for name in names:
            #initialize the dictinary
            dic[name] = tup(0, 'year', 'month')
        for row in info:
            year, month = row[:2]         
            for name, price in zip(names, map(int, row[2:])):
                if dic[name].price < price:
                    dic[name] = tup(price, year, month)
    return dic
data_company()
