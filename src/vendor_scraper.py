from bs4 import BeautifulSoup
import urllib.request
import json

def vendorScrape(url):

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    
    print("-------------------------------------------------------------")
    
    # Name
    name = str(soup.find("h1", {"class":"mb-lg-1"} ).text).strip()
    print("Retrieving info for vendor '", name, "'")
    
    # Subtitle
    subtitle = str(soup.find("span", {"data-in-modal-editable-text":"title"} ).text).strip()
    print("\t","Found subtitle '", subtitle, "'")
    
    # Location
    location = str(soup.find("span", {"class":"shop-location mr-lg-2 pr-lg-2 br-lg-1"}).text).strip()
    print("\t","Found location '", location, "'")
    
    # Vendor Since
    vendor_since = str(soup.find("span", {"class": "etsy-since no-wrap"}).text).strip().split(" ")[-1]
    print("\t","Found vendor_since '", vendor_since, "'")
    
    # Number of Sales
    number_of_sales = str(soup.find("div", {"class": "display-flex-lg flex-direction-row flex-wrap align-items-center mt-lg-1"}).findChildren("span")[0].text).strip().split(" ")[0]
    print("\t","Found number_of_sales '", number_of_sales, "'")
    
    # Banner Image
    banner_image = str(soup.find("img", {"class":"width-full display-block"} ).get("src"))
    print("\t","Found banner_image '", banner_image, "'")
    
    # Vendor Image
    vendor_image = str(soup.find("img", {"class":"rounded width-full shop-icon-external"} ).get("src"))
    print("\t","Found vendor_image '", vendor_image, "'")

    # Featured Products
    featured_products = []
    featured_products_container = soup.find("div", {"class":"featured-products-area position-relative"})
    for a in featured_products_container.findChildren("a", {"class": "wt-display-inline-block listing-link wt-transparent-card"}, recursive=True):
        url = a.get("href")
        featured_products.append({
            "url": url
            # Could add image, name, price
        })
    print("\t","Found featured_products '", len(featured_products) , "'")

    # All Products
    all_products = []
    all_products_container = soup.find("div", {"data-listings-container":True})
    for a in all_products_container.findChildren("a", {"class": "wt-display-inline-block listing-link wt-transparent-card"}, recursive=True):
        url = a.get("href")
        all_products.append({
            "url": url
            # Could add image, name, price
        })
    print("\t","Found all_products '", len(all_products) , "'")


    # Returns JSON data
    return {
        "name": name,
        "subtitle": subtitle,
        "location": location,
        "vendor_since": vendor_since,
        "number_of_sales": number_of_sales,
        "banner_image": banner_image,
        "vendor_image": vendor_image,
        "featured_products": featured_products,
        "all_products": all_products,
    }