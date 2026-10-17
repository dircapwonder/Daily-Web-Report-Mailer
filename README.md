# Web Stock Scraper \& Email Reporter

A small Python project that scrapes key quote data for a list of stocks from Yahoo Finance, saves it to a dated CSV file, and emails the report as an attachment.

## Features

* Scrapes quote data from Yahoo Finance using `requests` and `BeautifulSoup`
* Collects, for each stock: current price, previous close, open, bid, ask, day's range, 52-week range, volume, and average volume
* Saves results to a CSV file named after the current date (e.g. `2026-10-15.csv`)
* Emails the CSV as an attachment through Gmail SMTP
* Waits 5 seconds between requests to avoid hammering the server

## Project Structure

```
.
├── scraper.py       
├── mailsender.py    
└── 2026-10-15.csv   
```

## Requirements

* Python 3.8+
* Libraries: `requests`, `beautifulsoup4`, `lxml`

Install the dependencies:

```bash
pip install requests beautifulsoup4 lxml
```

## Setup

### 1\. Add your User-Agent

In `scraper.py`, replace the placeholder with your browser's user agent string (search Google for "my user agent"):

```python
headers = {'User-Agent': 'YOUR USER AGENT INFO HERE'}
```

### 2\. Choose your stocks

Edit the `urls` list in `scraper.py` to track the stocks you want:

```python
urls = \["https://finance.yahoo.com/quote/AAPL/",
        "https://finance.yahoo.com/quote/BAC/",
        "https://finance.yahoo.com/quote/TTWO/"]
```

### 3\. Configure email

In `mailsender.py`, fill in your details:

```python
from\_add = "YOUR EMAIL ADRESS"
to\_add = "TARGET EMAIL ADRESS"
server.login(from\_add, "YOUR EMAIL APP PASSWORD")
```

This project uses Gmail's SMTP server (`smtp.gmail.com:587`). Gmail requires an **App Password** instead of your normal account password:

1. Enable 2-Step Verification on your Google account.
2. Create an App Password in your Google account security settings.
3. Use that App Password in `mailsender.py`.


## Usage

```bash
python scraper.py
```

The script will:

1. Fetch each stock page and extract the data
2. Write everything to `YYYY-MM-DD.csv`
3. Email the CSV file to the configured recipient

## Example Output

|Stock Name|Current Price|Previous Close|Open|Bid|Ask|Day's Range|52 Week Range|Volume|Avg. Volume|
|-|-|-|-|-|-|-|-|-|-|
|Apple Inc. (AAPL)|342.96|341.27|344.61|342.96 x 700|346.70 x 500|341.72 - 347.07|243.42 - 348.15|49,893,047|45,038,190|
|Bank of America Corporation (BAC)|51.39|53.96|49.83|51.35 x 170000|51.32 x 310000|49.26 - 51.51|46.12 - 65.23|117,950,601|33,835,162|

## How It Works

* `scraper.py` requests each Yahoo Finance quote page and parses the HTML with BeautifulSoup. The stock title and price come from the page header, and the remaining eight values come from the quote summary list.
* `mailsender.py` builds a multipart email, attaches the CSV, and sends it through Gmail's SMTP server using TLS.

## Limitations

* **Fragile selectors:** The scraper relies on Yahoo Finance's current CSS class names (e.g. `yf-ltlfr9`). If Yahoo changes its page layout, the scraper will break and the selectors will need updating.
* **Terms of service:** Scraping may be restricted by Yahoo's terms of service. This project is intended for educational and personal use only.
* **Raw values:** Values are saved as scraped text (including extra whitespace and thousands separators), without further cleaning.

## Possible Improvements

* Strip whitespace and convert numeric values before saving
* Add error handling for failed requests or missing elements
* Read stock tickers from a config file or command-line arguments
* Store credentials in environment variables
* Schedule daily runs with `cron` or Windows Task Scheduler
* Switch to an official data source or API for more reliable data

## Disclaimer

This project is for educational purposes only. The data it collects is not financial advice.

