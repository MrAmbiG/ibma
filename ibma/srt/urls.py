from django.urls import path, include
from .views import *
from .models import *
from rest_framework import routers
from srt import views as srt_views

router = routers.DefaultRouter()
router.register('py37', py37View)

urlpatterns = [
    path('', include(router.urls)),
    path('<slug:model>/<slug:uid>/output',
         srt_views.outputter, name="outputter")
]
