from html.parser import HTMLParser
import requests
from urllib.parse import urlparse

def extract_domain_without_port(url):
    parsed_url = urlparse(url)
    if ':' in parsed_url.netloc:
        return parsed_url.netloc.split(':')[0]
    else:
        return parsed_url.netloc

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr.lower() == 'href':
                    self.urls.append(value)

html_file = input()
parser = MyHTMLParser()
parser.feed(requests.get(html_file).text)
domains = sorted(set(map(extract_domain_without_port, parser.urls)))
for domain in domains:
    print(domain)