# Etsy Scraper

Retrieves info from Etsy using UrlLib and Beautiful Soup and returns the data in JSON.

**Note:** This is a web scraper, therefore, it will work until Etsy changes the tags we use to locate and
extract the different fields in the page. Be aware of that if you plan on using it in any large scale project.
Please see the Contribution section to help me keep it up-to-date!

## Installation

Run the following to install:

```python
pip install etsy_scraper
```

## Usage

To retrieve product data:

```python
from etsy_scraper.product_scraper import productScrape

# Retrieve product data from URL
productScrape(PRODUCT_URL)

# Returns
# {
#   "id": id,
#   "title": title,
#   "description": description,
#   "currency":currency,
#   "price":price,
#   "materials":materials,
#   "images":images,
# }
```

To retrieve vendor data:
```python
from etsy_scraper.vendor_scraper import vendorScrape

# Retrieve vendor data from URL
vendorScrape(VENDOR_URL)

# Returns something like
# {
#   "name": name,
#   "subtitle": subtitle,
#   "location": location,
#   "vendor_since": vendor_since,
#   "number_of_sales": number_of_sales,
#   "banner_image": banner_image,
#   "vendor_image": vendor_image,
#   "featured_products": featured_products,
#   "all_products": all_products,
# }
```

## Contribute

If you plan on using / are using the tool and notice that Etsy updated in a way that breaks this code, please
notify me, either by raising an issue or submitting a PR.

## License

This code is distributed under the MIT license.