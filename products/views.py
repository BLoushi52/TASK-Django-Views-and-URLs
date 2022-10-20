from itertools import product
from multiprocessing import context
from django.http import HttpResponse
from urllib import request
from django.shortcuts import render

from products.models import Product

# Create your views here.


def get_home(request):
    return HttpResponse(f"<h1> Hey, Welcome to our website!</h1>")


# def get_product(request, product_id):
#     product = Product.objects.get(id=product_id)
#     return HttpResponse(
#         f"""
#          <h2>Product ID: {product_id} </h2>
#          <h3>Product Name: </h3>{product.name}
#          <br>
#          <br>
#          <h3>Description: </h3>{product.description}"
#          """
#     )


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": {
            "product_id": product_id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
        }
    }
    return render(request, "product_detail.html", context)


def get_products(request):

    products = Product.objects.all()
    new_products = []
    for product in products:
        new_products.append(
            {"id": product.id, "name": product.name, "price": product.price}
        )
    context = {"products": new_products}
    return render(request, "product_list.html", context)
