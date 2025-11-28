from flask import Flask, render_template, request
from news_client import fetch_top_headlines
import os

app = Flask(__name__)

# Default values
DEFAULT_COUNTRY = os.getenv("COUNTRY", "us")
DEFAULT_PAGE_SIZE = 20

# Supported countries (NewsData.io supports many)
COUNTRIES = {
    "us": "United States",
    "gb": "United Kingdom",
    "ca": "Canada",
    "in": "India",
    "au": "Australia",
    "de": "Germany",
    "fr": "France",
    "jp": "Japan",
    "ru": "Russia",
    "cn": "China"
}

PAGE_SIZES = [5, 10, 15, 20, 25, 30]

@app.route("/")
def home():
    country = request.args.get("country", DEFAULT_COUNTRY)
    page_size = int(request.args.get("page_size", DEFAULT_PAGE_SIZE))

    articles = fetch_top_headlines(country=country, page_size=page_size)

    return render_template(
        "home.html",
        articles=articles,
        selected_country=country,
        selected_page_size=page_size,
        countries=COUNTRIES,
        page_sizes=PAGE_SIZES
    )

if __name__ == "__main__":
    app.run(debug=True)
