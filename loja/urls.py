from django.urls import path, include
from loja.views.home import Index
from loja.views.login import Login
from loja.views.signup import Signup
from loja.views.products import ProductView
from loja.views.categoria import CategoriaView
from loja.views.user import UserView
from loja.views.logout import logout_view  
from loja.views.contactos import contactos_view
from loja.views.upload_product import upload_product_view

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('products/', ProductView.as_view(), name='products'),
    path('categoria/', CategoriaView.as_view(), name='categorias'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', logout_view, name='logout'),
    path('contactos/', contactos_view, name='contactos'),  
    path("upload-product/", upload_product_view, name="upload_product"),
    path('api/', include('chat.urls'))

    ]
