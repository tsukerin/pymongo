from django.shortcuts import render, redirect
from pymongo import MongoClient
from .models import Student

def student_list(request):
    students = Student.read_all()
    return render(request, 'student_list.html', {'students': students})

def create_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        faculty = request.POST['faculty']
        Student.create(name, faculty)
        return redirect('student_list')
    return render(request, 'create_student.html')

def update_student(request, student_id):
    student = Student.read_one(student_id)
    if request.method == 'POST':
        name = request.POST['name']
        faculty = request.POST['faculty']
        Student.update(student_id, name, faculty)
        return redirect('student_list')
    return render(request, 'update_student.html', {'student': student})

def delete_student(request, student_id):
    Student.delete(student_id)
    return redirect('student_list')
