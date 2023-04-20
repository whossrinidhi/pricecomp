import requests
from lxml import etree
from bs4 import BeautifulSoup
amazon_product_url = "https://www.amazon.in/Sony-Bravia-inches-Google-XR-55A80K/dp/B09ZLMV9V4/ref=sr_1_7?crid=17QDVXW65Z09N&keywords=sony+led+tv+55+inch&qid=1680516925&sprefix=sony+led+tv+55+inch%2Caps%2C257&sr=8-7"
flipkart_product_url = "https://www.flipkart.com/sony-139-cm-55-inch-oled-ultra-hd-4k-smart-google-tv/p/itmd16681001c38e?pid=TVSGHESCP6GSF5KU&lid=LSTTVSGHESCP6GSF5KU85ST9R&marketplace=FLIPKART&q=sony+139cm+xr+55a+80k&store=ckf%2Fczl&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=49ccd70b-93af-4f54-9390-86250c9a8e73.TVSGHESCP6GSF5KU.SEARCH&ppt=sp&ppn=sp&ssid=qtb0uojn9s0000001680517087399&qH=a991eb4b1f6e3c0c"
croma_product_url = "https://www.croma.com/canon-eos-200d-ii-24-1-mp-dslr-camera-18-55-mm-lens-22-3-x-14-9-mm-optical-image-stabilization-/p/267968"
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
amazon_page = requests.get(url=amazon_product_url, headers=headers) 
amazon_soup = BeautifulSoup(amazon_page.content,"html.parser") 
print("in amazon:")
amazon_title = amazon_soup.find(id="productTitle")
amazon_text = amazon_title.get_text() # Will get text from html tags
aproduct_title = amazon_text.strip() # Removing special characters like \n (newline)
print(aproduct_title )
aprice = amazon_soup.find(class_="a-price-whole")
aptext = aprice.get_text()
aproduct_price = aptext.strip()
print(aproduct_price)
flipkart_page = requests.get(url=flipkart_product_url,headers=headers)
flipkart_soup = BeautifulSoup(flipkart_page.content,"html.parser")
print("in flipkart")
flipkart_title = flipkart_soup.find(class_="B_NuCI")
flipkart_title_text = flipkart_title.get_text()
print(flipkart_title_text)
flipkart_price = flipkart_soup.find(class_="_30jeq3 _16Jk6d")
flipkart_price_text = flipkart_price.get_text()
print(flipkart_price_text)
# croma_page = requests.get(url=croma_product_url,headers=headers)
# croma_soup = BeautifulSoup(croma_page.content,"html.parser")
# pretty = croma_soup.prettify()
