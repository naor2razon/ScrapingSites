import requests
from bs4 import BeautifulSoup

URL = 'https://www.zimmersdaka90.co.il'      # Define URL

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='boxWrapper')

obj_elemnts = results.find_all('div', class_='recBox')
for obj_element in obj_elemnts:
   title_element = obj_element.find('a', class_='vilaName')
   location_element = obj_element.find('div', class_='vilaArea')
   phoneNum_element = obj_element.find('div', class_='phoneNum')
   if None in (title_element, location_element, phoneNum_element):
      continue
   print(title_element.text)
   print(location_element.text)
   print(phoneNum_element.text)




"""browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
"""