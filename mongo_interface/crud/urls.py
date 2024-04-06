from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.create_student, name='create_student'),
    path('update/<str:student_id>/', views.update_student, name='update_student'),
    path('delete/<str:student_id>/', views.delete_student, name='delete_student'),
]