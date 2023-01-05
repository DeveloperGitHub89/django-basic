from django.urls import path
from . import views

urlpatterns=[
    path('',views.openIndexPage),
    path('multiply',views.product),
    path('form',views.openForm),
    path('sum',views.sum)
]