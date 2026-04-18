import requests

def fetch_page(url: str) -> tuple[str | None, int | str]:
    """Fetch raw HTML and HTTP status from a URL, handling all network errors explicitly."""
    if url.startswith("http://") or url.startswith("https://"):
        full_url = url
    else:
        full_url = f"https://{url}"

    try:
        response = requests.get(
            full_url,
            timeout=8,
            headers={"User-Agent": "Mozilla/5.0 (compatible; PortfolioScraper/1.0)"},
            allow_redirects=True
        )
        return response.text, response.status_code
    except requests.exceptions.SSLError:
        return None, "SSL_ERROR"
    except requests.exceptions.ConnectionError:
        return None, "CONNECTION_ERROR"
    except requests.exceptions.Timeout:
        return None, "TIMEOUT"
    except requests.exceptions.RequestException as e:
        return None, f"ERROR: {e}"