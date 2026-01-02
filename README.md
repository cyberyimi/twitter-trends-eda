# Twitter/X Trending Hashtags Analysis (2020-2025)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-red)

## 📊 Project Overview

A comprehensive exploratory data analysis of trending hashtags on Twitter/X from 2020 to 2025, examining 12,036 unique trending entries across six years. This project analyzes viral phenomena, cultural moments, and major world events through the lens of social media trending data.

## 🎯 Objectives

- Identify trending patterns and seasonal variations in viral content
- Analyze the lifecycle of trending hashtags
- Correlate major world events with hashtag trends
- Discover peak engagement periods and content themes
- Extract actionable insights for social media strategy

## 📁 Dataset

**Source:** Kaggle - Twitter/X Trending Hashtags (2020-2025)  
**Records:** 12,036 unique trend entries  
**Time Period:** 2020 - 2025  
**Data Source:** Wayback Machine snapshots of x.com trending data

### Dataset Structure
```
Columns:
- tag: Trending hashtag or topic
- year: Year of trending
- peak_date: Date when hashtag peaked
- tweets: Number of tweets
- rank: Trending rank position
```

## 🔍 Key Analyses

### 1. Temporal Trends Analysis
- Year-over-year trending patterns
- Monthly and seasonal variations
- Day-of-week trending behavior

### 2. Major Events Correlation
- 2020: COVID-19 pandemic emergence
- 2020: US Presidential Election
- 2021-2025: Cultural and political milestones
- Viral content lifecycle patterns

### 3. Hashtag Performance Metrics
- Tweet volume distribution
- Trending duration analysis
- Peak engagement timing
- Rank position patterns

### 4. Content Category Analysis
- Political vs. entertainment trends
- News vs. cultural moments
- Organic vs. campaign-driven hashtags

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib** - Static visualizations
- **Seaborn** - Statistical data visualization
- **Plotly** - Interactive visualizations
- **Jupyter Notebook** - Analysis environment

## 📈 Visualizations

The project includes:
- Interactive timeline visualizations
- Heatmaps showing trending patterns over time
- Distribution plots for tweet volumes
- Top trending hashtags by year
- Word clouds for popular topics
- Time series analysis of major events

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8 or higher
pip package manager
```

### Installation

1. Clone the repository
```bash
git clone https://github.com/cyberyimi/twitter-trends-eda.git
cd twitter-trends-eda
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Download the dataset
- Visit [Kaggle Dataset Link]
- Place `twitter_trends.csv` in the `data/` folder

4. Run the analysis
```bash
jupyter notebook notebooks/twitter_trends_analysis.ipynb
```

## 📊 Key Findings

*Findings will be updated after completing the analysis*

- Trending patterns show strong correlation with major news events
- Peak engagement occurs during [specific timeframes]
- Cultural moments vs. news events have distinct trending patterns
- [Additional insights from analysis]

## 📝 Project Structure

```
twitter-trends-eda/
│
├── data/
│   └── twitter_trends.csv           # Raw dataset
│
├── notebooks/
│   └── twitter_trends_analysis.ipynb # Main analysis notebook
│
├── visualizations/
│   ├── timeline_trends.html         # Interactive timeline
│   ├── top_hashtags.png            # Top hashtags visualization
│   └── heatmap_trends.png          # Temporal heatmap
│
├── requirements.txt                 # Project dependencies
└── README.md                       # Project documentation
```

## 🎓 Skills Demonstrated

- **Data Cleaning:** Handling timestamps, missing values, and data quality issues
- **Exploratory Data Analysis:** Statistical analysis and pattern recognition
- **Data Visualization:** Creating compelling and informative visualizations
- **Time Series Analysis:** Analyzing temporal patterns and trends
- **Statistical Thinking:** Drawing insights from large datasets
- **Technical Communication:** Presenting findings clearly and professionally

## 👤 Author

**Monse Rojo**
- LinkedIn: [linkedin.com/in/monse-rojo-6b70b3397](https://www.linkedin.com/in/monse-rojo-6b70b3397/)
- GitHub: [github.com/cyberyimi](https://github.com/cyberyimi)

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Dataset provided by Kaggle community
- Inspired by the evolution of social media trends 2020-2025
- Built as part of a data science portfolio project

---

*Last Updated: December 2024*
