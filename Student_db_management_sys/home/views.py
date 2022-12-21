from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.contrib import auth
from django.db.models import Q
from . models import User,Course,Student,Teacher
def sign(request):
    return render(request,'sign_in.html')
def sign_in(request):
    Name=request.POST['name']
    Pass=request.POST['password']
    if User.objects.filter(Name=Name).exists():
        user=User.objects.get(Name=Name)
        Password=user.Password
        if check_password(Pass,Password):
            messages.success(request,"Login Successful")
            data=Course.objects.all()
            x=Course.objects.all().count()
            y=Student.objects.all().count()
            return render(request,'dashboard.html',{'data':data,'x':x,'y':y})
        else:
            messages.info(request,'Password Incorrect')
            return render(request,'sign_in.html')
    else:
        x=Course.objects.all().count()
        y=Student.objects.all().count()
        return render(request,'sign_in.html',{'x':x,'y':y})
def sign_up(request):
    if request.method=="POST":
        Name=request.POST['name']
        Email=request.POST['email']
        Password=make_password(request.POST['password'])
        if User.objects.filter(Name=Name).exists():
            messages.info(request,'Username already exists')
            return render(request,"sign_up.html")
        elif User.objects.filter(Email=Email).exists():
            messages.info(request,'Email already exists')
            return render(request,"sign_up.html")
        else:
            User.objects.create(Name=Name,
                                    Email=Email,
                                    Password=Password)
            messages.success(request,'!!!!Successfully registered!!!!')
            return render(request,'sign_in.html')
    else:
        return render(request,'sign_up.html')

def dashboard (request):
    data=Course.objects.all()
    x=Course.objects.all().count()
    y=Student.objects.all().count()
    z=Teacher.objects.all().count()
    return render(request,'dashboard.html',{'data':data,'x':x,'y':y,'z':z})


def course (request):
    data=Course.objects.all()
    return render(request,'course.html',{'data':data})

def students (request):
    s_data=Student.objects.all()
    data=Course.objects.all()
    return render(request,'viewstudents.html',{'s_data':s_data,"data":data})

def lgout(request):
    auth.logout(request)
    return render(request,'sign_in.html')


def add_course(request):
    Name=request.POST['name']
    Fees=request.POST['fees']
    Fees=int(Fees)
    Duration=request.POST['duration']
    TextField=request.POST['area']
    if Course.objects.filter(Name=Name).exists():
        messages.info(request,'Course already exists')
        return render(request,"course.html")
    else:
        Course.objects.create(Name=Name,
                                Fees=Fees,
                                TextField=TextField,
                                Duration=Duration)
        messages.success(request,'!!!!Successfully Added!!!!')
        data=Course.objects.all()
        return render(request,'course.html',{'data':data})

def add_student(request):
    s=Student()
    s.Name=request.POST['name']
    s.Email=request.POST['email']
    s.Contact=request.POST['contact']
    s.College=request.POST['college']
    s.Degree=request.POST['degree']
    s.Total=request.POST['total']
    s.Paid=request.POST['paid']
    s.Due=request.POST['due']
    s.course=Course.objects.get(id=(request.POST['course']))
    s.save()
    data=Course.objects.all()
    s_data=Student.objects.all()
    return render(request,'viewstudents.html',{'s_data':s_data,'data':data})
def delete_std(request):
    sid=request.GET['sid']
    Student.objects.get(id=sid).delete()
    data=Course.objects.all()
    s_data=Student.objects.all()
    return render(request,'viewstudents.html',{'s_data':s_data,'data':data})
def update_student(request):
    s=Student()
    s.id=request.POST['uid']
    s.Name=request.POST['name']
    s.Email=request.POST['email']
    s.Contact=request.POST['contact']
    s.College=request.POST['college']
    s.Degree=request.POST['degree']
    s.Total=request.POST['total']
    s.Paid=request.POST['paid']
    s.Due=request.POST['due']
    cid=request.POST['course']
    s.course=Course.objects.get(id=cid)
    s.save()
    data=Course.objects.all()
    s_data=Student.objects.all()
    return render(request,'viewstudents.html',{'data':data,'s_data':s_data})
