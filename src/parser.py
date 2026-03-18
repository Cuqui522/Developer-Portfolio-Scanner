from bs4 import BeautifulSoup

def parse_html(html):
    return BeautifulSoup(html, "lxml")

def extract_text(soup):
    return soup.get_text().lower()