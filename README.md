# Twitter/X Trending Hashtags Analysis (2020-2025)

## Project Overview
An exploratory data analysis of trending hashtags on Twitter/X from 2020 to 2025. The dataset contains 12,036 unique trending entries spanning six years.

## Objectives
- Identify trending patterns
- Analyze the lifecycle of trending hashtags
- Correlate major world events with hashtag trends
- Discover peak engagement periods
- Extract insights for social media strategy

## Dataset
**Source:** Kaggle - Twitter/X Trending Hashtags (2020-2025)  
**Records:** 12,036 unique trend entries  
**Time Period:** 2020 - 2025  
**Data Source:** Wayback Machine snapshots of x.com trending data

### Dataset Structure
- `tag`: Trending hashtag or topic
- `year`: Year of trending
- `peak_date`: Date when hashtag peaked
- `tweets`: Number of tweets
- `rank`: Trending rank position

## Key Analyses

**Temporal Trends**
- Year-over-year trending patterns
- Monthly and seasonal variations
- Day-of-week trending behavior

**Major Events Correlation**
- 2020: COVID-19 pandemic emergence
- 2020: US Presidential Election
- 2021-2025: Cultural and political milestones
  
**Hashtag Performance Metrics**
- Tweet volume distribution
- Trending duration analysis
- Peak engagement timing
- Rank position patterns

**Content Category Analysis**
- Political vs. entertainment trends
- News vs. cultural moments
- Organic vs. campaign-driven hashtags

## Technologies
- Python 3.8+
- Pandas - Data manipulation and analysis
- NumPy - Numerical computing
- Matplotlib - Static visualizations
- Seaborn - Statistical data visualization
- Plotly - Interactive visualizations
- Jupyter Notebook - Analysis environment

## Visualizations
The project includes interactive timeline visualizations, heatmaps showing trending patterns over time, distribution plots for tweet volumes, top trending hashtags by year, word clouds for popular topics, and time series analysis of major events.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
Clone the repository:
```bash
git clone https://github.com/cyberyimi/twitter-trends-eda.git
cd twitter-trends-eda
```

Install required packages:
```bash
pip install -r requirements.txt
```

Download the dataset from Kaggle and place `twitter_trends.csv` in the `data/` folder.

Run the analysis:
```bash
jupyter notebook notebooks/twitter_trends_analysis.ipynb
```

## Key Findings
*Findings will be updated after completing the analysis*
- Trending patterns show strong correlation with major news events
- Peak engagement occurs during [specific timeframes]
- Cultural moments vs. news events have distinct trending patterns

## Project Structure

```
twitter-trends-eda/
│
├── data/
│   └── twitter_trends.csv
│
├── notebooks/
│   └── twitter_trends_analysis.ipynb
│
├── visualizations/
│   ├── timeline_trends.html
│   ├── top_hashtags.png
│   └── heatmap_trends.png
│
├── requirements.txt
└── README.md
```

## Author
**Monse Rojo**  
LinkedIn: linkedin.com/in/monse-rojo-6b70b3397  
GitHub: github.com/cyberyimi

## License

This project is open source and available under the MIT License.

## Acknowledgments

Dataset provided by Kaggle community. Built as part of a data science portfolio project.
