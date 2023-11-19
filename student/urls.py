from django.urls import path
from .views import *

urlpatterns = [
    path('student/', student, name='student_home'),
    path('studentapplication/', studentapplication, name='studentapplication'),
    path('studentapplicationsave/', studentapplicationsave, name='studentapplicationsave'),
    path('student-view-attendance/', student_view_attendance, name='student-view-attendance'),
    path('result/', result , name='result')
    
]