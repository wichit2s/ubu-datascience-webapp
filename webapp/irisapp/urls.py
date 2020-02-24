from django.conf.urls import url, include
from rest_framework import routers

from .views import SpeciesViewSet

router = routers.DefaultRouter()
router.register('species', SpeciesViewSet)
