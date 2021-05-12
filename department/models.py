from django.db import models
from django.db.models.expressions import Value

# Create your models here.

class Departments(models.Model):
    department_code=models.IntegerField()
    department_name=models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.department_code}:{self.department_name }"
class Topper(models.Model):
    rank1=models.CharField(max_length=64)
    rank1_dep=models.ForeignKey(Departments,on_delete=models.CASCADE,related_name="rank1_name")
    rank2=models.CharField(max_length=64)
    rank2_dep=models.ForeignKey(Departments,on_delete=models.CASCADE,related_name="rank2_name")
    rank3=models.CharField(max_length=64)
    rank3_dep=models.ForeignKey(Departments,on_delete=models.CASCADE,related_name="rank3_name")
    
    def __str__(self):
        return f"First Rank {self.rank1  } || Second rank {self.rank2  }|| Third Rank  {self.rank3 }" 

class CseTopper(models.Model):
    rank1=models.CharField(max_length=64)
    rank2=models.CharField(max_length=64)
    rank3=models.CharField(max_length=64)
    def __str__(self):
        return f"First Rank {self.rank1  } || Second rank {self.rank2  }|| Third Rank  {self.rank3  }" 
  
class EeeTopper(models.Model):
    rank1=models.CharField(max_length=64)
    rank2=models.CharField(max_length=64)
    rank3=models.CharField(max_length=64)
    def __str__(self):
        return f"First Rank {self.rank1  } || Second rank {self.rank2  }|| Third Rank  {self.rank3  }" 
    


class AutoTopper(models.Model):
    rank1=models.CharField(max_length=64)
    rank2=models.CharField(max_length=64)
    rank3=models.CharField(max_length=64)
    def __str__(self):
        return f"First Rank {self.rank1  } || Second rank {self.rank2  }|| Third Rank  {self.rank3  }" 
    

class Department_Details_onlyA(models.Model):
    academic_Year=models.DateField()
    secondYearCse=models.IntegerField()
    thirdYearCse=models.IntegerField()
    finalYearCse=models.IntegerField()
    #total_Cse_Students=models.IntegerField(Value=secondYearCse+thirdYearCse+finalYearCse)
    total_Cse_staffs=models.IntegerField()
    #eee
    secondYearEee=models.IntegerField()
    thirdYearEee=models.IntegerField()
    finalYearEee=models.IntegerField()
    #total_Eee_Students=models.IntegerField(editable=False)
    total_Eee_staffs=models.IntegerField()
    #auto
    secondYearAuto=models.IntegerField()
    thirdYearAuto=models.IntegerField()
    finalYearAuto=models.IntegerField()
    #total_Auto_Students=models.IntegerField(editable=False)
    total_Auto_staffs=models.IntegerField()
    #Ovellall college Student details
    #total_no_students=models.Sum(total_Auto_Students,total_Cse_Students,total_Eee_Students)
    #total_no_staffs=models.Sum(total_Eee_staffs,total_Auto_staffs,total_Cse_staffs)    



      
class Cse_Daily_Strength(models.Model):
    date_of_attendence=models.DateField()
    second_year_present=models.IntegerField()
    third_year_present=models.IntegerField()
    final_year_present=models.IntegerField()
#    tota_no_students_present=second_year_present+third_year_present+final_year_present
    staffs_present=models.IntegerField()
class Eee_Daily_Strength(models.Model):
    date_of_attendence=models.DateField()
    second_year_present=models.IntegerField()
    third_year_present=models.IntegerField()
    final_year_present=models.IntegerField()
#    tota_no_students_present=second_year_present+third_year_present+final_year_present
    staffs_present=models.IntegerField()

class Auto_Daily_Strength(models.Model):
    date_of_attendence=models.DateField()
    second_year_present=models.IntegerField()
    third_year_present=models.IntegerField()
    final_year_present=models.IntegerField()
    staffs_present=models.IntegerField()
    #    tota_no_students_present=second_year_present+third_year_present+final_year_present
    def __str__(self):
        return f"Date {self.date_of_attendence  } || Staffspresent {self.staffs_present  }|| Totalstudents {self.second_year_present+self.third_year_present+self.final_year_present}" 
    
    


