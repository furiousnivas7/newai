import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # For demonstration, let's say we scrape paragraphs only
    paragraphs = soup.find_all('p')
    return " ".join([para.text for para in paragraphs])
