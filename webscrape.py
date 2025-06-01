import requests
from bs4 import BeautifulSoup
from readability import Document as ReadabilityDocument
from langchain.schema import Document

def webloader(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "https://www.google.com/",
        "DNT": "1",  
        "Connection": "keep-alive"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 403:
        print("cant open url")
    
    response.raise_for_status()
    return response.text


def transform2(url):
    """Use this to scrape and extract useful text content from a given URL. Input should be a URL string."""
    html = webloader(url)
    readable = ReadabilityDocument(html).summary()
    soup = BeautifulSoup(readable, "html.parser")
    text = soup.get_text(separator="\n", strip=True)
    return [Document(page_content=text, metadata={"source": url})]

def transform(url):
    return transform2(url)
