"""
URL configuration for projetoPDI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from . import settings 
from django.urls import path
from loja.views.upload_product import upload_product_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja.urls')), 
    path("upload-product/", upload_product_view, name="upload_product"),
    path('api/', include('chat.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
