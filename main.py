from report import *
from file import *
from datacontainer import *
from website import *
from formulas import *

from collections import namedtuple

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
    contents = file.read_all().strip()
    company_info = (grouping for grouping in contents.split('\n'))
    Company = namedtuple('Company', 'name stock_symbol')
    companies = []
    for info in company_info:
        company_fields = info.split(', ')
        company = Company(*company_fields)
        companies.append(company)
    return companies


def get_industries_from_file(file):
    contents = file.read_all().strip()
    industries_info = (grouping for grouping in contents.split('\n'))
    Industry = namedtuple('Industry', 'industry precedent dependent')
    industries = []
    for info in industries_info:
        industry_fields = info.split(', ')
        industry = Industry(*industry_fields)
        industries.append(industry)
    return industries
    

def get_portfolios_from_file(file):
    contents = file.read_all().strip()
    portfolio_info = contents.split('\n')
    Portfolio = namedtuple('Portfolio', 'url')
    portfolios = []
    for info in portfolio_info:
        portfolio = Portfolio(info)
        portfolios.append(portfolio)
    return portfolios


def main():
    # pull company names from file
    relevant_companies = File("C:\\Users\\Michael Zhang\\Documents\\testing01.txt")
    companies = get_companies_from_file(relevant_companies)
    # access their websites for their information (stocks and actual company info)
    # do analysis on the company's information and the company's stock information
    
    # pull industries and dependencies and reliances of the company
    relevant_industries = File("")
    industries = get_industries_from_file(relevant_industries)
    # access news related to the different industries and the performance of the industry
    # do analysis on this information
    
    # pull portfolio links from file
    relevant_portfolios = File("")
    portfolios = get_portfolios_from_file(relevant_portfolios)
    # access their websites for their information
    # do analysis on the portfolio's information
    
    # scrape web for news articles
    # access those news articles
    # do analysis on the news article's information
    
    # construct a report
    # send the report
    

if __name__ == '__main__':
    main()

