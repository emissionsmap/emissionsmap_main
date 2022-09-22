from django.http import HttpResponse
from pathlib import Path
import json
import os
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
jsonurl = os.path.join(BASE_DIR, 'data_restructuring/data/world.geojson')
top10 = os.path.join(BASE_DIR,'data_restructuring/data/emisiones_pais.csv')

df = pd.read_csv(top10)
topPaises = [
    {"anio":2000, "paises":list(df.sort_values('2000',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2000',ascending=False)[:10]['2000'])},
    {"anio":2001, "paises":list(df.sort_values('2001',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2001',ascending=False)[:10]['2001'])},
    {"anio":2002, "paises":list(df.sort_values('2002',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2002',ascending=False)[:10]['2002'])},
    {"anio":2003, "paises":list(df.sort_values('2003',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2003',ascending=False)[:10]['2003'])},
    {"anio":2004, "paises":list(df.sort_values('2004',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2004',ascending=False)[:10]['2004'])},
    {"anio":2005, "paises":list(df.sort_values('2005',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2005',ascending=False)[:10]['2005'])},
    {"anio":2006, "paises":list(df.sort_values('2006',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2006',ascending=False)[:10]['2006'])},
    {"anio":2007, "paises":list(df.sort_values('2007',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2007',ascending=False)[:10]['2007'])},
    {"anio":2008, "paises":list(df.sort_values('2008',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2008',ascending=False)[:10]['2008'])},
    {"anio":2009, "paises":list(df.sort_values('2009',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2009',ascending=False)[:10]['2009'])},
    {"anio":2010, "paises":list(df.sort_values('2010',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2010',ascending=False)[:10]['2010'])},
    {"anio":2011, "paises":list(df.sort_values('2011',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2011',ascending=False)[:10]['2011'])},
    {"anio":2012, "paises":list(df.sort_values('2012',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2012',ascending=False)[:10]['2012'])},
    {"anio":2013, "paises":list(df.sort_values('2013',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2013',ascending=False)[:10]['2013'])},
    {"anio":2014, "paises":list(df.sort_values('2014',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2014',ascending=False)[:10]['2014'])},
    {"anio":2015, "paises":list(df.sort_values('2015',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2015',ascending=False)[:10]['2015'])},
    {"anio":2016, "paises":list(df.sort_values('2016',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2016',ascending=False)[:10]['2016'])},
    {"anio":2017, "paises":list(df.sort_values('2017',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2017',ascending=False)[:10]['2017'])},
    {"anio":2018, "paises":list(df.sort_values('2018',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2018',ascending=False)[:10]['2018'])},
    {"anio":2019, "paises":list(df.sort_values('2019',ascending=False)[:10].pais), "emisiones":list(df.sort_values('2019',ascending=False)[:10]['2019'])},   
]

with open(jsonurl, "r") as read_content:
    dict1 = json.load(read_content)

def apiGeoJson(request):
    data = json.dumps(dict1)
    return HttpResponse(data,'application/json') 

def topContinentes(request):
    data = json.dumps(topPaises)
    return HttpResponse(data,'application/json') 