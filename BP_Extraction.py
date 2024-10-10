import requests
import pdfplumber
import re
from datetime import datetime
import os

def extract(pdf_link_url):
    extracted_tables = []
    pdf_folder = "pdf_files"
    #downloading the pdf and extracting the table
    for i, pdfurl in enumerate(pdf_link_url):
        try:
            date = extract_date_from_link(pdfurl)
            response = requests.get(pdfurl, timeout=20)
            if response.status_code == 200:
                pdf_filename = os.path.join(pdf_folder, f"pdf_gov{i+1}.pdf")
                #downloading the pdf
                with open(pdf_filename,"wb") as pdf_file:
                    pdf_file.write(response.content)

                #opening pdf and table extraction
                with pdfplumber.open(pdf_filename) as openpdf:
                    # greater than 1 is the second page where the table is located
                    if len(openpdf.pages) > 1:
                        page = openpdf.pages[1]
                        table = page.extract_table()
                        if table:
                            table_with_date = []

                            if table[0]:
                                table_with_date.append(table[1] + ["Date"])

                            for row in table[2:]:
                                table_with_date.append(row + [date])

                            extracted_tables.append(table_with_date)
                                                                            
            else:
                print(f"Failed to download {pdfurl}. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while downloading {pdfurl}: {e}")
    return extracted_tables

def extract_date_from_link(url):
    date_pattern = r'([A-Za-z]+)-(\d{1,2})-(\d{4})'
    match = re.search(date_pattern, url)

    if match:
        month = match.group(1)
        day = int(match.group(2))
        year = int(match.group(3))
        date = datetime.strptime(f'{month} {day} {year}', '%B %d %Y')
        return date.strftime('%Y-%m-%d')

if __name__ == "__main__":
    print()
    #testlink = ["https://www.da.gov.ph/wp-content/uploads/2024/09/Price-Monitoring-September-6-2024.pdf"]
    #print(extract(testlink))