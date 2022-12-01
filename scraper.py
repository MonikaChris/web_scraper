import requests
from bs4 import BeautifulSoup
import re


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    citations = soup.find_all(class_="noprint Inline-Template Template-Fact")
    return len(citations)


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Get list of all paragraphs
    paragraphs = soup.find_all("p")

    # Report to be returned
    report = ''

    # Tag on paragraphs needing citation
    pattern = r'(<sup class="noprint Inline-Template)'

    # From list of paragraphs, grab the ones needing citations
    for par in paragraphs:
        if re.search(pattern, str(par)):
            report += par.get_text() + '\n'

    return report




if __name__ == "__main__":
    #print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Earth'))
    print(get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Earth'))
