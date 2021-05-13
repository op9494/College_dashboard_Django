from django.urls import path
from . import views
urlpatterns = [
    path("",views.department,name="department"),
    path("CSE/",views.cse,name="cse"),
    path("download/<str:f_path>/<str:f_name>",views.fileopean,name="fp")
]
