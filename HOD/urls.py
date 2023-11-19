from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('HOD/', HOD, name='HOD'),
    path('add-student/', Add_Student, name='Add_Student'),
    path('view-student/', View_Student, name='View_Student'),
    path('edit-student/<int:id>/', Edit_Student, name='Edit_Student'),
    path('update-student/', Update_Student, name='Update_Student'),
    path('del-student/<int:id>/', Del_Student, name='Del_Student'),

    path('add-courses/', Add_Course, name='Add_Course'),
    path('courses/', View_Course, name='View_course'),
    path('edit-course/<int:id>/', Edit_Course, name='Edit_course'),
    path('update-course/', Update_Course, name='Update_course'),
    path('del-course/<int:id>/', Del_course, name='Del_course'),


    path('add-subject/', Add_Subject, name='Add_Subject'),
    path('subject/', View_Subject, name='View_Subject'),
    path('edit-subject/<int:id>/', Edit_Subject, name='Edit_Subject'),
    path('update-subject/', Update_Subject, name='Update_Subject'),
    path('del-subject/<int:id>/', Del_Subject, name='Del_Subject'),


    path('add-staff/', Add_Staff, name='Add_Staff'),
    path('staff-view/', View_Staff, name='View_Staff'),
    path('edit-staff/<int:id>/', Edit_Staff, name='Edit_Staff'),
    path('update=staff/', Update_Staff, name='Update_Staff'),
    path('del-staff/<int:id>/', Del_Staff, name='Del_Staff'),


    path('add_session/', add_session, name='add_session'),
    path('view_session/', view_session, name='view_session'),
    path('edit_session/<int:id>/', edit_session, name='edit_session'),
    path('update_session/', update_session, name='update_session'),
    path('del_session/<int:id>/', del_session, name='del_session'),




    path('leave-application-view/', staff_leave_application_view, name='staff_leave_application_view'),
    path('leave-application-approved/<int:id>/', staff_leave_application_approved, name='staff_leave_application_approved'),
    path('leave-application-disapproved/<int:id>/', staff_leave_application_disapproved, name='staff_leave_application_disapproved'),


    path('student-leave-view/', student_leave_view, name='student_leave_view'),
    path('student_leave_application_approved/<int:id>/', student_leave_application_approved, name='student_leave_application_approved'),
    path('student_leave_application_disapproved/<int:id>/', student_leave_application_disapproved, name='student_leave_application_disapproved'),

    path('HOD/view-student-attendance/', view_student_attendance, name='view-student-attendance')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)