from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json
    news_api_request= requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=fece1f6546bf41d0aa83ad695d20b8c2")
    api= json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api})

def tech(request):
    
    import requests
    import json
    news_api_request= requests.get("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=fece1f6546bf41d0aa83ad695d20b8c2")
    api= json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api})