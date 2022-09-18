from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import json
import os
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
jsonurl = os.path.join(BASE_DIR, 'data/world.geojson')

with open(jsonurl, "r") as read_content:
    dict1 = json.load(read_content)

def inicio(request):
    return render(request,'api.html')
 
def apiGeoJson(request):
    data = json.dumps(dict1)
    return HttpResponse(data,'application/json') 