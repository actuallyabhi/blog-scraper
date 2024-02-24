import csv
import os

def save_to_csv(data, csv_file_name='scraped_data.csv'):
    # Check if the CSV file already exists
    file_exists = os.path.isfile(csv_file_name)
   
    if file_exists:
        # Open the CSV file in append mode
        with open(csv_file_name, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the data to the CSV file
            writer.writerows(data)
    else:
        # Open the CSV file in write mode
        with open(csv_file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the header to the CSV file
            writer.writerow(['Title', 'Data', 'URL'])
            # Write the data to the CSV file
            writer.writerows(data)


# get list of urls from json file
def get_urls():
    import json
    with open('blog_links.json', 'r') as file:
        return json.load(file)
    
def save_dict_to_csv(data, filename='data.csv', url=None, blog_title=None):
    # Open the file in write mode
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
                
        # Iterate over the data dictionary and write each entry to the file
        for title, text in data.items():
            writer.writerow([title, text, url, blog_title])
