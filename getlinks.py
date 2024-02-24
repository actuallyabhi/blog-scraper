import requests

from bs4 import BeautifulSoup


def get_links(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        # get the urls of link with have class of the a
        links = [link.get('href') for link in soup.find_all(class_='article__link')]
        return links
    else:
        print(f"Failed to fetch {url} with status code: {response.status_code}")


all_links = []
FIRST_PAGE = 1
LAST_PAGE = 10
for x in range(FIRST_PAGE, LAST_PAGE + 1):
    url = f'https://www.ivfmatters.co.uk/blogs/news?page={x}'
    all_links.extend(get_links(url))
    
import json
with open('blog_links.json', 'w') as file:
    json.dump(all_links, file)
print(f"Links successfully saved to blog_links.json")
