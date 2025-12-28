"""
Twitter/X Trending Hashtags Analysis (2020-2025)
Author: Monse Rojo
Description: Comprehensive EDA of 12,000+ trending hashtags
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
import os

# Configuration
warnings.filterwarnings('ignore')
plt.style.use('dark_background')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 11

# Define neon cyan color for this project
NEON_CYAN = '#00ffff'

# Create visualizations directory if it doesn't exist
os.makedirs('visualizations', exist_ok=True)

print("="*60)
print("TWITTER TRENDING HASHTAGS ANALYSIS (2020-2025)")
print("="*60)
print("\nLoading dataset...")

# Load data
df = pd.read_csv('data/twitter-trending-hashtags.csv')
print(f"✅ Dataset loaded: {len(df):,} rows")

# Data preprocessing
print("\n" + "="*60)
print("DATA PREPROCESSING")
print("="*60)

df['peak_date'] = pd.to_datetime(df['peak_date'])
df['month'] = df['peak_date'].dt.month
df['month_name'] = df['peak_date'].dt.month_name()
df['day_of_week'] = df['peak_date'].dt.day_name()
df['quarter'] = df['peak_date'].dt.quarter

print(f"Date range: {df['peak_date'].min()} to {df['peak_date'].max()}")
print(f"Years covered: {sorted(df['year'].unique())}")
print("✅ Date features created")

# Basic statistics
print("\n" + "="*60)
print("BASIC STATISTICS")
print("="*60)
print(f"Total hashtags: {len(df):,}")
print(f"Average tweets: {df['tweets'].mean():,.0f}")
print(f"Median tweets: {df['tweets'].median():,.0f}")
print(f"Max tweets: {df['tweets'].max():,.0f}")

# VISUALIZATION 1: Trends by Year
print("\n📊 Creating visualization 1: Trends by Year...")
yearly_counts = df['year'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(yearly_counts.index, yearly_counts.values, 
              color=NEON_CYAN, edgecolor='white', linewidth=2)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}',
            ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Trending Hashtags', fontsize=14, fontweight='bold')
ax.set_title('Trending Hashtags by Year (2020-2025)', 
             fontsize=16, fontweight='bold', pad=20)
ax.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('visualizations/trends_by_year.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: trends_by_year.png")

# VISUALIZATION 2: Monthly Patterns
print("📊 Creating visualization 2: Monthly Patterns...")
monthly_counts = df.groupby('month_name').size().reindex([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

fig, ax = plt.subplots(figsize=(14, 6))
bars = ax.bar(range(12), monthly_counts.values, 
              color=NEON_CYAN, edgecolor='white', linewidth=2)

top_3_indices = monthly_counts.nlargest(3).index
for i, month in enumerate(monthly_counts.index):
    if month in top_3_indices:
        bars[i].set_color('#ff00ff')

ax.set_xticks(range(12))
ax.set_xticklabels(monthly_counts.index, rotation=45, ha='right')
ax.set_xlabel('Month', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Trending Hashtags', fontsize=14, fontweight='bold')
ax.set_title('Trending Patterns by Month', fontsize=16, fontweight='bold', pad=20)
ax.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('visualizations/trends_by_month.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: trends_by_month.png")

# VISUALIZATION 3: Day of Week
print("📊 Creating visualization 3: Day of Week Analysis...")
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dow_counts = df.groupby('day_of_week').size().reindex(day_order)

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(range(7), dow_counts.values, 
              color='#00ffff', edgecolor='white', linewidth=2)

bars[5].set_color('#ff6600')  # Saturday
bars[6].set_color('#ff6600')  # Sunday

ax.set_xticks(range(7))
ax.set_xticklabels(day_order, rotation=45, ha='right')
ax.set_xlabel('Day of Week', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Trending Hashtags', fontsize=14, fontweight='bold')
ax.set_title('Trending Activity by Day of Week', fontsize=16, fontweight='bold', pad=20)
ax.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('visualizations/trends_by_day.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: trends_by_day.png")

# VISUALIZATION 4: Top 20 Hashtags
print("📊 Creating visualization 4: Top 20 Hashtags...")
top_20 = df.nlargest(20, 'tweets')

fig, ax = plt.subplots(figsize=(12, 10))
bars = ax.barh(range(20), top_20['tweets'].values, color='#00ffff', edgecolor='white', linewidth=2)

colors = {'2020': '#00ffff', '2021': '#00ffff', '2022': '#00ffff', 
          '2023': '#00ffff', '2024': '#00ffff', '2025': '#00ffff'}
for i, (idx, row) in enumerate(top_20.iterrows()):
    bars[i].set_color(colors.get(str(row['year']), '#00ffff'))

ax.set_yticks(range(20))
ax.set_yticklabels(top_20['tag'].values)
ax.invert_yaxis()
ax.set_xlabel('Number of Tweets', fontsize=14, fontweight='bold')
ax.set_title('Top 20 Trending Hashtags (2020-2025)', fontsize=16, fontweight='bold', pad=20)
ax.grid(axis='x', alpha=0.3, linestyle='--')

for i, v in enumerate(top_20['tweets'].values):
    ax.text(v, i, f' {v:,.0f}', va='center', fontsize=10)

plt.tight_layout()
plt.savefig('visualizations/top_20_hashtags.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: top_20_hashtags.png")

# VISUALIZATION 5: Tweet Volume Distribution
print("📊 Creating visualization 5: Tweet Volume Distribution...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

ax1.hist(df['tweets'], bins=50, color='#00ffff', edgecolor='white', alpha=0.7)
ax1.axvline(df['tweets'].mean(), color='#ff00ff', linestyle='--', 
            linewidth=2, label=f'Mean: {df["tweets"].mean():,.0f}')
ax1.axvline(df['tweets'].median(), color='#00ffff', linestyle='--', 
            linewidth=2, label=f'Median: {df["tweets"].median():,.0f}')
ax1.set_xlabel('Number of Tweets', fontsize=12, fontweight='bold')
ax1.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax1.set_title('Distribution of Tweet Volumes', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(alpha=0.3)

df.boxplot(column='tweets', by='year', ax=ax2, patch_artist=True)
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Number of Tweets', fontsize=12, fontweight='bold')
ax2.set_title('Tweet Volume Distribution by Year', fontsize=14, fontweight='bold')
plt.suptitle('')

plt.tight_layout()
plt.savefig('visualizations/tweet_volume_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: tweet_volume_distribution.png")

# VISUALIZATION 6: Heatmap
print("📊 Creating visualization 6: Trends Heatmap...")
heatmap_data = df.groupby(['year', 'month']).size().unstack(fill_value=0)

fig, ax = plt.subplots(figsize=(14, 6))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', 
            linewidths=0.5, ax=ax, cbar_kws={'label': 'Number of Trends'})
ax.set_xlabel('Month', fontsize=12, fontweight='bold')
ax.set_ylabel('Year', fontsize=12, fontweight='bold')
ax.set_title('Trending Activity Heatmap (Year vs Month)', 
             fontsize=14, fontweight='bold', pad=20)

month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticklabels(month_labels)

plt.tight_layout()
plt.savefig('visualizations/trends_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: trends_heatmap.png")

# VISUALIZATION 7: Top Trends by Year
print("📊 Creating visualization 7: Top Trends by Year...")
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
axes = axes.flatten()

years = sorted(df['year'].unique())
for i, year in enumerate(years):
    year_data = df[df['year'] == year].nlargest(10, 'tweets')
    
    axes[i].barh(range(10), year_data['tweets'].values, 
                 color='#00ffff', edgecolor='white', linewidth=1.5)
    axes[i].set_yticks(range(10))
    axes[i].set_yticklabels(year_data['tag'].values, fontsize=9)
    axes[i].invert_yaxis()
    axes[i].set_title(f'Top 10 Trends in {year}', fontsize=12, fontweight='bold')
    axes[i].grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('visualizations/top_trends_by_year.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: top_trends_by_year.png")

# Print summary
print("\n" + "="*60)
print("ANALYSIS COMPLETE!")
print("="*60)
print(f"\n📁 All visualizations saved to: visualizations/")
print(f"📊 Total visualizations created: 7")
print("\nTop 10 Most Tweeted Hashtags:")
print("="*60)
top_10_summary = df.nlargest(10, 'tweets')[['tag', 'tweets', 'year']]
for idx, row in top_10_summary.iterrows():
    print(f"{row['tag']:20} | {row['tweets']:>12,} tweets | {row['year']}")

print("\n" + "="*60)
print("Project by: Monse Rojo")
print("GitHub: github.com/cyberyimi")
print("="*60)
