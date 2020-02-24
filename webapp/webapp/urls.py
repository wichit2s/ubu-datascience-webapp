from django.contrib import admin
from django.urls import path, include
from myapp import views
from irisapp import views as irisview
from irisapp.urls import router

urlpatterns = [
    path('', irisview.index),

    path('api/', include(router.urls)),
    path('api/species', irisview.api_species),

    path('matmul/', views.matmul),
    path('admin/', admin.site.urls),
]
