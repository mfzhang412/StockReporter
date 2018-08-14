from report import *
from file import *
from datacontainer import *
from website import *
from formulas import *

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

    
def get_companies_from_file(file):
    contents = relevant_stocks.read_all().strip()
    company_info = (grouping for grouping in contents.split("\n"))
    Company = collections.namedtuple('Company', 'name stock_symbol')
    companies = []
    for grouping in company_info:
        company_fields = grouping.split(', ')
        company = Company(*company_fields)
        companies.append(company)
    return companies


def main():
    # pull company names from file
    relevant_stocks = File("C:\\Users\\Michael Zhang\\Documents\\testing01.txt")
    companies = get_companies_from_file(relevant_stocks)
    # access their websites for their information
    # do analysis on the company's information and the company's stock information
    
    # pull portfolio links from file
    # access their websites for their information
    # do analysis on the portfolio's information
    
    # scrape web for news articles
    # access those news articles
    # do analysis on the news article's information
    
    # construct a report
    # send the report


main()
