#  Gaming Analytics Pipeline

## What This Project Does
A data engineering pipeline that analyses
16,000+ video game sales records to find:
- Top 10 best selling games of all time
- Most popular gaming genres
- Best performing platforms
- Top game publishers
- Gaming sales trends over years

## Tools Used
- Python 3
- Pandas (data cleaning & analysis)
- Matplotlib (charts & visualizations)
- Jupyter Notebook

## Dataset
Video Game Sales dataset from Kaggle
16,598 games across all platforms

## How to Run
1. Install requirements:
pip install pandas matplotlib jupyter

2. Open Jupyter:
jupyter notebook

3. Open gaming_pipeline.ipynb
4. Run all cells!

## Key Findings
- Most popular genre: Action
- Peak gaming year: 2008-2009
- Top publisher: Nintendo

## Project Structure
gaming-analytics-pipeline/
├── gaming_pipeline.ipynb  → main notebook
├── vgsales.csv            → raw data
├── clean_vgsales.csv      → clean data
├── top10_games.png        → chart
├── genre_sales.png        → chart
├── platform_sales.png     → chart
└── sales_trend.png        → chart
