from django.shortcuts import render,redirect
from .models import Problem,Idea
from account.models import Student,ProblemCreator,User

def home(request):
    if request.method == 'POST':
        return render(request,f"{request.POST['email']}.html")
    return render(request,'home.html')


def problem(request):
    if request.method == "POST":
        title = request.POST["title"]
        code = request.POST["code"]
        cat = request.POST["cat"]
        org = request.POST["Organisation"]
        com = request.POST["complexity"]
        theme = request.POST["theme"]
        desc = request.POST["desc"]

        prob = Problem.objects.create(title=title,code=code,category=cat,desc=desc,theme=theme,complexity=com,org_type=org)

        return render(request,'is.html',{'error':'Your problem has been Successfully added.'})

    return render(request, 'problem.html')
    
def idea(request,pr):
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        doc = request.FILES["doc"]
        pr = request.POST["pr"]
        prob = Problem.objects.get(id=pr)

        idea = Idea.objects.create(user=Student.objects.get(user=request.user),title=title,doc=doc,desc=desc,problem=prob)

        error='Your idea has been successfully submitted.'
        return render(request,'is.html',{'error':error})
    prob = Problem.objects.get(id=pr)
    try:
        Idea.objects.get(problem=prob,user=Student.objects.get(user=request.user))
        error='You have already submitted idea on this problem.'
        return render(request,'is.html',{'error':error})
    except:
        return render(request,'idea.html',{'prob':prob})


def about(request):
    return render(request,'about.html')

def past(request):
    return render(request,'past.html')


def prdesc(request):
    probs = Problem.objects.all()
    if request.method == 'POST':
        probs = Problem.objects.all().filter(category=request.POST['category'],theme=request.POST['theme'])
    return render(request,'prdesc.html',{'probs':probs})

def profile(request):
    stu=Student.objects.get(user=request.user)
    ideas=Idea.objects.all().filter(user=stu)
    return render(request, "profile.html", {"stu": stu, "ideas": ideas})
    
def subidea(request):
    stu=Student.objects.get(user=request.user)
    ideas=Idea.objects.all().filter(user=stu)
    return render(request,"subidea.html",{"stu":stu,"ideas":ideas})

