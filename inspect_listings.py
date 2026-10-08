# Print the text of every .price match. Check the results against the five prices in the browser.
# Predictions
# .item            -> 5
# .badge           -> 5
# .free-shipping   -> 3
# .sponsored       -> 1
# #results > li    -> 5
# .item + .item    -> 5
# li.item > a      -> 5

from bs4 import BeautifulSoup
from lab_selectors import extract_listings

with open('sample_merchandise.html', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('.price'):
    print(tag.text)

selectors = [".item", ".badge", ".free-shipping", ".sponsored",
             "#results > li", ".item + .item", "li.item > a"]

for selector in selectors:
    print(selector, len(soup.select(selector)))

records = extract_listings(html)
for record in records:
    print(record['name'])

# Phrases = jobs, freedom, MAGA - I predict freedom will appear most