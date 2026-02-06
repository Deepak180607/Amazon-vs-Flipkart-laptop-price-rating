import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def make_plots(amazon_df, flipkart_df):
    # Set professional theme
    sns.set_theme(style="whitegrid")
    
    # Standardize column names (Flipkart 'Price' vs Amazon 'Prices')
    flip_comp = flipkart_df.copy().rename(columns={'Price': 'Prices'})
    amz_comp = amazon_df.copy()
    
    # Label platforms and combine
    amz_comp['Platform'] = 'Amazon'
    flip_comp['Platform'] = 'Flipkart'
    combined = pd.concat([amz_comp, flip_comp], ignore_index=True)

    # 1. VALUE SCORE COMPARISON (Inspiration: Red Palette)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=combined, x='Platform', y='value_score', palette='Reds_d', errorbar='sd')
    plt.title('Value Score Comparison: Amazon vs Flipkart', fontsize=14, fontweight='bold')
    plt.ylabel('Value Score (Rating / Price)')
    plt.tight_layout()
    plt.savefig('data/value_score_comparison.png')
    plt.close()

    # 2. RATINGS COMPARISON (Inspiration: Purple/Magma Palette)
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=combined, x='Platform', y='Ratings', palette='magma')
    plt.title('User Ratings Distribution: Amazon vs Flipkart', fontsize=14, fontweight='bold')
    plt.ylabel('Ratings (Out of 5)')
    plt.tight_layout()
    plt.savefig('data/ratings_comparison.png')
    plt.close()

    # 3. PRICE COMPARISON (Inspiration: Blue Palette)
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=combined, x='Prices', hue='Platform', fill=True, palette='Blues_d')
    plt.title('Price Distribution Comparison', fontsize=14, fontweight='bold')
    plt.xlabel('Price (₹)')
    plt.tight_layout()
    plt.savefig('data/price_comparison.png')
    plt.close()

    print("Comparison PNGs (Value, Ratings, Price) saved successfully.")