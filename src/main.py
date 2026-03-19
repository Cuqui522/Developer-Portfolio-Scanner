from fetcher import fetch_page
from parser import parse_html, extract_text
from extractor import extract_skills, extract_availability

with open("../data/websites.txt") as f:
    sites = [line.strip() for line in f]

paths = ["", "/about", "/about-me", "/bio", "/profile"]

for site in sites:
    print(f"\nChecking: {site}")

    for path in paths:
        url = f"https://{site}{path}"

        html, status = fetch_page(url)
        print(f"  Trying {path or '/'} → {status}")

        if html:
            soup = parse_html(html)
            text = extract_text(soup)

            print("  Preview:", text[:200])

            skills = extract_skills(text)
            availability = extract_availability(text)

            if skills or availability:
                print("  ✅ FOUND DATA!")
                print("  Skills:", skills)
                print("  Available:", availability)
                break