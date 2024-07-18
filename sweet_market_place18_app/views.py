from django.shortcuts import render, redirect, get_object_or_404
from sweet_market_place18_app.forms import ProductForm
from django.views.generic import ListView
from sweet_market_place18_app.models import Products
# Create your views here.

def home_view(request):
    return render(request, 'sweet_market_place18_app/home.html')

#este o functie cu ajutorul careia putem sa incarcam produsele folosind un sablon
def product_upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) #Accesam pe clasa ProductForm din forms request.POST si request.FIELDS TOATE CU LITERE MARI!
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'sweet_market_place18_app/upload_product.html', context={
        'form': form
    })
    #Am incarcat template ul html upload_product in template si dam o referinta la fisierul acela

class ProductListView(ListView): #Importam from django.views.generic import ListView
    #Cu asteasta clasa creem si afisam o lista de obiecte!
    model = Products
    template_name = 'sweet_market_place18_app/products.html' #Am dat drag and drop in fisierul sweet_marketplace_app18 html ul products.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #O sa fie un dictionar care o sa aiba cheia products
        context['products'] = context['object_list']
        return context

def product_details(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    return render(request, template_name='sweet_market_place18_app/product.html', context={'product': product})

