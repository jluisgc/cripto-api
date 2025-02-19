from bs4 import BeautifulSoup
import requests, csv

URL = "https://apewisdom.io/all-crypto/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
criptos = soup.find_all("div", class_="company-name")
criptos = str(criptos)
criptos = criptos.replace('<div class="company-name">', '|')
criptos = criptos.replace('</div>', '')
criptos = criptos.replace('[', '')
criptos = criptos.replace(']', '')
criptos = criptos.replace(', ', '')

criptoclean = criptos.split('|');
criptoclean.pop(0)

lista = []
lista.append(criptoclean[0])
lista.append(criptoclean[1])
lista.append(criptoclean[2])

with open('reddit.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(criptoclean)

print(criptoclean)