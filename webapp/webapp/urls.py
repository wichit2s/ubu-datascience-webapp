from django.contrib import admin
from django.urls import path
from myapp import views
from irisapp import views as irisview
urlpatterns = [
    path('', irisview.index),
    path('matmul/', views.matmul),
    path('admin/', admin.site.urls),
]
