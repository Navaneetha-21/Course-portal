from django.shortcuts import render
from django.http import HttpResponse
from . mock_data import COURSES

def list_of_courses(request):
    query =request.GET.get('search','')
    course_dict=dict()

    if query:
        for code,course in COURSES.items():
            if query.lower() in course['meta']['title'].lower():
                course_dict[code]=course
    else:
        course_dict=COURSES

    context ={
        'courses' : course_dict,
    }


    return render(request,'course_lists.html',context)
