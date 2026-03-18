from fetcher import fetch_page
from parser import parse_html, extract_text
from extractor import extract_skills, extract_availability

with open("../data/websites.txt") as f:
    sites = [line.strip() for line in f]

for site in sites:
    url = f"https://{site}"

    html, status = fetch_page(url)

    print(site, status)

from scraper.parser import parse_html

if html:
    soup = parse_html(html)
    print(soup.title.string)