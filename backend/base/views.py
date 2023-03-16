from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .products import products
from .serializers import ProductSerializer


@api_view(['GET'])  # list of allowed methods
def getRoutes(request):
    routes = [
        'api/products/',
        'api/products/create/',
        'api/products/upload/',
        'api/products/<id>/reviews/',
        'api/products/top/',
        'api/products/<id>/',
        'api/products/delete/<id>/',
        'api/products/<update>/<id>/',
    ]
    return Response(routes)  # use it instead of JsonResponse


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)  # are we serializing a single object or not?
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)  # we want to return a single item

    return Response(serializer.data)
