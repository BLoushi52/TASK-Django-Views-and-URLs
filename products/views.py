from itertools import product
from django.http import HttpResponse
from urllib import request
from django.shortcuts import render

from products.models import Product

# Create your views here.


def get_home(request):
    return HttpResponse(f"<h1> Hey, Welcome to our website!</h1>")

def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(f" <h3>Product Name:</h3> {product.name} <br><br> <h3>Description:</h3> {product.description}")