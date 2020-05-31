
from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # home page
    path('accounts/', include('accounts.urls')), # forward to accounts' urls.py
    path('products/', include('products.urls')), # forward to products' urls.py
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
