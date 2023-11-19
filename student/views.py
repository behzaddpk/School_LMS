from django.shortcuts import render, redirect
from HOD.models import *
from .models import *
from django.contrib import messages

# Create your views here.


def student(request):
    return render(request, 'student_home.html')


def studentapplication(request):
    user = request.user
    student = Student.objects.filter(admin = user)
    for i in student:
        
        student = i.id

        student_leave_history = Student_leave.objects.filter(student_id = student)


    context = {
        'student_leave_history': student_leave_history
    }
    return render(request, 'application.html', context)


def studentapplicationsave(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        student_id = Student.objects.get(admin = request.user.id)

        leave = Student_leave(
            student_id = student_id,
            date = leave_date,
            message = leave_message
        ) 
        leave.save()
        messages.success(request, 'Leave Appplication Has been sent')
        return redirect('studentapplication')
    pass


def student_view_attendance(request):
    student = Student.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(course=student.course)
    action = request.GET.get('action')

    subjects = None
    get_subject = None
    attendance_report =None
    if action is not None:
        if request.method == 'POST':
            subjects = request.POST.get('subject')
            get_subject = Subject.objects.get(id=subjects)

            attendance = Attendance.objects.filter(subject_id=get_subject)
            attendance_report = Attendance_report.objects.filter(student_id=student, Attendance__subject_id=subjects)
            
    context = {
        'subject': subject,
        'action': action,
        'get_subject': get_subject,
        'attendance_report': attendance_report
    }
    return render(request, 'student-attendance.html', context)


def result(request):
    student = Student.objects.get(admin = request.user.id)

    result = StudentResult.objects.filter(student_id = student)
    mark = None
    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark

        mark = assignment_mark + exam_mark

    context = {
        'result': result,
        'mark':mark
    }
    return render(request, 'result.html', context)