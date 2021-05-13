from django.contrib import admin

# Register your models here.
from .models import Departments,Topper,AutoTopper,CseTopper,College_notification,EeeTopper,Department_Details_onlyA,Cse_Daily_Strength,Eee_Daily_Strength,Auto_Daily_Strength
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