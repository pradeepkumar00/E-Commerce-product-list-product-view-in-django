from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    return render(request, 'index.html')
def product(request):
    if request.method == "GET":
        index = request.GET.get('index')
        name = request.GET.get('name')
        brand = request.GET.get('brand')
        price = request.GET.get('price')
        weight = request.GET.get('weight')
        flavour = request.GET.get('flavour')
        parameter = {'index': index, 'name': name, 'brand': brand, 'price': price, 'weight': weight,'flavour': flavour}
        return render(request, 'product.html', parameter)
    if request.method == "POST":
        index = request.POST.get('index', ' ')
        name = request.POST.get('name', ' ')
        brand = request.POST.get('brand', ' ')
        price = request.POST.get('price', ' ')
        weight = request.POST.get('weight', ' ')
        flavour = request.POST.get('flavour', ' ')
        pname = request.POST.get('pname', ' ')
        pemail = request.POST.get('pemail', ' ')
        pphone = request.POST.get('pphone', ' ')
        parameter = {'index': index, 'name': name, 'brand': brand, 'price': price, 'weight': weight, 'flavour': flavour, 'pname': pname, 'pemail': pemail, 'pphone': pphone}
        contact = Product(inde = index, name = name, brand = brand, price = price, weight = weight, flavour = flavour, pr = pname, pemail = pemail, pphone = pphone)
        contact.save()
        return render(request, 'success.html', parameter)
    else:
        return render(request,'index.html')