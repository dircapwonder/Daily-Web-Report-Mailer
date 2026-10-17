# Web Scrape and Send Via Mail

A Python project that scrapes data from websites and automatically sends the results via email using SMTP. It is useful for recurring reports, price checks, monitoring updates, and other alert-style workflows.

## Features

- Scrape content from websites using requests and BeautifulSoup
- Extract data with configurable selectors or parsing logic
- Format results as plain text or HTML
- Send emails through SMTP with support for attachments
- Easily adapt the project for reports, alerts, or scheduled updates
- Simple structure that can be expanded into a more advanced automation tool

## Requirements

Make sure you have Python 3 installed.

Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

Optional packages for more advanced functionality:

```bash
pip install lxml python-dotenv schedule
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/dircapwonder/Web-Scrape-and-Send-Via-Mail.git
cd Web-Scrape-and-Send-Via-Mail
```

2. Configure your scraper and email settings in the project files.

3. Run the main script:

```bash
python main.py
```

## Project Structure

```text
Web-Scrape-and-Send-Via-Mail/
├── main.py
├── scraper.py
├── mailer.py
├── config_example.json
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

1. A script loads the target website URL.
2. It fetches and parses the HTML content.
3. It extracts the fields you want, such as headlines, prices, or text blocks.
4. The data is formatted into an email body.
5. The message is sent using SMTP to a recipient email address.

## Example Use Cases

- Daily stock or crypto price report
- Product price monitoring from an online store
- News headline summaries sent by email
- Website monitoring and alerts

## Security Notes

- Do not hardcode passwords or API keys in the repository.
- Store sensitive values in environment variables or a local config file that is not committed.
- Follow the terms of service and legal requirements for the sites you scrape.

## Technologies Used

- Python
- requests
- BeautifulSoup
- SMTP email sending
