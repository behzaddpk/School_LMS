from django.shortcuts import render, redirect
from HOD.models import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student.models import *

# Create your views here.

@login_required
def Staff_Home(request):
    return render(request, 'staff_home.html')


@login_required
def Notification(request):
    staff =  Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        notification = Staff_Notification.objects.filter(staff_id=staff_id)


        context = {
            'notification':notification
        }
    return render(request, 'notification.html', context)


@login_required
def Mark_Notification(request, status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('Notification')

@login_required
def Staff_Apply_Leave(request):
    user = request.user
    staff = Staff.objects.filter(admin = user)
    for i in staff:
        
        staff_id = i.id

        staff_leave_history = Staff_leave.objects.filter(staff_id = staff_id)


    context = {
        'staff_leave_history': staff_leave_history
    }
    return render(request, 'staff_leave.html', context)


@login_required
def Apply_Leave_save(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff_id = Staff.objects.get(admin = request.user.id)

        leave = Staff_leave(
            staff_id = staff_id,
            date = leave_date,
            message = leave_message
        ) 
        leave.save()
        messages.success(request, 'Leave Appplication Has been sent')
        return redirect('Staff_leave')
    pass


@login_required
def StaffFeedback(request):
    staff_id = Staff.objects.get(admin = request.user.id)

    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)
    context = {
        'feedback_history':feedback_history
    }
    return render(request, 'staff_feedback.html', context)


@login_required
def feedback_save(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        staff_id = Staff.objects.get(admin = request.user.id)

        feedback = Staff_Feedback(
            staff_id = staff_id,
            feedback = feedback
        )
        feedback.save()
        messages.success(request, 'Your Feedback Has been Sent')
        return redirect('StaffFeedback')
    

def take_attendance(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(staff = staff_id)
    sessions = Session.objects.all()
    action = request.GET.get('action')
    students = None
    get_subject = None
    get_session = None
    if action is not None:
        if request.method == 'POST':
            subject = request.POST.get('subject')
            session = request.POST.get('session')
            get_subject = Subject.objects.get(id = subject)
            get_session = Session.objects.get(id= session)

            subject_stud = Subject.objects.filter(id = subject)
            for i in subject_stud:
                student_id = i.course.id
                students = Student.objects.filter(course = student_id)

    context = {
        'subjects': subjects,
        'sessions': sessions,
        'get_subject': get_subject,
        'get_session': get_session,
        'students': students,
        'action': action,
    }
    return render(request, 'take-attendance.html', context)

def attendance(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        session = request.POST.get('session')
        date = request.POST.get('attendance_date')
        students = request.POST.get('students')
    
        get_subject = Subject.objects.get(id=subject)
        get_session = Session.objects.get(id=session)
        
        attendance = Attendance(
            subject_id = get_subject,
            date = date,
            session = get_session
        )
        attendance.save()
        
        for i in students:
            stud_id = 1
            int_stud = int(stud_id)

            p_students = Student.objects.get(id = int_stud)
            attendance_report = Attendance_report(
                student_id = p_students,
                Attendance = attendance,
            )
            attendance_report.save()

            return redirect('take-attendance')


@login_required
def view_attendance(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff_id=staff_id)
    session = Session.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None 
    attendance_report = None
    date = None
    if action is not None:
        if request.method == 'POST':
            subject = request.POST.get('subject')
            session = request.POST.get('session')
            date =  request.POST.get('attendance_date')


            get_subject = Subject.objects.get(id=subject)
            get_session = Session.objects.get(id=session)

            attendance = Attendance.objects.filter(subject_id = get_subject, date=date)
            for i in attendance:
                attendance_id = i.id 
                attendance_report = Attendance_report.objects.filter(Attendance=attendance_id)
    context = {
        'subject': subject,
        'session': session,
        'action': action,
        'get_subject': get_subject,
        'get_session': get_session, 
        'date': date,
        'attendance_report': attendance_report
    }

    return render(request, 'view_atteandance.html', context)


@login_required
def add_result(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff_id=staff_id)
    session = Session.objects.all()
    action = request.GET.get('action')
    get_session = None
    get_subject = None
    students = None
    if action is not None:
        if request.method == 'POST':
            subject = request.POST.get('subject')
            session = request.POST.get('session')


            get_subject = Subject.objects.get(id=subject)
            get_session = Session.objects.get(id=session)
            print(get_subject)
            subject_stud = Subject.objects.filter(id = subject)
            for i in subject_stud:
                student_id = i.course.id
                students = Student.objects.filter(course = student_id)

    context = {
        'subject':subject,
        'sessions': session,
        'action': action,
        'get_subject': get_subject,
        'get_session': get_session,
        'students': students
    }
    return render(request, 'add_result.html', context)


def save_result(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        student_id = request.POST.get('student_id')
        session_id = request.POST.get('session')
        assignment_marks = request.POST.get('assignment_marks')
        exam_marks = request.POST.get('exam_marks')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exists = StudentResult.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        if check_exists:
            result = StudentResult.objects.get(subject_id=get_subject, student_id=get_student)
            result.assignment_mark=assignment_marks
            result.exam_mark=exam_marks
            result.save()
            messages.success(request, 'Result Added')
            return redirect('add_result')
        else:
            result = StudentResult(
                student_id=get_student,
                subject_id=get_subject,
                exam_mark = exam_marks,
                assignment_mark = assignment_marks
            )
            result.save()
            messages.success(request, 'Result are Added')
            return redirect('add_result')




