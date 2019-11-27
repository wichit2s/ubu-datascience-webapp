from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('matmul', views.matmul),
    path('admin/', admin.site.urls),
]
