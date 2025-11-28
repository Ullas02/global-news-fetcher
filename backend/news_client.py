import os
import requests
from typing import List, Dict, Any
from dotenv import load_dotenv
from cache import cache

# Load environment variables
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # NewsData.io API key
COUNTRY = os.getenv("COUNTRY", "us")
CACHE_TTL = int(os.getenv("CACHE_TTL_SECONDS", "300"))

NEWS_URL = "https://newsdata.io/api/1/latest"

def fetch_top_headlines(country: str = None, page_size: int = 20) -> List[Dict[str, Any]]:
    """
    Fetch top headlines from NewsData.io for a given country and number of articles.
    Uses in-memory caching to reduce repeated API calls.
    """
    if country is None:
        country = COUNTRY

    cache_key = f"top_headlines_{country}_{page_size}"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    params = {
        "apikey": NEWS_API_KEY,
        "country": country,
        "language": "en"
    }

    try:
        resp = requests.get(NEWS_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        articles = data.get("results") or []
    except requests.exceptions.RequestException as e:
        print("Error fetching news:", e)
        articles = []

    # Clean fields for template
    cleaned = []
    count = 0
    for a in articles:
        if count >= page_size:
            break
        cleaned.append({
            "title": a.get("title"),
            "description": a.get("description"),
            "source": a.get("source_id"),
            "url": a.get("link"),
            "urlToImage": a.get("image_url"),
            "publishedAt": a.get("pubDate")
        })
        count += 1

    cache.set(cache_key, cleaned, ttl=CACHE_TTL)
    return cleaned
