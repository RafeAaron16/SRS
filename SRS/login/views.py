from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def login(request):
        return render(request, 'login.html')

def home(request):
        return HttpResponse("<p>Welcome new Student. <a href='login'>Go to the login page</a></p>")

def signup(request):
        return render(request, 'signup.html')

@csrf_exempt
def verification(request):
        if 'Username' not in request.POST or 'Password' not in request.POST:
                return HttpResponse("104")

        user = request.POST['Username']
        pas = request.POST['Password']

        sdt = Student.objects.filter(usr=user)

        if not sdt:
                return HttpResponse("101")
        else:
                if sdt[0].password != pas:
                        return HttpResponse("102")

        return HttpResponse("100")

@csrf_exempt
def verifynew(request):
        if 'Username' not in request.POST or 'Password' not in request.POST or 'Email' not in request.POST or 'Lname' not in request.POST or 'Fname' not in request.POST or 'Confirm Password' not in request.POST:
                return HttpResponse("104")


        fname = request.POST['Fname']
        lname = request.POST['Lname']
        user = request.POST['Username']
        eml = request.POST['Email']
        pas = request.POST['Password']
        cpas = request.POST['Confirm Password']

        if pas != cpas:
                return HttpResponse("101")

        sdt = Student.objects.filter(email = eml)
        sdt1 = Student.objects.filter(usr = user)

        if sdt:
                return HttpResponse("102")

        if sdt1:
                return HttpResponse("103")

        student = Student(Fname=fname, Lname=lname, usr = user, email = eml, password = pas )
        student.save()

        return HttpResponse("100")

def main(request):
        return HttpResponse("Welcome to main we shall update this soon <a href='login'>Log out</a>")
