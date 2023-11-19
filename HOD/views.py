from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from app.models import CustomUser
from django.contrib import messages
from Staff.models import *
from student.models import *
from rest_framework.renderers import JSONRenderer

# Create your views here.

@login_required
def HOD(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    # subject_count = sub.objects.all().count()
    course_count = Course.objects.all().count()


    student_count_male = Student.objects.filter(gender = 'male').count()
    student_count_female = Student.objects.filter(gender = 'female').count()

    print(student_count_female)
    print(student_count_male)

    context = {
        'student_count': student_count,
        'student_count_male': student_count_male,
        'student_count_female': student_count_female,
        'staff_count': staff_count,
        'course_count':course_count,
        
    }

    return render(request, 'HOD_HOME.html', context)

@login_required
def Add_Student(request):
    course = Course.objects.all()
    session = Session.objects.all()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        mobile_no = request.POST.get('mobile_no')
        course = request.POST.get('course')
        session = request.POST.get('session')
        img = request.FILES.get('img')
        password = request.POST.get('password')

        print(first_name,last_name, username, email,gender,mobile_no, course, session, img, password)
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is Already Taken')
            return redirect('Add_Student')
            
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is Already Taken')
            return redirect('Add_Student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic = img,
                user_type = 3
            )
            user.set_password(password)
            user.save()
            course = Course.objects.get(id=course)
            session = Session.objects.get(id=session)
            student = Student(admin=user, gender=gender, mobile_no=mobile_no, course=course, session=session)
            student.save()
            messages.success(request, user.first_name + ' ' + user.last_name + ' ' + ' Registered Sucessfully')
            return redirect('Add_Student')
        
        

    context = {
        "course": course,
        'session': session
    }
    return render(request, 'student/add_student.html', context)


@login_required
def View_Student(request):
    student = Student.objects.all()
    context = {
        'students':student
    }
    return render(request, 'student/view_student.html', context)

@login_required
def Edit_Student(request, id):
    student = Student.objects.get(id=id)
    course = Course.objects.all()
    session = Session.objects.all()


    context = {
        'student': student,
        "course": course,
        'session': session
    }
    return render(request, 'student/edit_student.html', context)

@login_required
def Update_Student(request):
    if request.method == 'POST':
        id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        mobile_no = request.POST.get('mobile_no')
        course = request.POST.get('course')
        session = request.POST.get('session')
        img = request.FILES.get('img')
        password = request.POST.get('password')


        user = CustomUser.objects.get(id = id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        
        if password !=None and password != "":
            user.set_password(password)

        if img !=None and img != "":
            user.profile_pic=img

        user.save()
        

        student = Student.objects.get(admin=id)
        student.gender = gender
        student.mobile_no = mobile_no
        course = Course.objects.get(id=course)
        student.course = course
        session = Session.objects.get(id=session)
        student.session = session
        student.save()
        # print(user.first_name, user.last_name, user.username, user.email, student.gender, student.mobile_no, student.course, student.session, user.profile_pic, user.password)
        
        messages.success(request, 'Data Successfully updated')
    return render(request, 'student/edit_student.html')


@login_required
def Del_Student(request, id):
    students = CustomUser.objects.get(id=id)
    students.delete()
    messages.success(request, 'Student Deleted Successfully')
    return redirect('View_Student')



@login_required
def Add_Course(request):
    if request.method == 'POST':
        courses = request.POST.get('Course_name')

        course = Course(
            name = courses
        )
        course.save()
        messages.success(request, 'Course Add Successfully')
        return redirect('Add_Course')
    return render(request, 'course/add_course.html')

@login_required
def View_Course(request):
    course = Course.objects.all()

    context = {
        'courses': course
    }
    return render(request, 'course/view_course.html', context)

@login_required
def Edit_Course(request, id):
    course = Course.objects.get(id=id)

    context = {
        'course': course
    }
    return render(request, 'course/edit_course.html', context)


@login_required
def Update_Course(request):
    if request.method == 'POST':
        course_id = request.POST.get('Course_id')
        course_name = request.POST.get('Course_name')

        course = Course.objects.get(id = course_id)

        course.name = course_name

        course.save()
        messages.success(request, "Course Updated Successfully")
    return render(request, 'course/edit_course.html')

@login_required
def Del_course(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request, 'course deleted')

    return redirect('View_course')




@login_required
def Add_Subject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        Subject_name = request.POST.get('Subject_name')
        course_name = request.POST.get('course_name')
        staff_id = request.POST.get('staff')

        courses = Course.objects.get(id = course_name)
        staffs = Staff.objects.get(admin = staff_id)
        subject = Subject(
            name= Subject_name,
            course = courses,
            staff= staffs
        )
        subject.save()
        messages.success(request, 'Subject Added Successfully..!!')

    context = {
        'course': course,
        'staff': staff
    }
    return render(request, 'subject/add_subject.html', context)


@login_required
def View_Subject(request):
    subject = Subject.objects.all()


    context = {
        'subjects': subject
    }
    return render(request, 'subject/view_subject.html', context)


@login_required
def Edit_Subject(request, id):
    subject = Subject.objects.get(id = id)
    staff = Staff.objects.all()
    course = Course.objects.all()

    context = {
        'subject': subject,
        'staff':staff,
        'course':course
    }
    return render(request, 'subject/edit_subject.html', context)


@login_required
def Update_Subject(request):
    if request.method == 'POST':
        Subject_name = request.POST.get('Subject_name')
        course_name = request.POST.get('course_name')
        staff_id = request.POST.get('staff')
        subject_id = request.POST.get('subject_id')

        courses = Course.objects.get(id = course_name)
        staffs = Staff.objects.get(admin = staff_id)

        subject = Subject.objects.get(id=subject_id)
        subject.name = Subject_name
        subject.course = courses
        subject.staff = staffs
        subject.save()
        messages.success(request, 'Subject Updated Successfully...!!')
    
    return redirect('View_Subject')


@login_required
def Del_Subject(request, id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    return redirect('View_Subject')

@login_required
def Add_Staff(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        course_id  = request.POST.get('course')
        mobile_no = request.POST.get('mobile_no')
        profile_pic = request.FILES.get('profile_pic')
        password = request.POST['password']

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is Already Taken')
            return redirect('Add_Student')
            
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is Already Taken')
            return redirect('Add_Student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic = profile_pic,
                user_type = 2
            )
            user.set_password(password)

            user.save()
            course = Course.objects.get(id=course_id)
            staff = Staff(
                admin = user,
                gender = gender,
                mobile_no = mobile_no,
                course=course,
            )

            staff.save()
            messages.success(request, user.first_name + ' ' + user.last_name + ' ' + ' Registered Sucessfully')
            return redirect('Add_Staff')
    context = {
        'courses': courses
    }
    return render(request, 'staff/add_staff.html', context)


@login_required
def View_Staff(request):
    staff = Staff.objects.all()

    context = {
        'staffs': staff
    }
    return render(request, 'staff/view_staff.html', context)


@login_required
def Edit_Staff(request, id):
    staff = Staff.objects.get(id=id)

    return render(request, 'staff/edit_staff.html', {'staff':staff})


@login_required
def Update_Staff(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        mobile_no = request.POST.get('mobile_no')
        profile_pic = request.FILES.get('profile_pic')
        password = request.POST['password']



        user = CustomUser.objects.get(id = staff_id)

        user.first_name = first_name,
        user.last_name = last_name,
        user.username = username,
        user.email = email,
        user.profile_pic = profile_pic

        if password !=None and password != '':
            user.set_password(password)

        if profile_pic !=None and profile_pic != '':
            user.profile_pic = profile_pic

        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender,
        staff.mobile_no = mobile_no,

        staff.save()
        messages.success(request, 'Data Updated Successfully')


    return render(request, 'staff/edit_staff.html')



@login_required
def Del_Staff(request, id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    messages.success(request, 'Staff Deleted')
    return redirect('View_Staff')


@login_required
def add_session(request):
    if request.method == 'POST':
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        session = Session(session_start=session_start, session_end=session_end)
        session.save()
        messages.success(request, 'Session Added')
        return redirect('add_session')
    return render(request, 'session/add_session.html')


@login_required
def view_session(request):
    session = Session.objects.all()


    context = {
        'session': session
    }
    return render(request, 'session/view_session.html', context)


@login_required
def edit_session(request, id):
    session = Session.objects.get(id= id)
    

    context = {
        'session': session
    }
    return render(request, 'session/edit_session.html', context)


@login_required
def update_session(request):
    if request.method == 'POST':
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        session_id = request.POST.get('session_id')

        session = Session.objects.get(id = session_id)
        session.session_start = session_start
        session.session_end = session_end
        session.save()
        
        return redirect('view_session')

@login_required
def del_session(request, id):
    session = Session.objects.get(id= id)
    session.delete()
    return redirect('view_session')





@login_required
def staff_leave_application_view(request):
    staff_leave = Staff_leave.objects.all()

    context = {
        'staff_leave': staff_leave
    }
    return render(request, 'staff/staff_leave_view.html', context)

@login_required
def staff_leave_application_approved(request, id):
    leave = Staff_leave.objects.get(id= id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_application_view')

@login_required
def staff_leave_application_disapproved(request, id):
    leave = Staff_leave.objects.get(id= id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_application_view')


def student_leave_view(request):
    student_leave = Student_leave.objects.all()

    context = {
        'student_leave': student_leave
    }
    return render(request, 'student/student_leave_view.html', context)


def student_leave_application_approved(request, id):
    leave = Student_leave.objects.get(id= id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')

def student_leave_application_disapproved(request, id):
    leave = Student_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')


def view_student_attendance(request):
    
    subject = Subject.objects.all()
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
    return render(request, 'student/viewstudentattendance.html', context)