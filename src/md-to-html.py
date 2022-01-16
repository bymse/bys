import sys

import markdown
from bs4 import BeautifulSoup

md_path = sys.argv[1]
readme = open(md_path, "r")
md = readme.read()
html = markdown.markdown(md)

soup = BeautifulSoup(html, 'html.parser')
images = soup.find_all('img')

for image in images:
    image["src"] = 'https://github.com/bymse/bys/raw/main/' + image['src']

soup.find('h1').extract()

html_file = open("templates/readme.html", "w")
html_file.write(str(soup.currentTag))
