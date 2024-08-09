from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Blog, Internship, Project_details, Category
import datetime, time

# Create your views here.
date =  datetime.datetime.now()
h = int(date.strftime('%H'))
msg = "Good "
if h < 12 :
    msg += "Morning"
elif h < 16 :
    msg += "Afternoon"
elif h < 21:
    msg += "Evening"
else:
    msg = "Good Night"
my_dict = {"insert_date": date, "insert_msg": msg}

def greeting(request):
    return render(request,'basic.html', context=my_dict)

def home(request):
    return render(request, 'home.html', context=my_dict)
def handleblog(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to access this page")
        return redirect('/auth/login/')
    posts=Blog.objects.all()
    context={"posts":posts, "insert_date":date, "insert_msg": msg}
    return render(request, 'blog.html', context)

def blog_details(request,pk):
    posts = Blog.objects.get(id=pk)
    context = {"posts": posts, "insert_date":date, "insert_msg": msg}
    return render(request, "service-details.html", context)

def about(request):
    return render(request, 'about.html', context=my_dict)

def internshipdetails(request):
    
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to access this page")
        return redirect('/auth/login/')
    
    if request.method=="POST":
        fname=request.POST.get('name')
        email=request.POST.get('email')
        usn=request.POST.get('usn')
        college=request.POST.get('cname')
        offer=request.POST.get('offer')
        startdate=request.POST.get('startdate')
        enddate=request.POST.get('enddate')
        projreport=request.POST.get('projreport')

# converting to upper case

        fname=fname.upper()
        usn=usn.upper()
        college=college.upper()
        projreport=projreport.upper()
        offer=offer.upper()
        
# 
        check1=Internship.objects.filter(usn=usn)
        check2=Internship.objects.filter(email=email)
        
        if check1 or check2:
            messages.warning(request, "USN or Email Already Exists")
            
            return redirect(to="/internshipdetails")
        
        query=Internship(fullname=fname, usn=usn, email=email,college_name=college,offer_status=offer,start_date=startdate,end_date=enddate,proj_report=projreport)
        query.save()
        messages.success(request, "Form is Submitted Successfully ✔")
        return redirect('/internshipdetails')
        
    return render(request, 'intern.html', context=my_dict)

def contact(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to access this page")
        return redirect('/auth/login/')
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        desc=request.POST.get('desc')
        query= Contact(name=name, email=email, phonenumber=phoneno, description=desc)
        query.save()
        messages.success(request, "Message sent ✔.  Thanks for contacting us ")
        return redirect('/contact')
                
    return render(request, 'contact.html', context=my_dict)

def service(request):
    return render(request, 'home.html', context=my_dict)

def portfolio_cat(request, foo):
    foo = foo.replace('-', '')
    try:
        category = Category.objects.get(name=foo)
        proj_filter = Project_details.objects.filter(proj_category=category)
        context = {"projects": proj_filter, "category":category, "insert_date":date, "insert_msg": msg}
        return render(request, 'portfolio.html', context)
    except:
        messages.success(request, ("That category does not exist!!!"))
        return redirect('/portfolio')
        
def portfolio(request):
    projects = Project_details.objects.all()
    context = {"projects": projects, "insert_date":date, "insert_msg": msg}
    return render(request, "portfolio.html", context)


def portfolio_details(request, pk):
    proj_det = Project_details.objects.get(id=pk)
    context = {"proj_det": proj_det, "insert_date":date, "insert_msg": msg}
    return render(request, "portfolio-details.html", context)

