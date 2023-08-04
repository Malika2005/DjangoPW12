from django.shortcuts import render, redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('product_list')

def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.count_on_stock = request.POST['count_on_stock']
        product.save()
        return redirect('product_list')
    return render(request, 'edit_product.html', {'product': product})