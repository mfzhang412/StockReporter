from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

class Website(object):
    """
    Represents an HTML/XML website.
    """

    version = '0.1'
    

    def __init__(self, url):
        """
        Construct a new 'Website' object.

        :param url: The website URL
        """
        self.url = url

    def get_raw_html(self):
        """
        Retrieve the raw HTML/XML from the URL.

        :return: The raw HTML/XML from the URL if successful, None otherwise
        """
        try:
            with closing(get(self.url, stream=True)) as resp:
                if (self.good_response(resp)):
                    return resp.content
                else:
                    return None
        except RequestException as error:
            raise

    def good_response(self, resp):
        """
        Return True if response is in HTML/XML, False otherwise

        :param resp: The website response
        :return: True if response is in HTML, false otherwise
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)

    def get_html(self):
        """
        Retrieve the formatted HTML/XML from the URL.

        :return: The formatted HTML/XML from the URL if successful, None otherwise
        """
        raw_html = self.get_raw_html()
        if (raw_html == None):
            return None
        html = BeautifulSoup(raw_html, 'html.parser')
        return html
        
        

def testing():
    site = Website("https://www.pythonforbeginners.com/lists/list-comprehensions-in-python/")
    print(site.url)
    raw_html = site.get_raw_html(); # do nothing with this
    html = site.get_html()
    print(html)



testing()





