import requests
import re

pattern = re.compile(r'<a\s+(?:[^>]*?\s+)?href=[\'"]?([^\'" >]+)[\'"]?', re.IGNORECASE)
doc_a, doc_b = input(), input()
found = False
for url in pattern.findall(requests.get(doc_a).text):
    if any(
        map(
            lambda u: u.replace("stepic.org", "stepik.org") == doc_b,
            pattern.findall(requests.get(url).text),
        )
    ):
        found = True
print(["No", "Yes"][found])


# def can_redirect_in_two_steps(doc_a, doc_b, step=0):
#     try:
#         response = requests.get(doc_a)
#         parser = MyHTMLParser()
#         parser.feed(response.text)
#         urls = [url.replace("stepic.org", "stepik.org") for url in parser.urls]
#         step += 1
#         if step > 2:
#             return False
#         if step == 2 and doc_b in urls:
#             return True
#         can_redirect_partial = partial(can_redirect_in_two_steps, doc_b=doc_b, step=step)
#         return any(map(can_redirect_partial, urls))
#     except (FileNotFoundError, AttributeError, requests.exceptions.ConnectionError, Exception):
#         pass

# print("Yes" if can_redirect_in_two_steps(doc_a, doc_b) else "No")


# import requests
# from functools import partial
# from html.parser import HTMLParser
#
# class MyHTMLParser(HTMLParser):
#     def __init__(self):
#         super().__init__()
#         self.urls = []
#
#     def handle_starttag(self, tag, attrs):
#         if tag == 'a':
#             for attr, value in attrs:
#                 if attr.lower() == 'href':
#                     self.urls.append(value)
#
# def can_redirect_in_two_steps(doc_a, doc_b, step=0):
#     try:
#         response = requests.get(doc_a)
#         parser = MyHTMLParser()
#         parser.feed(response.text)
#         urls = [url.replace("stepic.org", "stepik.org") for url in parser.urls]
#         step += 1
#         if step > 2:
#             return False
#         if step == 2 and doc_b in urls:
#             return True
#         can_redirect_partial = partial(can_redirect_in_two_steps, doc_b=doc_b, step=step)
#         return any(map(can_redirect_partial, urls))
#     except (FileNotFoundError, AttributeError, requests.exceptions.ConnectionError, Exception):
#         pass
#
# doc_a, doc_b = [input().replace("stepic.org", "stepik.org") for _ in range(2)]
#
# print("Yes" if can_redirect_in_two_steps(doc_a, doc_b) else "No")


# import re
# pattern = re.compile(r'<a\s+(?:[^>]*?\s+)?href=[\'"]?([^\'" >]+)[\'"]?', re.IGNORECASE)
# num_of_redirects = 0
# visited = set()
# docs = [doc_a]
#
# while docs:
#     url = docs.pop(0)
#     visited.add(url)
#     if url == doc_b:
#         break
#     response = requests.get(url)
#     if match := pattern.search(response.text):
#         match_url = match.group(1)
#         if match_url not in visited:
#             docs.append(match_url)
#             num_of_redirects += 1
#
# print(["No", "Yes"][num_of_redirects == 2 and doc_b in visited])


# pattern = re.compile(r'<a\s+(?:[^>]*?\s+)?href=[\'"]?(?:[^\'" >]+)(\b\w+\b\.html)[\'"]?', re.IGNORECASE)
# doc_a, doc_b = "sample0.html", "sample2.html"
# def can_redirect_in_two_steps(doc_a, doc_b, step=0):
#     if step > 2:
#         return
#     try:
#         with open(doc_a) as f:
#             for line in f:
#                 line = line.rstrip()
#                 link = re.match(pattern, line)
#                 if link.group(1) == doc_b and step == 2:
#                     return True
#                 if can_redirect_in_two_steps(link.group(1), doc_b, step + 1) is True:
#                     return True
#     except (FileNotFoundError, AttributeError):
#         pass
#
# print(can_redirect_in_two_steps(doc_a, doc_b))
