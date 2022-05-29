
from distutils.command.build import build
from django.urls import include, path

from .views import builder

urlpatterns = [
    path('', builder,name='builder'),
]
