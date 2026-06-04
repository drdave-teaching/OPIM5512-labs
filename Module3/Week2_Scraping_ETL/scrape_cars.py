import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re


def scrape_listings(url, max_pages=3):
    headers = {"User-Agent": "Mozilla/5.0 (educational scraping project)"}
    records = []

    for page in range(max_pages):
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Got status {response.status_code}, stopping.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        listings = soup.find_all("li", class_=re.compile("result"))

        for listing in listings:
            title = listing.find("a", class_=re.compile("title"))
            price = listing.find("span", class_=re.compile("price"))
            records.append({
                "title": title.get_text(strip=True) if title else None,
                "price": price.get_text(strip=True) if price else None,
            })

        print(f"Page {page + 1}: scraped {len(listings)} listings")
        time.sleep(1)  # be polite — don't hammer the server

    return pd.DataFrame(records)


def clean_price(df):
    df["price_clean"] = (
        df["price"]
        .str.replace(r"[^\d]", "", regex=True)
        .pipe(pd.to_numeric, errors="coerce")
    )
    return df


def main():
    # replace with a real URL when running in class
    url = "https://example.com/cars-for-sale"
    df = scrape_listings(url)
    df = clean_price(df)
    print(df.head(10))
    df.to_csv("scraped_cars.csv", index=False)
    print(f"\nSaved {len(df)} records to scraped_cars.csv")


if __name__ == "__main__":
    main()
