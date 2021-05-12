from django.shortcuts import render
from .models import Departments
# Create your views here.
def department(request):
    CollegeName="Example College Name"
    return render(request,"department/home.html",{
                  "cg_name":CollegeName})
    
def cse(request):
    return render(request,"department/CSE.html",{"departments":Departments.objects.all()})