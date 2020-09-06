from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from  math import ceil

def index(request):
  #products = Product.objects.all()
   #print(products)
   #n= len(products)
   #nSlides = n//4 + ceil((n/4)-(n//4))
  # params ={'no_of_slides': nSlides, 'range': range(1, nSlides),'products': products}
   #allProds=[[products, range(1,nSlides), nSlides],[products, range(1,nSlides),nSlides]]
   #params= {'allProds':allProds}

   allProds = []
   catprods= Product.objects.values('product_category','id')
   cats= {item['product_category'] for item in catprods}
   for cat in cats:
       prod=Product.objects.filter(product_category=cat)
       n = len(prod)
       nSlides = n // 4 + ceil((n / 4) - (n // 4))
       allProds.append([prod, range(1,nSlides), nSlides])
       context={
          'allProds':allProds
       }

   return render(request, 'shop/index.html',context)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("Welcome to the about page")


def tracker(request):
    return HttpResponse("Welcome to the Tracker page")


def search(request):
    return HttpResponse("Welcome to the search page")


def productView(request):
    return HttpResponse("Welcome to the product view page")


def checkout(request):
    return HttpResponse("Welcome to the checkout  page")

