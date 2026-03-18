import requests

def fetch_page(url):
    try:
        response = requests.get(url, timeout=5)
        return response.text, response.status_code
    except:
        return None, "failed"