import requests
import traceback
from bs4 import BeautifulSoup
from utils import save_dict_to_csv

def parse_html_to_key_value_pairs(html):
    try:
        # Initialize a dictionary to hold the headings and their corresponding texts
        headings_text = {}

        # Variables to keep track of the current heading and its accumulated text
        current_heading = None
        current_text = ""

        tags = html.find_all(['h2', 'h3', 'p', 'h4', 'li', 'div'])
        # divs_with_notion_text = html.find_all('div', class_='notion-text')
        # print(divs_with_notion_text)

        # Combine the lists if you need a unified list of elements
        all_elements = tags 

        for element in all_elements:
            if element.name in ['h2','h3', 'h4']:
                # If there's a current heading being processed, save it and its text
                if current_heading is not None:
                    headings_text[current_heading] = current_text.strip()
                # Start a new heading
                current_heading = element.get_text().strip()
                current_text = ""
            else:
                # Append text to the current heading's text
                current_text += element.get_text().strip() + " "

        # Don't forget to save the last heading and its text
        if current_heading is not None:
            headings_text[current_heading] = current_text.strip()

        # Output the dictionary
        # print(headings_text)
        return headings_text
    except Exception as e:
        traceback.print_exc()
        print(f"Error parsing HTML: {e}")


def scrape_and_store(url, filename='ivf_matters.csv'):
    # Iterate through each URL in the list
    try:
        # Send a GET request to the URL
        response = requests.get(url.strip())
        # Check if the request was successful
        print(response.status_code)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract the title and data based on the class names       
            title_elem = soup.find(class_='notion-h1')
            title = title_elem.get_text(strip=True)
            data = soup.find_all(class_='notion-column')[1]
            final_data = parse_html_to_key_value_pairs(data)
            # Append the title, data, and URL to the list
            # save key value pairs to csv
            save_dict_to_csv(final_data, filename, url=url, blog_title=title)
            print(f"Data successfully scraped from {url}")
        else:
            print(f"Failed to fetch {url} with status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

if __name__ == "__main__":        
    # Get the list of URLs
    # urls = get_urls()
    with open('blog_links.jsonl') as f:
        urls = f.readlines()
    csv_file_name = 'ivf_matters.csv'

    # Clear the file
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
        file.write('Heading,Text,URL,Blog Title\n')

    # # Call the function
    for url in urls:
        scrape_and_store(url.replace("\n", ""), filename=csv_file_name)





