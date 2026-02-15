
from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('products/', products_view, name='products'),
    path('contact', contact_view)

]
