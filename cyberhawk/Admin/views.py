from django.shortcuts import render,redirect

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from website.models import *

@csrf_exempt
def home(request):
    return render(request,"Admin/home.html",{})

@csrf_exempt
def statastics(request):
    return render(request,"Admin/statastics.html",{})

@csrf_exempt
def viewmanager(request):
    students = registrationtable.objects.filter(user_type=2)
    return render(request, "Admin/viewmanagers.html", {'students': students})
@csrf_exempt
def viewstaff(request):
    students = registrationtable.objects.filter(user_type=3)
    return render(request, "Admin/viewstaff.html", {'students': students})

@csrf_exempt
def viewusers(request):
    students = registrationtable.objects.filter(user_type=4)
    return render(request, "Admin/viewusers.html", {'students': students})

@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('username')
            mobile_no = request.POST.get('userphone')
            email = request.POST.get('useremail')
            district = request.POST.get('userdistrict')
            address =request.POST.get('useraddress')

            user_type = request.POST.get('usertype')
            password = request.POST.get('userpassword')
            # Create and save the Teacher instance
            teacher = registrationtable.objects.create(
             name=name,
             mobile_no=mobile_no,
             email=email,
             district=district,
             user_type=user_type,
             password=password,
            address=address
            )
            
            data={"data":"Admin:add"}
            return render(request,"Admin/savedpage.html",data)
        except Exception as e:
            print(e)
            data={"data":"Admin:add"}
            return render(request,"Admin/failed_page.html",data)            

    return render(request, 'Admin/adminregisteraccounts.html')






@csrf_exempt
def profile(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('Name')
            email = request.POST.get('Email')
            mobile_no = request.POST.get('mobile')
            district = request.POST.get('district')
            address =request.POST.get('address')
            password =request.POST.get('password')


            print(name,email,mobile_no,district,address,password)
            teacher = registrationtable(
             name=name,
             mobile_no=mobile_no,
             email=email,
             district=district,
             user_type=1,
             password=password,
             address=address
            )
            teacher.save()
        except Exception as e:
            print(e)

    a=registrationtable.objects.filter(user_type=1).first()
    return render(request,"Admin/profile.html",{"data":a})


def add_post(request):
    if request.method == 'POST':
        content_name = request.POST.get('content_name')
        content_desc = request.POST.get('content_desc')
        content_img = request.FILES.get('content_img')
        
        if content_name and content_desc and content_img:
            # Create and save the new post
            new_post = contenttable(
                content_name=content_name,
                content_desc=content_desc,
                content_img=content_img
            )
            new_post.save()
            
            return redirect('Admin:post') 
    post=contenttable.objects.all().order_by("-content_id")    
    return render(request, 'Admin/post.html',{"posts":post})



def CaseStatus(request):
    b=AllocateCase.objects.all().order_by("-case_id")
    return render(request,"Admin/CaseStatus.html",{"cases":b})




def CaseStatus2(request,id):
    b=AllocateCase.objects.filter(id=id).first()
    c=CaseFlow.objects.filter(case_id=b.case_id)    
    return render(request,"Admin/CaseStatus2.html",{"data":b,"c":c})


def SubmitCase(request,id):
    b=AllocateCase.objects.filter(id=id).first()
    b.AdminApproval=1
    b.save()
    t=crimetable.objects.filter(case_id=b.case_id).first()
    t.case_progress=1
    t.save()
    return redirect("Admin:CaseStatus")


def CancelCase(request,id):
    b=AllocateCase.objects.filter(id=id).first()
    b.casestatus=0
    b.ManagerApproval=0
    b.save()
    return redirect("Admin:CaseStatus")
