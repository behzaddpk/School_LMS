from django.db import models
from HOD.models import *
# Create your models here.


class Student_leave(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    message = models.TextField(max_length=255)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.student_id.admin.first_name + self.student_id.admin.last_name
    

class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.DO_NOTHING)
    date = models.DateField()
    session = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__ (self):
        return self.subject_id.name
    
class Attendance_report(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    Attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__ (self):
        return self.student_id.admin.first_name + self.student_id.admin.last_name
    


class StudentResult(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignment_mark = models.IntegerField()
    exam_mark = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__ (self):
        return self.student_id.admin.first_name + self.student_id.admin.last_name
    
