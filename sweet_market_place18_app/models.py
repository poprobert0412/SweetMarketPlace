from django.db import models

# Create your models here.
#Vom defini structura bazei de date
#aici scriem structura bazei de date din documentul acela, daca facem prajituri avem nevoie de urmatoarele chestii
#punem si imaginile deoarece avem nevoie de ele


class Products(models.Model):
    name = models.CharField(max_length=100) #Daca avem un titlu lung venim aici sa il refacem
    description = models.TextField()#Punem acest .TextField acolo unde AVEM TEXT
    price = models.DecimalField(max_digits=10, decimal_places=2) #Avand un pret este un pret cu decimale adica 10 lei si 50 de bani 10.5 si asa trebuie sa acesam models.DecimalField
    ingredients = models.TextField(null=True)#Nu o sa fie niciodata null adica trebuie mereu sa aibe parametrii
    weight = models.PositiveIntegerField(default=0) #Aici cum avem numere punem PositiveIntegerField
    available = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)#Daca avem imagini atunci apelamImageField si ca trebuie neaparat sa avem imagini si unde dam upload

    def __str__(self):
        return self.name

#Dupa ce scriem baza de date o sa trebuiasca sa scriem in terminal python manage.py makemigrations ca sa faca
#baza de date django ul
#dupa aceea trebuie sa scriem tot in terminal python manage.py migrate
#Dupa intram in sqlite 3 si o sa vedem numele proiectului _app product si cu aceea baza de data o sa lucram

#DUPA ASTA MERGEM IN VIEWS SA SCRIEM UN COD product_uploud sa scriem o functie in care dam uploud in sqlite3