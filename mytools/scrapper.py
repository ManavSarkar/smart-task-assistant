import requests
from bs4 import BeautifulSoup

def extract_web_content(url):
    """
    Extracts and returns the title, full text, and links from a given URL.
    
    Parameters:
        url (str): The URL of the web page to extract content from.

    Returns:
        dict: A dictionary containing 'title', 'text', and 'links'.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        return {'error': f"Failed to fetch page: {e}"}

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract page title
    title = soup.title.string.strip() if soup.title else 'No Title Found'

    # Extract visible text
    text = soup.get_text(separator='\n', strip=True)

    # Extract all href links
    links = [a['href'] for a in soup.find_all('a', href=True)]

    return {
        'title': title,
        'text': text,
        'links': links
    }
