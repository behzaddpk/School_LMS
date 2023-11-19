from django.urls import path
from .views import *


urlpatterns = [
    path('STAFF/', Staff_Home, name='Staff_Home'),
    path('Staff-notification/', Notification, name='Notification'),
    path('mark-notification/<str:status>/', Mark_Notification, name='Mark_Notification'),


    path('Staff-leave/', Staff_Apply_Leave, name='Staff_leave'),
    path('apply-leave-save/', Apply_Leave_save, name='Apply_Leave_save'),

    path('staff-feeback/', StaffFeedback, name='StaffFeedback'),
    path('save-staff-feeback/', feedback_save, name='feedback_save'),

    path('take-attendance/', take_attendance, name='take-attendance'),
    path('attendance/', attendance, name='attendance'),

    path('View-attendance/', view_attendance, name='view-attendance'),

    path('add_result/', add_result, name='add_result'),
    path('save_result/', save_result, name='save_result')

]