"""
Simple agentic ETL: given a block of unstructured text, use Claude to extract
structured records and save them as a CSV.

Requires: pip install anthropic python-dotenv
Set ANTHROPIC_API_KEY in a .env file (never commit that file).
"""

import os
import json
import csv
import anthropic
from dotenv import load_dotenv

load_dotenv()

SAMPLE_TEXT = """
Storm Event 1: On March 4th, a tornado touched down near Tulsa, OK causing
significant damage to residential areas. Wind speeds reached 120 mph.
Estimated damage: $2.3 million. No fatalities reported.

Storm Event 2: Flash flooding in Austin, TX on March 8th inundated roads
and forced dozens of evacuations. Rainfall totaled 6 inches in 3 hours.
One fatality reported.

Storm Event 3: A severe hailstorm hit Denver, CO on March 12th. Hail up to
2 inches in diameter damaged vehicles and rooftops. Estimated damage: $800,000.
"""

EXTRACT_PROMPT = """
Extract storm event records from the text below. Return a JSON array where each
object has these fields: date, location, event_type, max_intensity, damage_usd, fatalities.

Use null for any missing values. Return ONLY valid JSON, no explanation.

Text:
{text}
"""


def extract_events(text: str) -> list[dict]:
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": EXTRACT_PROMPT.format(text=text)}],
    )
    raw = message.content[0].text.strip()
    return json.loads(raw)


def save_to_csv(records: list[dict], path: str):
    if not records:
        print("No records to save.")
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)
    print(f"Saved {len(records)} records to {path}")


def main():
    print("Extracting structured records from unstructured text...\n")
    records = extract_events(SAMPLE_TEXT)
    for r in records:
        print(r)
    save_to_csv(records, "storm_events_extracted.csv")


if __name__ == "__main__":
    main()
