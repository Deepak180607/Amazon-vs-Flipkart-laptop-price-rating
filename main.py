import scraper as sc
import Scrape_amazon as sa
import analysis as an
import Amxon_analysis as aan
import visualize as vs

def main():
    # Scraping
    print("Starting data collection...")
    flip_df = sc.scrape_data()
    amz_df = sa.Scrape_data()

    # Cleaning & Scoring
    print("Analyzing data...")
    flip_df = an.clean_data(flip_df)
    amz_df = aan.clean_data(amz_df)

    # Visualization
    print("Generating comparison graphs...")
    vs.make_plots(amz_df, flip_df)

    print("Process Complete. PNG files are ready.")

if __name__ == "__main__":
    main()