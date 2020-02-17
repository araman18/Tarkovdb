from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from .models import Item
from django.template import RequestContext
from django.template import loader
from .scrape import scrape


def index(request):
    item_list = Item.objects.order_by('-price')[:15]
    template = loader.get_template('tarkovdb/index.html')
    context = {
        'item_list': item_list,
    }
    return render(request,'tarkovdb/index.html',context)

def detail(request, item_id):
    item = get_object_or_404(Item,pk=item_id)
    return render(request, 'tarkovdb/detail.html', {'item': item})

def add(request):
	if request.method == "POST":
		n = request.POST.get('Item name', 'Did not work')
		pr = scrape(n)
		i = Item(name=n,price=pr)
		i.save()
	return render(request,'tarkovdb/test.html')

def maps(request):
		template = loader.get_template('tarkovdb/maps.html')
		return render(request,'tarkovdb/maps.html')

