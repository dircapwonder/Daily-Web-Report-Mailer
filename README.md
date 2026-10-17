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

2. Configure your scraper and email settings in the project files (see `config_example.json`).

3. Run the main script:

```bash
python main.py --config config_example.json
```

## How to use

1. Prepare configuration

- Copy `config_example.json` to `config.json` and edit the `targets` and `email` sections with your URLs, selectors, SMTP host, and recipients.
- Or set environment variables for sensitive values (recommended):
  - EMAIL_USERNAME
  - EMAIL_PASSWORD (or use a named env key referenced by the config file)

Example `config.json` snippet:

```json
{
  "targets": [
    {
      "name": "Example Headlines",
      "url": "https://example.com/news",
      "selector": ".article h2",
      "type": "css"
    }
  ],
  "email": {
    "smtp_host": "smtp.example.com",
    "smtp_port": 587,
    "use_tls": true,
    "username": "you@example.com",
    "password_env": "EMAIL_PASSWORD",
    "from": "you@example.com",
    "to": ["recipient@example.com"],
    "subject": "Daily Scrape Report"
  }
}
```

2. Test locally (dry run)

- Run the script and print results without sending email (if supported):

```bash
python main.py --config config.json --dry-run
```

If a `--dry-run` flag is not implemented, run with a test SMTP server or use a temporary recipient address to verify the email formatting.

3. Send a real email

```bash
python main.py --config config.json
```

4. Scheduling

- Cron (Linux / macOS):

```
0 9 * * * /usr/bin/python3 /path/to/main.py --config /path/to/config.json
```

- Windows Task Scheduler: create a basic task that runs Python with the main script and config path.

- Built-in scheduler: if you include the `schedule` library and the project supports a `--schedule "daily 09:00"` argument, you can run the script long-running to send at the configured times.

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

## Why I Keep This Repo

I keep this repository because it is a compact, practical project that helps me practice and demonstrate a few recurring skills:

- Hands-on experience with web requests and HTML parsing (requests + BeautifulSoup)
- Building reliable automation workflows (scheduling, retries, throttling)
- Working with email delivery via SMTP and understanding email formatting/attachments
- A convenient template for small monitoring and reporting tools I can reuse or adapt
- Fast to iterate on and a good place to try out enhancements like headless browsers or mail APIs

It’s also a useful showcase project for quick demos in interviews or when explaining how to wire together a simple automation pipeline.

## Technologies Used

- Python
- requests
- BeautifulSoup
- SMTP email sending

## License

This project is for educational and personal use.

## Short Description

Automated web scraping and email delivery tool built with Python.
