#Importam forms ul complet din django
from django import forms
from sweet_market_place18_app.models import Products
#In cadrul acestui fisier vom crea toate clasele necesare pentru formulare personalizate

#Includem o clasa Meta in clasa ProductForm cu referinta la forms.ModelForm
#Este important sa introducem classa Meta in clasa noastra
class ProductForm(forms.ModelForm):
    class Meta:#Aceasta clasa ne ajuta pe noi sa modelom FORMULARUL uploud_products nostru care o sa fie vizual
        model = Products #Facem referire la formularul pentru produsele din baza de date unde dorim sa incarcam date
        #In field ul asta introducem din models.py numele din classa Product!
        fields = [#Aici scriem coloanele din baza de date din models.py
            'name',
            'description',
            'price',
            'ingredients',
            'weight',
            'available',
            'image',
        ]
#Dupa acesta intram in views ca sa scriem def product_upload