import requests

cookies = {
    # 'jjSPnsABk': 'A-Q23FR7AQAAFAQ44HWgWeoob_ZVcrt1klEOaPOGNTwey8UsANKH1GyDJMuaAa21CKqcuA00wH8AAOfvAAAAAA|1|0|e7012594af0804e5347a5c6455da9e699ff6ab69',
    # 'form_key': 'CaxSjWpNKuLfhYND',
    # '__zlcmid': '15ckGKFrYigeBG1',
    # 'location': 'V5E',
    # 'preferedstorecode': 'MT',
    # 'cookiesaccepted': '%7B%22accepted%22%3Atrue%7D',
    # 'mage-cache-storage': '%7B%7D',
    # 'mage-cache-storage-section-invalidation': '%7B%7D',
    # 'mage-cache-sessid': 'true',
    # 'PHPSESSID': 'tko05h8alhntcl39hdmnoilhl2',
    # 'autocomplete': '%7B%7D',
    # 'mage-messages': '',
    # 'recently_viewed_product': '%7B%7D',
    # 'recently_viewed_product_previous': '%7B%7D',
    # 'recently_compared_product': '%7B%7D',
    # 'recently_compared_product_previous': '%7B%7D',
    # 'product_data_storage': '%7B%7D',
    # 'autocomplete-provider': '%7B%7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # # 'X-NewRelic-ID': 'VgMFUFZbDhAJXFNRBgYBVVw=',
    # # 'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI1MjEwODYiLCJhcCI6Ijk4MjQ3ODk1MCIsImlkIjoiNjIzYTg3Yzc1MjQ2ZTMwZCIsInRyIjoiNmVjMTAwNjBmNzBiNzc0MjIwODMyNmVlNjBmYjE5ZTAiLCJ0aSI6MTYyOTIzNTI5MTU4MCwidGsiOiIzNDM5NDkifX0=',
    # # 'traceparent': '00-6ec10060f70b7742208326ee60fb19e0-623a87c75246e30d-01',
    # # 'tracestate': '343949@nr=0-1-2521086-982478950-623a87c75246e30d----1629235291580',
    'X-Store-Code': 'default',
    'X-Prefered-Store-Code': 'MT',
    'X-In-Store-Pickup-Id': 'null',
    'X-Postcode': 'null',
    'X-Requested-With': 'XMLHttpRequest',
    # 'Connection': 'keep-alive',
    'Referer': 'https://www.tntsupermarket.com/fresh-frozen/fruits-vegetables.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
}

params = (
    ('categoryId', '714'),
    ('is_pickup', '0'),
    ('pageSize', '30'),
    ('page', '1'),
    # ('cat', '717,718,719,731,732'),  # vegetables
    ('cat', '715,716'),  # fruits
)

response = requests.get('https://www.tntsupermarket.com/rest/V1/xmapi/app-magento-products', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.tntsupermarket.com/rest/V1/xmapi/app-magento-products?categoryId=714&is_pickup=0&pageSize=30', headers=headers, cookies=cookies)
data = response.json()
# print(data["data"])

print(data["data"]["category"]["total_page"])
# print(len(data["data"]["category"]["items"]))

sale_items = []

for item in data["data"]["category"]["items"]:
    # print(f"{item['name']}: '{item['was_price']}'")

    if float(item["was_price"]) != 0:
        old_price = float(item["was_price"])
        new_price = float(item["prices"]["final_price"]["amount"])
        discount = round(old_price - new_price, 2)

        if discount > 0:
            row = (item['name'].strip(), old_price, new_price, discount)
            print(row)
            sale_items.append(row)
    # print(item["name"], item["was_price"], item["prices"]["final_price"]["amount"], item["review_avg_score"])


# print(data["data"]["category"])
