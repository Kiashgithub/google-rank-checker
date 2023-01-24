import requests
from bs4 import BeautifulSoup
import re


# Example usage
url = 'https://www.urbankreative.com'
domain = 'urbankreative.com'
query = 'web design in kenya'
country_code = 'ke'


def track_rank(url, query, country_code):
    # Make a GET request to the Google search page for specific country
    response = requests.get(f'https://www.google.com/search?q={query}&gl={country_code}')

    # Parse the HTML of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the rank of the website
    rank = 1
    for link in soup.find_all('a'):
        if link.get('href').startswith(f'/url?q={url}'):
            return rank
        rank += 1

    # If the website is not found in the search results
    return 'Website not found in search results.'


def get_top_ten(query, location):
    # Make a GET request to the Google search page for specific location
    response = requests.get(f'https://www.google.com/search?q={query}&gl={location}')

    # Parse the HTML of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the top ten websites
    top_ten = []
    for link in soup.find_all('a'):
        if link.get('href').startswith('/url?q='):
            top_ten.append(link.get('href').replace('/url?q=', ''))
        if len(top_ten) == 10:
            return top_ten

    # If less than ten websites are found in the search results
    return top_ten

url_list = get_top_ten(query, country_code)


def get_domain_name(url):
    match = re.search(r'(?:https?://)?(?:www\.)?([\w-]+\.[\w.-]+)', url)
    return match.group(1)


def get_domain_names_from_list(url_list):
    domain_names = []
    for url in url_list:
        domain_names.append(get_domain_name(url))
    return domain_names


domain_list = get_domain_names_from_list(url_list)

#print(get_domain_names_from_list(url_list))

if url in domain_list:
    print("the domain is in top ten rank of google search")
else:
    print("Domain not in top ten")