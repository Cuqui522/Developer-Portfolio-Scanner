import requests

def fetch_page(url):
    try:
        response = requests.get(
            url,
            timeout=5,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        return response.text, response.status_code
    except:
        return None, "failed"