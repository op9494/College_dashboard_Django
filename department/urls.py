from django.urls import path
from . import views
urlpatterns = [
    path("",views.department,name="department"),
    path("cse",views.depcse,name="dep_cse"),
    path("auto",views.depauto,name="dep_auto"),
    path("eee",views.depeee,name="dep_eee"),
    path("noti/<str:f_path>/<str:f_folder>/<str:f_name>",views.fileopean,name="fp")
]
