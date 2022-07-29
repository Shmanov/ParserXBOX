import requests

def str_id():
    url_reco = 'https://reco-public.rec.mp.microsoft.com/channels/Reco/V8.0/Lists/Computed/TopPaid?Market=gb&Language=en&ItemTypes=Game&deviceFamily=Windows.Xbox&count=2000&skipitems=0'
    reco = requests.get(url_reco).json().get('Items')
    list_id = []
    for el in reco:
        id = el.get('Id')
        list_id.append(id)

    return ','.join(list_id)





def product():
    id = str_id()
    products = []
    url = 'https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds='+ id + '&market=GB&languages=en-gb&MS-CV=DGU1mcuYo0WMMp+F.1'
    r = requests.get(url)
    i = 0
    for el in r.json().get("Products"):
        i += 1
        prod = {}
        prod['id'] = el.get("ProductId")
        prod['name'] = el.get("LocalizedProperties")[0].get('ProductTitle')
        prod['rating_ms'] = i
        ListPrice = el.get("DisplaySkuAvailabilities")[0].get('Availabilities')[0].get('OrderManagementData').get('Price').get('ListPrice')
        MSRP = el.get("DisplaySkuAvailabilities")[0].get('Availabilities')[0].get('OrderManagementData').get('Price').get('MSRP')
        if float(ListPrice) >= float(MSRP):
            prod['now_on_sale'] = False
        else:
            prod['now_on_sale'] = True
        products.append(prod)
    return products
a= product()
print(1)