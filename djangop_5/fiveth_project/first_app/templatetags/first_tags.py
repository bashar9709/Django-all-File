from django import template
from django.template.loader import get_template

register = template.Library()

# custom tag 
def my_template(value,arg):
     if arg=='change':
         value = 'Rahim'
         return value
     if arg == 'title':
         return value.title()

register.filter('change_name', my_template)

# custom templete
def show_courses():
    courses = [
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

       },]
    return {'courses' : courses}   
courses_template = get_template('first_app/courses.html') 
register.inclusion_tag(courses_template)(show_courses)  
    
    

     