# BantayPresyo

BantayPresyo is a Python-based tool that automates the extraction, transformation, and loading of price monitoring data from the Philippine Department of Agriculture's website.

## Overview

The tool performs the following functions:
1. Scrapes the DA website[https://www.da.gov.ph/price-monitoring/] for new price monitoring PDF links
2. Downloads and extracts tables from these PDFs
3. Transforms the data into a structured format
4. Loads the processed data into a MySQL database

## Requirements

- Python 3.x
- MySQL Database
- Required Python packages:
  - pandas
  - pdfplumber
  - requests
  - BeautifulSoup4
  - SQLAlchemy
  - mysqlclient

## Project Structure

- `BantayPresyo.py` - Main script that orchestrates the ETL process
- `BP_Extraction.py` - Handles PDF downloading and data extraction
- `BP_Transform.py` - Processes and cleans the extracted data
- `BP_Load.py` - Loads the transformed data into the MySQL database
- `Shared_func.py` - Contains shared utilities used across the project

## Setup

1. Ensure all required packages are installed:
```bash
pip install pandas pdfplumber requests beautifulsoup4 sqlalchemy mysqlclient
```

2. Configure the database connection in `BP_Load.py`:
```python
username = 'your_username'
password = 'your_password'
host = 'localhost'
port = '3306'
database = 'sql_bantaypresyodb'
```

## How It Works

1. The script checks for new PDF links on the DA website
2. Compares new links against previously processed links
3. Downloads and processes only new PDFs
4. Extracts price data from tables in the PDFs
5. Cleans and transforms the data, including:
   - Standardizing column names
   - Processing price ranges into averages
   - Mapping markets to cities
6. Loads the processed data into the MySQL database

## Data Processing

The tool processes various commodity prices, including:
- Rice
- Corn
- Fish (Tilapia, Galunggong)
- Vegetables (Ampalaya, Tomato, Cabbage)
- Meat (Pork, Chicken)
- Eggs

## File Management

- Previously processed links are stored in `daily.txt`
- Downloaded PDFs are saved in a `pdf_files` folder

## Error Handling

The tool includes error handling for:
- Failed PDF downloads
- Data processing errors
- Database connection issues

## Limitations

- Relies on consistent PDF formatting from the DA website
- Requires stable internet connection for web scraping and PDF downloads
- May need adjustments if the DA website structure changes

## Usage

Run the main script:
```bash
python BantayPresyo.py
```

## Notes

- The tool is designed to run daily to capture new price monitoring updates
- It only processes new PDFs, avoiding redundant processing
- Make sure the MySQL database is properly set up before running the tool
