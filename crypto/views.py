from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):

    #Get Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XLM,BCH,USDT,ADA,XRP,LTC&tsyms=USD,EUR")
    price = json.loads(price_request.content)

    #Get News Data
    news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    news = json.loads(news_request.content)

    #Render the home page
    return render(request, 'home.html',{'news': news,'price':price})

def prices(request):

    if request.method == 'POST':
        quote = request.POST["quote"]
        quote = quote.upper()
        #Get Price Data
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD,EUR")
        crypto = json.loads(crypto_request.content)

    
        return render(request, 'prices.html', {'quote':quote, 'crypto':crypto})
    else:
        #Render the prices page
        notfound = "Please enter a cryptocurrency from top right ↗️"
        return render(request, 'prices.html', {'notfound':notfound})