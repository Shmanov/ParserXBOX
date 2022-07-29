from django.shortcuts import render
from .models import Game
from .load import product

def index(request):
    if request.method == "POST":
        #r = requests.get('https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds=9NSDMZDFNLD4,9N7GD5JSLP4Z,C492DG1TQQ09,9PGD2M61C2B9&market=GB&languages=en-gb&MS-CV=DGU1mcuYo0WMMp+F.1')
        #for el in r.json().get("Products"):
         #   product_title = el.get("LocalizedProperties")[0].get('ProductTitle')
        Game.objects.all().delete()
        for el in product():
            Game.objects.update_or_create(**el)
            #newRecord.save()
    games = Game.objects.all()
    filds = Game._meta.get_fields()
    return render(request,'main/index.html', {'filds': filds, 'games': games})

def download(request):
    if request.method == "POST":
        #r = requests.get('https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds=9NSDMZDFNLD4,9N7GD5JSLP4Z,C492DG1TQQ09,9PGD2M61C2B9&market=GB&languages=en-gb&MS-CV=DGU1mcuYo0WMMp+F.1')
        #for el in r.json().get("Products"):
         #   product_title = el.get("LocalizedProperties")[0].get('ProductTitle')
        newRecord = Game()
        newRecord.name = "product_title"
        newRecord.rating_ms = 10
        newRecord.save()
    return render(request, 'main/download.html', locals())

