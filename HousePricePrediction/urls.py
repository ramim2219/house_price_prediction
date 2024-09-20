from django.contrib import admin
from django.urls import path
from .views import home, predict, result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('predict/', predict, name='predict'),
    path('predict/result/', result, name='result'),
]
