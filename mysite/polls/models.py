from concurrent.futures.process import _python_exit
from distutils.command.upload import upload
from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200, choices= settings.COUNTRIES)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Meta:
    abstract = True
    ordering = ['name',]


class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    sex = models.CharField(max_length=10, choices= settings.SEXE)
    country = models.CharField(max_length=200)

    def get_update_url(self):
        return reverse('update',kwargs={'pk':self.id})

    def __str__(self):
        return self.name

    @property
    def isMajor(self):
        return 'Majeur' if self.age >= 18 else 'Mineur'

class Magasin(Store):
    def get_update_url(self):
        return reverse('update',kwargs={'pk':self.store_ptr_id})

class ProfileMagasin(Store):
    email = models.EmailField(max_length=200,unique=True)
    phone = models.CharField(max_length=30,unique=True)
    magasin_profil = models.OneToOneField(Magasin,on_delete=models.CASCADE,related_name="magasin_profile")

    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse('update',kwargs={'pk':self.store_ptr_id})


class Produit(Store):
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="PRODUCT_IMG")
    magasin_produit = models.ForeignKey(Magasin,on_delete=models.CASCADE,related_name="product_magasin")

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse('update',kwargs={'pk':self.store_ptr_id})
