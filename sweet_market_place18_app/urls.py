#in cadrul acestui fisier definim rutele aplicatiei noastre sweet_market_place18
#Fisier creat de noi ca sa putem definii rutele respective de url
from django.urls import path
from sweet_market_place18_app.views import home_view, product_upload, ProductListView, product_details


app_name = 'sweet_market_place18_app'
urlpatterns = [
    path('', home_view, name='home'),#Dam doar o referinta nu o apelam #Numele html ului este numele de home de aceea am scris asta la name=
    path('upload_product/', product_upload, name='product_upload'), #Dam o referinta nu o apelam! accesam url ul din html cu numele de product_upload
    #DUpa aceea facem un .py cu numele de forms.py in aplicatia naostra adica in _app
    #upload_product este un html
    path('products/', ProductListView.as_view(), name='products'),#products/ este un html
    path('product/<int:product_id>/', product_details, name='product')#Trebuie precizat <int:product_id> pentru ca este un numar intreg
]