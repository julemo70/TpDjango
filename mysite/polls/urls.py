"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from polls.views import *

urlpatterns = [
    path('', index, name='home'),
    path('update/<int:pk>/',update_person,name='update'),
    path('create/produit',createProduit,name='create_produit'),
    path('create/magasin',createMagasin,name='create_magasin'),
    path('create/profile-magasin',createProfileMagasin,name='create_magasin_profile'),
    path('update/produit/<int:pk>/',update_produit,name='update_produit'),
    path('create/magasin/<int:pk>/',update_magasin,name='update_magasin'),
    path('create/magasinProfil/<int:pk>/',update_magasin,name='update_magasin_profile'),
]
