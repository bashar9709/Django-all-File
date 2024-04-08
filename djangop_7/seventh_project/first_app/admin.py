from django.contrib import admin
from first_app.models import Student, StudentInfoModel, TeacherInfoModel, EmployeeModel, ManagerModel, Friend, Me

# Register your models here.
admin.site.register(Student)
# admin.site.register(StudentInfoModel)
# admin.site.register(TeacherInfoModel)

@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'designation']
@admin.register(ManagerModel)
class ManagerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','city', 'designation', 'take_interview','hiring']    



@admin.register(Friend)
class FriendModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'section', 'attendence', 'hw']

@admin.register(Me)
class MeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'section', 'attendence', 'hw']
    