from report import *
from file import *
from datacontainer import *
from website import *

import collections

## things in computer files:
#### companies for initial input
#### relevant websites for data collection for each company
#### relevant key words for each company
#### relevant news sites to check
#### portfolio websites
#### folder of reports
## will have following classes:
###### stocks, portfolios, news articles, companies

def clean_split(string, delim='\n', generator=False):
    """
    Split a string with a delimiter and remove any empty elements.

    :param string: the string to split
    :param delim: the delimiter to split the string with, default is \\n
    :param generator: option to return a generator, default is False
    :return: a list that is split without empty values
    """
    _list = string.split(delim)
    if (generator == False):
        return [_ for _ in _list if len(_) > 0]
    elif (generator == True):
        return (_ for _ in _list if len(_) > 0)

def main():
    # pull names from file
    relevant_stocks = File("C:\\Users\\Michael Zhang\\Documents\\testing01.txt")
    contents = relevant_stocks.read_all().strip()
    company_info = (grouping for grouping in contents.split("\n"))
    companies = []
    for grouping in company_info:
        company_fields = grouping.split(', ')
        Company = collections.namedtuple('Company', 'name stock_symbol')
        c = Company(*company_fields)
        companies.append(c)
    #relevant_stocks.companies = [_.split(', ') for _ in _list]
    # access their websites for their information
    for company in companies:
        print(company)
        
    # do analysis on their information
    # format data
    # contruct a report
    # send the report

main()
