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


def get_companies_from_file(file):
    contents = file.read_all().strip()
    company_info = contents.split('\n')
    Company = namedtuple('Company', 'name stock_symbol')
    companies = []
    for info in company_info:
        company_fields = info.split(', ')
        company = Company(*company_fields)
        companies.append(company)
    return companies


def get_industries_from_file(file):
    contents = file.read_all().strip()
    industries_info = contents.split('\n')
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
    Portfolio = namedtuple('Portfolio', 'name website')
    portfolios = []
    for info in portfolio_info:
        portfolio_fields = info.split(', ')
        portfolio = Portfolio(*portfolio_fields)
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
    
    # scrape web for relevant key words
    # access those articles
    # do analysis on the articles (or just link to them in the email)
    
    # construct a report
    # send the report
    

if __name__ == '__main__':
    main()

