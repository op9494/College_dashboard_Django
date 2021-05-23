from django.shortcuts import render
from .models import Departments
from plotly.offline import plot
from plotly.graph_objs import Scatter
from .models import Departments,Topper,College_Details,Eee_notification,Auto_notification,AutoTopper,CseTopper,College_notification,Cse_notification,EeeTopper,Department_Details_onlyA,Cse_Daily_Strength,Eee_Daily_Strength,Auto_Daily_Strength
import mimetypes
import os
from django.http import HttpResponse

# Create your views here.
def department(request):  #College Dashboard View
    College=College_Details.objects.all()
    College_name=get_array(College_Details,'college_name')
    print(f"hi{College_name[0]}") 
    department_det=Department_Details_onlyA.objects.all()
    csetotal=department_det[0].finalYearCse+department_det[0].thirdYearCse+department_det[0].secondYearCse
    autototal=department_det[0].finalYearAuto+department_det[0].thirdYearAuto+department_det[0].secondYearAuto
    eeetotal=department_det[0].finalYearEee+department_det[0].thirdYearEee+department_det[0].secondYearEee
    print(f"department details {csetotal,autototal, eeetotal }")
    pielabels = ["CSE","EEE","AUTO"]
    piedata = [csetotal,autototal,eeetotal]
    barlabels = ["CSE","EEE","AUTO"]
    bardata = [csetotal,autototal,eeetotal]
    return render(request,"department/home.html",{
        "tittle":College_name[0],
        "csetoppers":Topper.objects.all(),
        "departments":Departments.objects.all(),
        "notification_list":College_notification.objects.all(),        
       # 'plot_div': plot_div,
       'labels1': pielabels,
        'data1': piedata,
        'labels2': barlabels,
        'data2': bardata,
        'final_s':autototal,
        'thirt_s':csetotal,
        'second_s':eeetotal,
                  })


def get_array(Table, column):
    rows = Table.objects.values(column)
    return [row[column] for row in rows]
    
def depcse(request):
   
    attendence_det=Cse_Daily_Strength.objects.all()
    date=get_array(Cse_Daily_Strength,'attendence_date')
    da_snip=[]
    rows=Cse_Daily_Strength.objects.values('attendence_date')
    
    for i in range(0,len(date)):
        s_date=date[i].date().day
        da_snip.append(s_date)
    final_strength=get_array(Cse_Daily_Strength, 'final_year_present')
    second_strength=get_array(Cse_Daily_Strength, 'second_year_present')
    third_strength=get_array(Cse_Daily_Strength, 'third_year_present')
    total=[]
    for i in range(0,len(final_strength)):
        total_strn=final_strength[i]+second_strength[i]+third_strength[i]
        total.append(total_strn)
    
    print(f"date={da_snip}\n total={total} ")
    x_data = da_snip
    y_data=total
    plot_div = plot([Scatter(x=x_data, y=y_data,opacity=1, marker_color='black')],output_type='div')
    dp_name="Computer Science and engineering"
    return render(request,"department/CSE.html",{
        "tittle":dp_name,
        "csetoppers":CseTopper.objects.all(),
        "departments":Departments.objects.all(),
        "notification_list":Cse_notification.objects.all(),        
        'plot_div': plot_div,
        'final_s':final_strength[len(final_strength)-1],
        'thirt_s':third_strength[len(third_strength)-1],
        'second_s':second_strength[len(third_strength)-1],
    })
def depeee(request):
    attendence_det=Eee_Daily_Strength.objects.all()
    date=get_array(Eee_Daily_Strength,'attendence_date')
    da_snip=[]
    rows=Eee_Daily_Strength.objects.values('attendence_date')
    
    for i in range(0,len(date)):
        s_date=date[i].date().day
        da_snip.append(s_date)
    final_strength=get_array(Eee_Daily_Strength, 'final_year_present')
    second_strength=get_array(Eee_Daily_Strength, 'second_year_present')
    third_strength=get_array(Eee_Daily_Strength, 'third_year_present')
    total=[]
    for i in range(0,len(final_strength)):
        total_strn=final_strength[i]+second_strength[i]+third_strength[i]
        total.append(total_strn)
    
    print(f"date={da_snip}\n total={total} ")
    x_data = da_snip
    y_data=total
    plot_div = plot([Scatter(x=x_data, y=y_data,opacity=1, marker_color='black')],output_type='div')
    dp_name="Electrical and electronics engineering"
    return render(request,"department/EEE.html",{
        "tittle":dp_name,
        "eeetoppers":EeeTopper.objects.all(),
        "departments":Departments.objects.all(),
        "notification_list":Eee_notification.objects.all(),        
        'plot_div': plot_div,
        'final_s':final_strength[len(final_strength)-1],
        'thirt_s':third_strength[len(third_strength)-1],
        'second_s':second_strength[len(third_strength)-1],

        })
def depauto(request):
    attendence_det=Auto_Daily_Strength.objects.all()
    date=get_array(Auto_Daily_Strength,'attendence_date')
    da_snip=[]
    rows=Auto_Daily_Strength.objects.values('attendence_date')
    
    for i in range(0,len(date)):
        s_date=date[i].date().day
        da_snip.append(s_date)
    final_strength=get_array(Auto_Daily_Strength, 'final_year_present')
    second_strength=get_array(Auto_Daily_Strength, 'second_year_present')
    third_strength=get_array(Auto_Daily_Strength, 'third_year_present')
    total=[]
    for i in range(0,len(final_strength)):
        total_strn=final_strength[i]+second_strength[i]+third_strength[i]
        total.append(total_strn)
    
    print(f"date={da_snip}\n total={total} ")
    x_data = da_snip
    y_data=total
    plot_div = plot([Scatter(x=x_data, y=y_data,opacity=1, marker_color='black')],output_type='div')
    dp_name="Automobile and engineering"
    return render(request,"department/AUTO.html",{
        "tittle":dp_name,
        "tittle":dp_name,
        "autotoppers":AutoTopper.objects.all(),
        "departments":Departments.objects.all(),
        "notification_list":Auto_notification.objects.all(),        
        'plot_div': plot_div,
        'final_s':final_strength[len(final_strength)-1],
        'thirt_s':third_strength[len(third_strength)-1],
        'second_s':second_strength[len(third_strength)-1],
        })

        
        
def fileopean(request,f_path,f_name,f_folder):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"--------{BASE_DIR}------")
    # Define the full file path
    filepath = BASE_DIR+'/'+f_path+'/'+f_folder+'/'+f_name
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
        
