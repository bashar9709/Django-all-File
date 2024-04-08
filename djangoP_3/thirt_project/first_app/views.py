from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request,'./first_app/index.html',{'author':'Bashar', 'age': 15,'marks': 19,
                                'courses': [
                                {
                                    'id': 1,
                                    'course':'c',
                                    'teacher':'Rahim'
                                },
                                {
                                    'id': 2,
                                    'course':'c++',
                                    'teacher':'Bashar'
                                },
                                {
                                    'id': 3,
                                    'course':'python',
                                    'teacher':'Babul'
                                },],
                                "name":"I am Bashar", "marks": 86, "lst":[24,3,10,5], "blog":"Lorem ipsum dolor, sit amet contesctercture adipisincing elit. Haram quetempore fight laborum valuptas mollitia. Explicabo earum assumend abaecati etc."
                            
                                   })