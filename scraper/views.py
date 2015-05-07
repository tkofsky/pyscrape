from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import csv
import json
import requests
from BeautifulSoup import BeautifulSoup

def  homepage(request,):
	
	return render(request,"index.html")
	

def runscrape(request,):
	
	list_of_rows = []
	url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
	response = requests.get(url)
	html = response.content

	soup = BeautifulSoup(html)
	table = soup.find('table', attrs={'class': 'resultsTable'})




	
	cnt=0
	print "hello"
	
	for row in table.findAll('tr')[1:]:
		list_of_cells = []
		cnt=cnt+1
		for cell in row.findAll('td'):
			text = cell.text.replace('&nbsp;', '')
			list_of_cells.append(text)
			#  import pdb; pdb.set_trace()
		list_of_rows.append(list_of_cells)
    	

	print list_of_rows
	print cnt

	cxt = {
		
		"thedata":list_of_rows
	}

	json_data = json.dumps(list_of_rows)
	return HttpResponse(json_data,content_type="application/json")
	# return render(request,"scraperesults.html",cxt)


def myfunction(request,):


	import fileinput
	newstr2=""
	for line in fileinput.input(['c:\pythoncode\pattern.txt']):
	    thestring=line
	    thestring=thestring.split(",")
	    part1=thestring[0]
	    part2=thestring[1]
	    part1 = part1[(len(part1)-4):len(part1)]
	    part2 = part2[:4]
	    newstr=part1+","+part2
	    newstr2=newstr2+newstr
	    print newstr







	return HttpResponse(newstr2)




# Create your views here.
