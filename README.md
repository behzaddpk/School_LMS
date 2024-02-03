# School Learning Management System

---


### HOD Dashboard
First HOD will signup for a account. (username: hod@gmail.com, password: hod)
After login they can see how many student/teacher wants to get job/admission in their school.
HOD can approve or delete/cancel the request.
HOD can add Teacher/Student.
HOD can update any student/teacher details.
HOD can accept/reject Student/teacher Leave Application.
HOD can View student's attendance.
HOD can announce notice also.


## Functions
### Teacher
After account approval by admin, teacher can take attendance of any class and view their attendance later.
Teacher can also publish/announce notice to student like submission of assignments.
Teacher add and view students attendance.



## Student
First student will take admission/signup.
When their account is approved by admin, only then the student can access their dashboard.
After account approval by admin the student can view their details like attendance.
Student can't view attendance of other student.
Students Can view their own Video lecture
Student can't announce, they can only view.




- Anyone can become Admin

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :

``` python -m pip install -r requirements.txt ```


- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```





