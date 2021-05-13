from django.shortcuts import render
from .models import Departments
from plotly.offline import plot
from plotly.graph_objs import Scatter
from .models import Departments,Topper,AutoTopper,CseTopper,College_notification,EeeTopper,Department_Details_onlyA,Cse_Daily_Strength,Eee_Daily_Strength,Auto_Daily_Strength
import mimetypes
import os
from django.http import HttpResponse

# Create your views here.
def department(request):  #College Dashboard View 
    CollegeName="Tamilnadu College Of Engineering"
    department_det=Department_Details_onlyA.objects.all()
    csetotal=department_det[0].finalYearCse+department_det[0].thirdYearCse+department_det[0].secondYearCse
    autototal=department_det[0].finalYearAuto+department_det[0].thirdYearAuto+department_det[0].secondYearAuto
    eeetotal=department_det[0].finalYearEee+department_det[0].thirdYearEee+department_det[0].secondYearEee
    print(f"department details {csetotal,autototal, eeetotal }")
    return render(request,"department/home.html",{
                    "cg_notification":College_notification.objects.all(),
                  "cg_name":CollegeName,
                  "csetotal":csetotal,
                  "autototal":autototal,
                  "eeetotal":eeetotal
                  
                  
                  
                  })
    
def cse(request):
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request,"department/CSE.html",{
        "departments":Departments.objects.all(),
        'plot_div': plot_div
        })    
def fileopean(request,f_path,f_name):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"--------{BASE_DIR}------")
    # Define the full file path
    filepath = BASE_DIR+'/'+f_path+'/'+f_name
    print(f"--------{filepath}------")
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % f_name
    # Return the response value
    return response
        
