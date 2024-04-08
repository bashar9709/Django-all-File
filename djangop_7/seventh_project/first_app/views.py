from django.shortcuts import render, redirect
from . import models 

# Create your views here.

def home(request):
    student = models.Student.objects.all()
    print(student)
    return render(request,'./index.html', {'data': student})

def delete_student(request,roll):
    std = models.Student.objects.get(pk=roll).delete()
    return redirect("homepage")

def showData(request):
    # students list for one teacher
    teacher = models.Teacher.objects.get(name = 'Tarek')
    students =teacher.student.all()
    for stud in students:
        print(stud.name, stud.roll, stud.class_name)
    # teachers list for one student
    student = models.Student.objects.get(name = 'Arup')
    teachers =student.teachers.all()
    for teacher in teachers:
        print(f"{teacher.name} {teacher.subject} {teacher.mobile}")
    return render(request, 'show_data.html')
