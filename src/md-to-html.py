import sys

import markdown
from bs4 import BeautifulSoup

md_path = sys.argv[1]
readme = open(md_path, "r")
md = readme.read()
html = markdown.markdown(md)

soup = BeautifulSoup(html, 'html.parser')

for image in soup.find_all('img'):
    image["src"] = 'https://github.com/bymse/bys/raw/main/' + image['src']

for link in soup.find_all('a'):
    link["target"] = "_blank"
    link["rel"] = "noreferrer noopener nofollow"

soup.find('h1').extract()

html_file = open("templates/readme.html", "w")
html_file.write(str(soup.currentTag))
