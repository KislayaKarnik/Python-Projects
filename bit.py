import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://www.bitmesra.ac.in/Visit_Other_Department_9910?cid=1&deptid=205&pid=184')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('a[href$=".pdf"]')

def notices_bit(links):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        # pprint.pprint(title)
        href = links[idx].get('href',None)
        if title != 'Access to MS Teams Account':
            hn.append({'link':href, 'title': title})
    return hn


# pprint.pprint(notices_bit(links))
dictio = notices_bit(links)
for i in dictio:
    pprint.pprint(i['title'])
    pprint.pprint(i['link']) 





