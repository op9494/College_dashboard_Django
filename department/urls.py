from django.urls import path
from . import views
urlpatterns = [
    path("",views.department,name="department"),
    path("CSE/",views.cse,name="cse")
]
