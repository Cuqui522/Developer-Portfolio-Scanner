import csv
import os
from fetcher import fetch_page
from parser import parse_html, extract_text
from extractor import extract_skills, extract_availability

PATHS = ["", "/about", "/about-me", "/bio", "/profile", "/projects", "/portfolio", "/work"]
OUTPUT_FILE = "../output/results.csv"

def clean_url(site: str) -> str:
    """Normalize URL by stripping protocol prefix so we control it consistently."""
    site = site.strip()
    for prefix in ("https://", "http://"):
        if site.startswith(prefix):
            site = site[len(prefix):]
    return site

def score_result(skills: dict[str, int], availability: bool) -> int:
    """Calculate total score: sum of skill mention counts plus availability bonus."""
    skill_score = sum(skills.values())
    availability_bonus = 10 if availability else 0
    return skill_score + availability_bonus

def scrape_site(site: str) -> dict | None:
    """Crawl a site across all defined paths and return the highest-scoring page result."""
    best_result = None
    best_score = 0

    for path in PATHS:
        url = f"https://{site}{path}"
        html, status = fetch_page(url)
        print(f"  {path or '/'} → {status}", end="")

        if not html or str(status).startswith(("4", "5")):
            print()
            continue

        soup = parse_html(html)
        text = extract_text(soup)
        skills = extract_skills(text)
        availability = extract_availability(text)
        score = score_result(skills, availability)

        print(f" | score={score} | skills={len(skills)} | available={availability}")

        if score > best_score:
            best_score = score
            best_result = {
                "site": site,
                "url": url,
                "available": availability,
                "skills": ", ".join(skills.keys()),
                "skill_detail": str(skills),
                "score": score,
            }

        if score >= 20:
            break

    return best_result

def main() -> None:
    """Read input domains, scrape each site, and write results to CSV."""
    with open("../data/websites.txt") as f:
        sites = [clean_url(line) for line in f if line.strip()]

    results = []
    for site in sites:
        print(f"\n🔍 Scraping: {site}")
        result = scrape_site(site)
        if result:
            results.append(result)
            print(f"  ✅ Best page: {result['url']} (score={result['score']})")
        else:
            print(f"  ❌ No data found")
            results.append({"site": site, "url": "", "available": False,
                            "skills": "", "skill_detail": "", "score": 0})

    os.makedirs("../output", exist_ok=True)
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["site", "url", "available", "skills", "skill_detail", "score"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\n📄 Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()