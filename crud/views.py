from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import StudentForm
from . models import Student

# Create your views here.
def studentAdd(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()    
        return HttpResponseRedirect('/')
    return render(request , 'crud/studentAdd.html' , {'form':form})

def show(request):
    student = Student.objects.all()  
    return render(request , 'crud/show.html' , {'student':student} )


def update(request , id):
    student = Student.objects.get(id=id) 
    form = StudentForm(request.POST , instance=student)
    if form.is_valid():
        form.save() 
        return HttpResponseRedirect('/')
    return render(request , 'crud/update.html' , {'student':student} )


def delete(request , id):
    form = Student.objects.get(id = id)
    form.delete()
    return HttpResponseRedirect('/')
