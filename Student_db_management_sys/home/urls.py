from django.urls import path 
from . import views 
urlpatterns = [
    path("",views.sign),
    path("sign_in",views.sign_in),
    path("sign_up",views.sign_up),
    path("dashboard",views.dashboard),
    path("course",views.course),
    path("add_course",views.add_course),
    path("students",views.students),
    path("lgout",views.lgout),
    path("add_student",views.add_student),
    path("delete_std",views.delete_std),
    path("update_student",views.update_student),
    path("update_course",views.update_course),
    path("delete_course",views.delete_course),
    path("search",views.search),
    path("search_course",views.search_course),
    path("teacher",views.teacher),
    path("update_teacher",views.update_teacher),
    path("delete_teacher",views.delete_teacher),
    path("update_teacher_page/<int:uid>/",views.update_teacher_page),
    path("update_student_page/<int:uid>/",views.update_student_page),
    path("update_course_page/<int:uid>/",views.update_course_page)
]
