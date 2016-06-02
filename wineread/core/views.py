from django.shortcuts import render
import csv
import json
import urllib.request as urllib
import collections
from django.conf import settings



# Create your views here.
def all(request):
	data = []
	selectedKey = 'Class'

	keys = ["Class","Alcohol","Malic acid","Ash","Alcalinity", "Magnesium", "Total phenols",
		"Flavanoids", "N. Phenols", "Proanthocyanins", "Color Int.", "Hue", "OD280/OD315 of diluted wines",
		"Proline"]

	url = settings.BASE_DIR+'/wine.csv'

	with open(url, 'r') as f:
	    reader = csv.reader(f) 
	    for row in reader:
	        data.append(dict(zip(keys, row)))

	return render(request, 'index.html', {'data':data, 'keys':keys})

def detailed(request):
	data = []
	selectedKey = 'Class'

	if request.method == 'POST':
		selectedKey = request.POST.get('selectedKey')

	keys = ["Class","Alcohol","Malic acid","Ash","Alcalinity", "Magnesium", "Total phenols",
		"Flavanoids", "N. Phenols", "Proanthocyanins", "Color Int.", "Hue", "OD280/OD315 of diluted wines",
		"Proline"]

	url = settings.BASE_DIR+'/wine.csv'

	with open(url, 'r') as f:
	    reader = csv.reader(f) 
	    for row in reader:
	        data.append(dict(zip(keys, row)))

	filterdata = [] 
	
	for row in data:
		filterdata.append(float(row[selectedKey]))

	frequency = collections.Counter(filterdata)

	frequency = collections.OrderedDict(sorted(frequency.items()))

	return render(request, 'detalhada.html', {'filterdata':filterdata,'frequency':frequency.items(),'keys':keys, 'selectedKey':selectedKey})