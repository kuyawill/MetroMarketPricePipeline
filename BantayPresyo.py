
import os
import pandas as pd

from BP_Extraction import extract
from BP_Transform import transform
from shared_func import today_links


def load_previous_data():
    if os.path.exists('daily.txt'):
        with open('daily.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]
    return []

def compare_data(new_links, old_links):
    new_set = set(new_links)
    old_set = set(old_links)

    added = new_set - old_set
    removed = old_set - new_set
    
    pdf_link = []
    
    if added:
        print("New links added:")
        for link in added:
            print(link)
            pdf_link.append(link)
                
    if removed:
        print("Links removed:")
        for link in removed:
            print(link)

    return pdf_link

if __name__ == "__main__":    
    yesterday_links = load_previous_data()
    addedlink = compare_data(today_links, yesterday_links)
    #testlink = ["https://www.da.gov.ph/wp-content/uploads/2024/09/Price-Monitoring-September-10-2024.pdf"]
    if not addedlink:
        print("No additional update today.")
    else:
        transform(extract(addedlink))
   
