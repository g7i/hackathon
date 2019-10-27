from django.shortcuts import render,redirect
from .models import Problem,Idea
from account.models import Student, ProblemCreator, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        discipline = request.POST["discipline"]
        link = request.POST["link"]
        outcome = request.POST["outcome"]

        prob = Problem.objects.create(title=title,code=code,category=cat,desc=desc,theme=theme,complexity=com,org_type=org)

        if discipline:
            prob.discipline = discipline
        if link:
            prob.link = link
        if outcome:
            prob.outcome = outcome
        prob.save()

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
    return render(request, 'about.html')
    
def downloads(request):
    return render(request, 'downloads.html')
    
def faq(request):
    return render(request,'faq.html')

def past(request):
    return render(request,'past.html')


def prdesc(request):
    probs = Problem.objects.all().order_by('code')
    ideas = Idea.objects.all()
    idea = []
    if request.method == 'POST':
        category = request.POST['category']
        code = request.POST['code']
        theme = request.POST['theme']
        probs = Problem.objects.all()
        if category:
            probs = probs.filter(category=category)
        if code:
            probs = probs.filter(code=code)
        if theme:
            probs = probs.filter(theme=theme)
    for prob in probs:
        idea.append(len(ideas.filter(problem=prob)))
    zprobs = list(zip(probs, idea))

    if request.method == 'POST':
        val = ({
            'category': category,
            'code': code,
            'theme': theme,
            'probs': zprobs,
            'post':True
        })
        return render(request,'prdesc.html',context=val)

    page = request.GET.get('page', 1)

    paginator = Paginator(zprobs, 15)
    try:
        probs = paginator.page(page)
    except PageNotAnInteger:
        probs = paginator.page(1)
    except EmptyPage:
        probs = paginator.page(paginator.num_pages)

    return render(request,'prdesc.html',{'probs':probs})

def profile(request):
    stu=Student.objects.get(user=request.user)
    return render(request, "profile.html", {"stu": stu})
    
def subidea(request):
    stu=Student.objects.get(user=request.user)
    ideas=Idea.objects.all().filter(user=stu)
    return render(request,"subidea.html",{"stu":stu,"ideas":ideas})

