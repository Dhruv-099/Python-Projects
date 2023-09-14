from bs4 import BeautifulSoup
import requests
import csv

pageToScrape=requests.get("http://quotes.toscrape.com")
soup=BeautifulSoup(pageToScrape.text,"html.parser")
quotes=soup.findAll("span",attrs={"class":"text"})
authors=soup.findAll("small",attrs={"class":"author"})

file=open("scrapped_quotes.csv", "w")
writer=csv.writer(file)

writer.writerow(["Quotes","Authors"])

for quote, author in zip(quotes,authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text,author.text])

file.close()