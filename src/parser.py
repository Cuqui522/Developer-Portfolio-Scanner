from bs4 import BeautifulSoup

def parse_html(html: str) -> BeautifulSoup:
    """Parse raw HTML into a BeautifulSoup object."""
    return BeautifulSoup(html, "lxml")

def extract_text(soup: BeautifulSoup) -> str:
    """Strip noisy tags and return clean lowercased text from the page body."""
    for tag in soup(["script", "style", "nav", "footer", "head"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True).lower()