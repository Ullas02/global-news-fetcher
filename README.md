# WebScrapper

## Live Demo
View my live project: [Project Link](https://global-news-fetcher.onrender.com)

## Overview
WebScrapper is a Python-based project designed to fetch and display global news. It includes a backend that handles news fetching and caching, and a simple HTML template for displaying the news.

## Project Structure
- `backend/`
  - `app.py`: Main application file to run the backend server.
  - `cache.py`: Handles caching of news data.
  - `news_client.py`: Fetches news from external sources.
  - `requirements.txt`: Lists the Python dependencies for the project.
  - `templates/home.html`: HTML template for the homepage.

## Requirements
- Python 3.8 or higher
- pip (Python package installer)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the `backend` directory:
   ```bash
   cd WebScrapper/global-news-fetcher/backend
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://127.0.0.1:5000` to view the homepage.

## Features
- Fetches global news from external APIs.
- Caches news data to improve performance.
- Simple and clean HTML interface.
