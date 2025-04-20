import requests
import json
import os

def search_google(query: str) -> dict:
    """
    Perform a Google search using the Serper API and return the search results.
    Args:
        query (str): The search query string.
    Returns:
        dict: The JSON response from the Serper API containing the search results.
    
    """
    url = "https://google.serper.dev/search"
    payload = json.dumps({
    "q": query,
    })
    headers = {
    'X-API-KEY': os.getenv("SERPER_API_KEY"),
    'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return {'error': f"Failed to fetch search results: {e}"}
