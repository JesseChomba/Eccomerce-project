from django.shortcuts import render, get_object_or_404 ,render
from .models import Product

# Create your views here.
def product_list(request):
    products=products.objects.all()
    context={
        'products':products,

    }
    return render(request,'Ecommerce/product_list.html',context)
def product_detail(request,pk):
    product=get_object_or_404(Product,pk=pk)
    context = {
        'product':product,

    }
    return render(request,'htmlfiles',context)
