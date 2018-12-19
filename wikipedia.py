import requests
from bs4 import BeautifulSoup

page = requests.get('https://en.wikipedia.org/wiki/Bear')
soup = BeautifulSoup(page.content, 'html.parser')
body = soup.find_all('body')
links = soup.find_all('a')
bearList = []
for n in range(len(links)):
    text = links[n].getText()
    if len(text) < 20:
        bearList = bearList + text.split()
print(bearList)

page2 = requests.get('https://en.wikipedia.org/wiki/Hook')
soup2 = BeautifulSoup(page2.content, 'html.parser')
body2 = soup2.find_all('body')
links2 = soup2.find_all('a')
hookList = []
for n in range(len(links2)):
    text = links2[n].getText()
    if len(text) < 20:
        hookList = hookList + text.split()
print(hookList)

print('Kenny')
print('Hello Shawn')

print("hi")
