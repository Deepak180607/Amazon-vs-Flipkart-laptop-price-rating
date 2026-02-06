# Amazon-vs-Flipkart-laptop-price-rating
An end-to-end data pipeline that scrapes gaming laptop data, cleans and analyzes it, and generates high-quality comparison visualizations.
# Laptop Price Comparison: Amazon vs Flipkart

An end-to-end data pipeline that scrapes gaming laptop data from **Amazon** and **Flipkart**, cleans it, analyzes value-for-money, and generates **publication-ready visualizations**.

## Features
- Web scraping using Selenium & Requests
- Data cleaning and feature engineering (value score)
- Comparison analysis across platforms
- Gradient-based, presentation-ready visualizations
- Automated PNG export

## Tech Stack
- Python
- Selenium
- BeautifulSoup
- Requests
- Pandas
- Matplotlib & Seaborn

## Project Structure
project_compare/
│
├── data/
│   ├── Amazon.csv                 # Raw Amazon laptop data
│   ├── Laptop.csv                 # Combined laptop dataset
│   ├── amazon_clean.csv           # Cleaned Amazon data
│   ├── flipkart_clean.csv         # Cleaned Flipkart data
│
├── plots/
│   ├── price_comparison.png       # Price comparison visualization
│   ├── ratings_comparison.png     # Ratings comparison chart
│   └── value_score_comparison.png # Value score comparison plot
│
├── main.py                        # Entry point of the project
├── analysis.py                    # Data analysis & comparison logic
├── visualize.py                   # Visualization and plotting functions
├── scraper.py                     # Web scraping utilities
├── scrape_amazon.py               # Amazon data scraping script
│
├── .gitignore                     # Git ignored files & folders
└── README.md                      # Project documentation

