#web scraping
import requests
from bs4 import BeautifulSoup
import csv
url = "http://quotes.toscrape.com/"

response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")
with open("quotes.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Quote", "Author", "Tags"])
    
    for quote in quotes:
        text = quote.find("span", class_="text")
        author = quote.find("small", class_="author")
        tags = quote.find_all("a", class_="tag")

        quote_text = text.text if text else "nothing"
        author_name = author.text if author else "nothing"
        tag_list = ", ".join([tag.text for tag in tags]) if tags else "nothing"
        
        writer.writerow([quote_text, author_name, tag_list])

print("web scraping is done")