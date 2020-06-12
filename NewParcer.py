import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://cbr.ru/')
main_text = r.text
soup = BS(main_text)

table = soup.find('div', {'class':'mobile-indicator_courses'})
dol_val = table.find('div', {'class':'value'})

euro_temp = dol_val.findNext('div', {'class':'value'})
dol_val = dol_val.text
euro_val = euro_temp.findNext('div', {'class':'value'})
euro_val = euro_val.text
print("Курс доллара: " + dol_val)
print("Курс евро: " + euro_val)
