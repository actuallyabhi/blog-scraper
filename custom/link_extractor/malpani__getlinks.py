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
        blog_links = soup.find_all(class_='single-article')

        links = [link.find('a').get('href') for link in blog_links]
        return links
    else:
        print(f"Failed to fetch {url} with status code: {response.status_code}")



BASE_URL = "https://www.drmalpani.com/amp/knowledge-center/"
SLUGS = ["the-infertile-man",
"the-infertile-woman",
"coping-with-infertility",
"infertility-testing",
"ivf",
"failed-ivf",
"how-to-make-the-most-of-your-doctor",
"ivf-calender"]

for slug in SLUGS:
    url = f"{BASE_URL}{slug}"
    all_links = get_links(url)
    for x in all_links:
        print(x)
print(f"Links successfully saved to blog_links.jsonl")