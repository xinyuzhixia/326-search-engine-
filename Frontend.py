from bottle import *
from collections import OrderedDict
historysearch={}
@route('/')
def search():
	return '<html><head><title>Googing Search</title></head>\
	<body><h1>Googing</h1><form action="/" method="post">\
		<input type="text" name="keywords" ><br>\
		<input type="submit" value="Search"></form></body></html>'

@post('/')
def do_search():
	inputkeyword = request.forms.get('keywords')
	output = check_appearance(inputkeyword)
	string = '<p>Search for "%s"</p>'%(inputkeyword)
	results = '<table id = "results"><tr> <th>Word</th> <th>Count</th></tr>'
	history = '<table id = "history"><tr> <th>Word</th> <th>Count</th></tr>'

	for key in output:
		tablecontent = '<tr><td>%s</td><td>%d</td></tr>'%(key,output[key])
		results = results+tablecontent
		store_history(key,output[key])	
	results = results+'</table>'

	for key,value in sorted(historysearch.iteritems(),key=lambda (k,v):(v,k),reverse=True):
		historyvalue='<tr><td>%s</td><td>%d</td></tr>'%(key,value)
		history = history+historyvalue
	history = history + '</table>'	
	return string + history


def store_history(key,value):
	if key in historysearch:
		historysearch[key] = historysearch[key] + value
	else:
		if len(historysearch) < 20:
			historysearch[key] = value
	return


def check_appearance(inputstring):
	#inputstring = inputstring.lower()
	splitstring = inputstring.split()
	appearance = OrderedDict()
	for key in splitstring:
		if key not in appearance:
			appearance[key] = 1
		else: 
			appearance[key] = appearance[key] + 1

	return appearance

run(host='localhost', port=8080, debug=True)