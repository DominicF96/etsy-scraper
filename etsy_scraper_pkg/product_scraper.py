from bs4 import BeautifulSoup
import urllib.request
import json

products = []

def productScrape(url):

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    
    print("-------------------------------------------------------------")
    
    # ID
    id = url.replace("https://www.etsy.com/ca/listing/", "").split("/")[0]
    print("Retrieving info for product '", id, "'")
    
    # Title
    title = str(soup.find("h1", {"class":"wt-text-body-03 wt-line-height-tight wt-break-word wt-mb-xs-1"} ).text).strip()
    print("\t","Found title '", title, "'")
    
    # Description
    description = str(soup.find("p", {"class":"wt-text-body-01 wt-break-word"}).text).strip()
    print("\t","Found description '", description, "'")
    
    # Currency
    currency = str(soup.find("p", {"class": "wt-text-title-03 wt-mr-xs-2"}).text).strip().split("$")[0]
    print("\t","Found currency '", currency, "'")
    
    # Price
    price = str(soup.find("p", {"class": "wt-text-title-03 wt-mr-xs-2"}).text).strip().split("$")[1]
    print("\t","Found price '", price, "'")
    
    # Materials
    materials = str(soup.find("p", {"id":"legacy-materials"} ).find("span").text.split(":")[1].split(","))
    print("\t","Found materials '", materials, "'")

    # Images
    images=[]
    carouseEntries = soup.find("ul", {"class":"wt-list-unstyled wt-overflow-hidden wt-position-relative carousel-pane-list"})
    for li in carouseEntries.findChildren("li", recursive=False):
        img = li.find("img")
        if img.get('src'):
            images.append(str(img.get('src')))
        else:
            images.append(str(img.get('data-src')))
    print("\t","Found images '", images, "'")


    # Build JSON

    products.append({
        "id": id,
        "title": title,
        "description": description,
        "currency":currency,
        "price":price,
        "materials":materials,
        "images":images,
    })

with open('links.txt','r', encoding="utf8") as links:
    for url in links:
        productScrape(url)

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump({"products": products}, f, ensure_ascii=False, indent=4)