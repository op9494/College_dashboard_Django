from django.contrib import admin

# Register your models here.
from .models import Departments,Topper,College_Details,AutoTopper,Auto_notification,Cse_notification,Eee_notification,CseTopper,College_notification,EeeTopper,Department_Details_onlyA,Cse_Daily_Strength,Eee_Daily_Strength,Auto_Daily_Strength
admin.site.register(Departments)
admin.site.register(Topper)
admin.site.register(AutoTopper)
admin.site.register(CseTopper)
admin.site.register(EeeTopper)
admin.site.register(Department_Details_onlyA)
admin.site.register(Cse_Daily_Strength)
admin.site.register(Eee_Daily_Strength)
admin.site.register(Auto_Daily_Strength)
admin.site.register(College_notification)
admin.site.register(Cse_notification)
admin.site.register(Eee_notification)
admin.site.register(Auto_notification)
admin.site.register(College_Details)