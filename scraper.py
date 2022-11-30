import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    citations = soup.find_all(class_="noprint Inline-Template Template-Fact")
    return len(citations)



if __name__ == "__main__":
    print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Earth'))
