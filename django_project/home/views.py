from django.shortcuts import render
import crispy_forms
# Create your views here.
from django.views.decorators.http import condition
from django.http import StreamingHttpResponse
import time
import requests
import requests.exceptions
import json


def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels/"
    try:
        res = requests.get(url)
        res_unicode = res.content.decode("utf-8")
        res_json = json.loads(res_unicode)
        for i in res_json["tunnels"]:
            if i['name'] == 'command_line':
                return i['public_url']
    except requests.ConnectionError as e:
        print(e)
    
    return ""


def home(request):
    s = get_ngrok_url()

    context = {
        'message':str(s),
    }
    return render(request, 'home/homepages.html', context)

def aboutus(request):
    return render(request, 'home/aboutus.html')

def smartHome(request):
    return render(request, 'home/rasp.html')

def security(request):
    return render(request, 'home/security.html')
