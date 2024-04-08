from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, './first_app/home.html',{"name":"I am Bashar", "marks": 88,
    "courses" : [
      { 
       "id" : 1,
       "course" : "c",
       "teacher" : "Bashar"

       },
      { 
       "id" : 2,
       "course" : "c++",
       "teacher" : "Baki"

       },
      { 
       "id" : 3,
       "course" : "python",
       "teacher" : "Babu"

       },      
    ]})
    
def about(request):
     return render(request, './first_app/about.html',{'author':'bashar'})
        