def update_course(request):
    c=Course()
    c.id=request.POST['uid']
    c.Name=request.POST['name']
    c.Fees=request.POST['fees']
    c.Fees=int(c.Fees)
    c.Duration=request.POST['duration']
    c.TextField=request.POST['area']
    c.save()
    data=Course.objects.all()
    s_data=Student.objects.all()
    return render(request,'course.html',{'data':data,'s_data':s_data})
def delete_course(request):
    cid=request.GET['cid']
    Course.objects.get(id=cid).delete()
    data=Course.objects.all()
    s_data=Student.objects.all()
    return render(request,'course.html',{'s_data':s_data,'data':data})
def search(request):
    find=request.POST['find']
    s=Student.objects.filter(Q(Email=find) | Q(Name=find) | Q(College=find) | Q(Degree=find)).all()
    return render(request,'viewstudents.html',{'s_data':s})
def search_course(request):
    find=request.POST['find']
    s=Course.objects.filter(Q(Name=find) | Q(Duration=find) | Q(TextField=find)).all()
    return render(request,'course.html',{'data':s})
def teacher(request):
    if request.method=="POST":
        Name=request.POST['name']
        Email=request.POST['email']
        Contact=request.POST['contact']
        Joining_dt=request.POST['date']
        Education=request.POST['education']
        Employee_id=request.POST['emp_id']
        Work_exp=request.POST['work_exp']
        Package=request.POST['package']
        if Teacher.objects.filter(Email=Email).exists():
            messages.info(request,'Email already exists')
            teachers=Teacher.objects.all()
            return render(request,'teacher.html',{'teachers':teachers})
        elif Teacher.objects.filter(Employee_id=Employee_id).exists():
            messages.info(request,'Employee id already exists')
            teachers=Teacher.objects.all()
            return render(request,'teacher.html',{'teachers':teachers})
        elif Teacher.objects.filter(Contact=Contact).exists():
            messages.info(request,'Phone no. already registered')
            teachers=Teacher.objects.all()
            return render(request,'teacher.html',{'teachers':teachers})
        else:
            Teacher.objects.create(Name=Name,
                                    Email=Email,
                                    Contact=Contact,
                                    Joining_dt=Joining_dt,
                                    Education=Education,
                                    Employee_id=Employee_id,

                                    Work_exp=Work_exp,
                                    Package=Package)
            messages.success(request,'!!!!Successfully registered!!!!')
            teachers=Teacher.objects.all()
            return render(request,'teacher.html',{'teachers':teachers})
    else:
        teachers=Teacher.objects.all()
        return render(request,'teacher.html',{'teachers':teachers})

def update_teacher(request):
    t=Teacher()
    t.id=request.POST['uid']
    t.Name=request.POST['name']
    t.Email=request.POST['email']
    t.Contact=request.POST['contact']
    t.Joining_dt=request.POST['date']
    t.Education=request.POST['education']
    t.Employee_id=request.POST['emp_id']
    t.Work_exp=request.POST['work_exp']
    t.Package=request.POST['package']
    t.save()
    teachers=Teacher.objects.all()
    return render(request,'teacher.html',{'teachers':teachers})

def delete_teacher(request):
    did=request.GET['did']
    Teacher.objects.get(id=did).delete()
    teachers=Teacher.objects.all()
    return render(request,'teacher.html',{'teachers':teachers})

    

def update_teacher_page(request,uid):
    res = Teacher.objects.get(id=uid)
    return render(request, 'update_teacher.html', context={
        'stu': res,
    })

def update_student_page(request,uid):
    res = Student.objects.get(id=uid)
    data=Course.objects.all()
    return render(request, 'update_students.html', context={
        'stu': res,
        'data':data
    })
    

def update_course_page(request,uid):
    res = Course.objects.get(id=uid)
    return render(request, 'update_course.html', context={
        'stu': res,
    })





# Create your views here.
