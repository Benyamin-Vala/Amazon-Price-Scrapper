import requests

headerV2 = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"accept-language": "en-US,en;q=0.9,fa;q=0.8",
"cache-control": "max-age=0",
"referer": "https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "same-origin",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"user-agent": "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2"
}

session = requests.session()
print('Please Enter Target Amazon Product Url For Scrape That Price: ')
productUrl = input()
response = session.get(productUrl,headers=headerV2)

try:
    price = response.text.split('<span class="a-offscreen">')[1].split('<')[0]
    print('Product Price : '+price)
except:
   
    print('Product Dose Not Have Any Price !')
        