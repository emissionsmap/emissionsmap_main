from django.shortcuts import render
from geospatial.main import  barPlot, linealPlot, emisionco2

def home(request):
    n = barPlot(),
    m = linealPlot(),
    g = emisionco2()
    context={
        'barPlot':n,
        'linealPlot':m,
        'emisionPlot':g
    }
    return render(request,'index.html',context)
