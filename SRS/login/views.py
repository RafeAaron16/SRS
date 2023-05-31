from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def login(request):
        return render(request, 'login.html')

def home(request):
        return HttpResponse("<p>Welcome new Student. <a href='login'>Go to the login page</a></p>")

def signup(request):
        return render(request, 'signup.html')

def verification(request):
        user = request.POST['Username']
        pas = request.POST['Password']

        sdt = Student.objects.filter(usr=user)

        if not sdt:
                return HttpResponse("No record with that Username exists")
        else:
                if sdt[0].password != pas:
                        return HttpResponse("Incorrect password for record")

        return HttpResponse(user + " " + pas + " <a href='main'>Go to main page</a>")

def verifynew(request):
        fname = request.POST['Fname']
        lname = request.POST['Lname']
        user = request.POST['Username']
        eml = request.POST['Email']
        pas = request.POST['Password']
        cpas = request.POST['Confirm Password']

        if pas != cpas:
                return HttpResponse("Passwords don't match")

        sdt = Student.objects.filter(email = eml)
        sdt1 = Student.objects.filter(usr = user)

        if sdt:
                return HttpResponse("That email is already taken")

        if sdt1:
                return HttpResponse("That username is already taken")

        student = Student(Fname=fname, Lname=lname, usr = user, email = eml, password = pas )
        student.save()

        return HttpResponse("Successful <a href='login'>Login</a>")

def main(request):
        return HttpResponse("Welcome to main we shall update this soon <a href='login'>Log out</a>")
