import requests
from bs4 import BeautifulSoup
from utils import save_to_csv, get_urls

def scrape_and_store(url):
    # Iterate through each URL in the list
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract the title and data based on the class names
            # title is an h1 tag, remove the div inside the h1 tag            
            title_elem = soup.find('h1')
            title_elem.find('div').decompose()
            title = title_elem.get_text(strip=True)
            data = soup.find(class_='entry-content').get_text(strip=True)
            # Append the title, data, and URL to the list
            save_to_csv([[title, data, url]])
            print(f"Data successfully scraped from {url}")
        else:
            print(f"Failed to fetch {url} with status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")


if __name__ == "__main__":
    # Get the list of URLs
    urls = get_urls()

    # Call the function
    for url in urls:
        scrape_and_store(url)
