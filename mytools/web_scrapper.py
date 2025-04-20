
from .scrapper import extract_web_content
from .web_search import search_google


def web_scrapper(query: str):
    """
    Scrapes web content based on a given query.
    This function performs a Google search using the provided query and retrieves
    the top three organic search results. For each result, it extracts the title,
    snippet, and the main content from the linked webpage. The extracted data is
    concatenated and returned as a single string.
    Args:
        query (str): The search query to be used for web scraping.
    Returns:
        str: A concatenated string web scrapped data from the top three search results.
    """

    results = search_google(query)
    
    if 'error' in results:
        return results['error']
    if 'organic' not in results:
        return "No organic results found."
    print(results)
    organic_results = results['organic'][:3]
    scrapped_data = []
    
    for result in organic_results:
        if 'link' in result:
            url = result['link']
            content = extract_web_content(url)
            if 'error' in content:
                scrapped_data.append(result['title'] + result['snippet'])
            else:
                scrapped_data.append(result['title'] + content['text'] + result['snippet'])

    scrapped_data = "\n".join(scrapped_data)
    scrapped_data = scrapped_data[:12000]  # Limit to 2000 characters
    return {
        "status": "success",
        "results": scrapped_data
    } 
