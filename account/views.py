from django.shortcuts import render,redirect
from .models import Student,Mentor,Judge,ProblemCreator,User
from django.contrib import auth
from django.http import JsonResponse
import csv,os
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings


def signups(request):
    if request.method == 'POST':
        adhar = request.POST['aadhar']
        if adhar == '':
                return render(request, 'signups.html', {'error': "You haven't verified you Aadhar Number. Please Verify it before SignUp."})
        try:
            stu = Student.objects.get(aadhar=adhar)
            return render(request, 'signups.html', {'error': "Don't try to be oversmart. You already have an account with this Adhar No."})
        except:
            pass
        username = request.POST["Username"]
        password = request.POST["Password"]
        confirmpass = request.POST["Confirm Password"]
        email = request.POST["E-mail"]
        fathername = request.POST["Father's Name"]
        firstname = request.POST["First Name"]
        lastname = request.POST["Last Name"]
        contact = request.POST["Contact Number"]
        branch = request.POST["Branch"]
        sem = request.POST["Semester"]
        clgid = request.POST["Collage ID"]
        files = request.FILES["myFile"]

        if password==confirmpass:
            try:
                user = User.objects.get(username=username)

                return render(request, 'signups.html',{'error':'User already exists.'})

            except User.DoesNotExist:
                user=User.objects.create_user(username =username,password=password,email=email,first_name=firstname,last_name=lastname,user_type='S')
                user = auth.authenticate(username=username,password=password)
                stu=Student.objects.create(user=user,father_name=fathername,college_id=clgid,semester=sem,contact_number=contact,branch=branch,letter=files,aadhar=adhar)
                auth.login(request, user)
                return redirect('home')

        else:
            return render(request, 'signups.html',{'error':'Password didn\'t match.'})

        return redirect("home")
       

    return render(request,'signups.html')




def signupm(request):
    if request.method == 'POST':
        username = request.POST["Username"]
        password = request.POST["Password"]
        confirmpass = request.POST["Confirm Password"]
        email = request.POST["E-mail"]
        fathername = request.POST["Father's Name"]
        firstname = request.POST["First Name"]
        lastname = request.POST["Last Name"]
        designation = request.POST["Designation"]
        aadhar = request.POST["Adhar Card Number"]
        teaching_exp = request.POST["Teaching Experience"]
        indust_exp = request.POST["Industrial Experience"]
        contact = request.POST["Contact Number"]
        deptt = request.POST["Department"]
        address = request.POST["Address"]
        qual = request.POST["Qualification"]

        if password==confirmpass:
            try:
                user = User.objects.get(username=username)

                return render(request, 'signupm.html',{'error':'User already exists.'})

            except User.DoesNotExist:
                user=User.objects.create_user(username =username,password=password,email=email,first_name=firstname,last_name=lastname,user_type='M')
                mentor = Mentor.objects.create(user=user, father_name=fathername, contact_number=contact, department=deptt, qualification=qual, designation=designation, aadhar=aadhar, teaching_exp=teaching_exp, industrial_exp=indust_exp, address=address)
                user = auth.authenticate(username=username,password=password)
                auth.login(request, user)
                return redirect('home')

        else:
            return render(request, 'signupm.html',{'error':'Password didn\'t match.'})

        return redirect("home")
       

    return render(request,'signupm.html')


def signupj(request):
    if request.method == 'POST':
        username = request.POST["Username"]
        password = request.POST["Password"]
        confirmpass = request.POST["Confirm Password"]
        email = request.POST["E-mail"]
        fathername = request.POST["Father's Name"]
        firstname = request.POST["First Name"]
        lastname = request.POST["Last Name"]
        designation = request.POST["Designation"]
        aadhar = request.POST["Adhar Card Number"]
        teaching_exp = request.POST["Teaching Experience"]
        indust_exp = request.POST["Industrial Experience"]
        contact = request.POST["Contact Number"]
        deptt = request.POST["Department"]
        address = request.POST["Address"]
        qual = request.POST["Qualification"]

        if password==confirmpass:
            try:
                user = User.objects.get(username=username)

                return render(request, 'signupj.html',{'error':'User already exists.'})

            except User.DoesNotExist:
                user=User.objects.create_user(username =username,password=password,email=email,first_name=firstname,last_name=lastname,user_type='J')
                judge = Judge.objects.create(user=user, father_name=fathername, contact_number=contact, department=deptt, qualification=qual, designation=designation, aadhar=aadhar, teaching_exp=teaching_exp, industrial_exp=indust_exp, address=address)
                user = auth.authenticate(username=username,password=password)
                auth.login(request, user)
                return redirect('home')

        else:
            return render(request, 'signupj.html',{'error':'Password didn\'t match.'})

        return redirect("home")
       

    return render(request,'signupj.html')


def signupp(request):
    if request.method == 'POST':
        username = request.POST["Username"]
        password = request.POST["Password"]
        confirmpass = request.POST["Confirm Password"]
        email = request.POST["E-mail"]
        firstname = request.POST["First Name"]
        lastname = request.POST["Last Name"]
        designation = request.POST["Designation"]
        contact = request.POST["Contact Number"]
        org = request.POST["Organisation"]
        address = request.POST["Address"]

        if password==confirmpass:
            try:
                user = User.objects.get(username=username)

                return render(request, 'signupp.html',{'error':'Username already exists.'})

            except User.DoesNotExist:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname,user_type='P')
                pc = ProblemCreator.objects.create(user=user, contact_number=contact, designation=designation, organisation=org,address=address)
                user = auth.authenticate(username=username,password=password)
                auth.login(request, user)
                return redirect('home')

        else:
            return render(request, 'signupp.html',{'error':'Password didn\'t match.'})

        return redirect("home")
    return render(request,'signupp.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect(request.POST.get('next','home'))
        else:
            try:
                username = User.objects.get(email=request.POST['username']).username
                user = auth.authenticate(username=username, password=request.POST['password'])
            except:
                pass
            if user is not None:
                auth.login(request,user)
                return redirect(request.POST.get('next','home'))
            else:
                return render(request,'login.html',{'error':'Invalid Credentials...'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def aadhar(request):
    if request.method == 'POST':
        path = os.path.join(settings.STATIC_ROOT,'verification.csv')
        aadhar = request.POST['aadhar']
        reader = csv.DictReader(open(path))
        response_data = {'Message':"Sorry you've not registered your Aadhar No. Please try next year.",'Status':'N'}
        for raw in reader:
            if aadhar == raw['Aadhar Number']:
                response_data = {'Message':'Your Aadhar No. has been verified. Fill the Form to SignUp.','email':raw['Username'],'Status':'Y'}
        return JsonResponse(response_data)