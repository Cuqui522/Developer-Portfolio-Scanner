import requests

with open("../data/websites.txt") as f:
    sites = [line.strip() for line in f]

for site in sites:
    url = f"https://{site}"

    try:
        response = requests.get(url, timeout=5)
        print(site, response.status_code)
    except:
        print(site, "failed")