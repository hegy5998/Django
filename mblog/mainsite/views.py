from django.shortcuts import render
from django.http import HttpResponse
from .models import Artwork
from django.template.loader import get_template
import random
# Create your views here.

def about(request):
	template = get_template('about.html')
	quotes = ['123','rthyt','ergtryt','ewretry','wefrt']
	html = template.render({'quote':random.choice(quotes)})
	return HttpResponse(html)

def homepage(request):
	template = get_template('index.html')
	#tags = '1.shop\n'+'2.artwork\n'+'3.tea'
	html = template.render()

	return HttpResponse(html)
	
def artwork_page(request):
	html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>藝術品列表</title>
</head>
<body>
<h2>藝術品總庫存</h2>
<hr>
<table width=1000 border=1 bgcolor='#ccffcc'>
{}
</table>
</body>
</html>
'''
	artworks = Artwork.objects.all()
	tags = '<tr><td>No.</td><td>藝術品名稱</td><td>藝術品編號</td><td>售價</td><td>所在位置</td><td>作者</td></tr>'
	for c,i in enumerate(artworks):
		tags = tags+'<tr><td>'+str(c+1)+'</td>'
		tags = tags+'<td>'+str(i.name)+'</td>'
		tags = tags+'<td>'+str(i.product_num)+'</td>'
		tags = tags+'<td>'+str(i.price)+'(NT)'+'</td>'
		tags = tags+'<td>'+str(i.shop)+'</td>'
		tags = tags+'<td>'+str(i.artist)+'</td></tr>'
	
	return HttpResponse(html.format(tags))

def tea_page(request):
	html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>茶葉列表</title>
</head>
<body>
<h2>茶葉總庫存</h2>
<hr>
<table width=1000 border=1 bgcolor='#ccffcc'>
{}
</table>
</body>
</html>
'''
'''
	tea = Tea.objects.all()
	tags = '<tr><td>No.</td><td>茶葉名稱</td><td>茶葉斤數</td><td>售價</td><td>生產地</td></tr>'
	for c,i in enumerate(tea):
		tags = tags+'<tr><td>'+str(c+1)+'</td>'
		tags = tags+'<td>'+str(i.name)+'</td>'
		tags = tags+'<td>'+str(i.stock)+'(斤)'+'</td>'
		tags = tags+'<td>'+str(i.price)+'(NT)/(斤)'+'</td>'
		tags = tags+'<td>'+str(i.origin)+'</td>'
	
	return HttpResponse(html.format(tags))
'''
