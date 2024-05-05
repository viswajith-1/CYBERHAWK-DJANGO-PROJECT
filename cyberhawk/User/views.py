from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from website.models import *
# Create your views here.

@csrf_exempt
def home(request):
    return render(request,"User/home.html",{})


def newsUpdates(request):
    c=contenttable.objects.all().order_by("-content_id")
    return render(request,"User/newsUpdates.html",{"posts":c})


@csrf_exempt
def registercase(request):
    if request.method == 'POST':
        try:
            victimname = request.POST.get('victimname')
            gender = request.POST.get('gender')
            victimage = request.POST.get('victimage')
            victimphone = request.POST.get('victimphone')
            victimdob =request.POST.get('victimdob')
            district = request.POST.get('district')
            victimaddress = request.POST.get('victimaddress')
            incidenttype = request.POST.get('incidenttype')
            crimedescription = request.POST.get('crimedescription')
            incidentdate =request.POST.get('incidentdate')

            user=request.session['gmail']
            a=registrationtable.objects.filter(email=user,user_type=4).first()

            # Create and save the Teacher instance
            teacher = crimetable.objects.create(
            victim_name=victimname, 
            victim_gender=gender,
            victim_age=victimage,
            victim_dob=victimdob,
            district=district,
            victim_address=victimaddress,
            incident_date=incidentdate,
            mobile_no=victimphone,
            incident_type=incidenttype,
            description=crimedescription,
            userid=a
        

            )
            
            data={"data":"User:registercase"}
            return render(request,"User/savedpage.html",data)
        except Exception as e:
            print(e)
            data={"data":"User:registercase"}
            return render(request,"User/failed_page.html",data)            


    return render(request,"User/registercase.html",{})



@csrf_exempt
def caseviewmore(request):
    user=request.session['gmail']
    a=registrationtable.objects.filter(email=user,user_type=4).first()
    a=crimetable.objects.filter(userid=a)
    return render(request,"User/caseviewmore.html",{"cases":a})


@csrf_exempt
def view_case(request,id):
    a=crimetable.objects.filter(case_id=id).first()
    b=AllocateCase.objects.filter(case_id=a).first()
    c=CaseFlow.objects.filter(case_id=b.case_id) 
    return render(request,"User/CaseStatus2.html",{"data":b,"c":c})


def SubmitCase(request,id):
    b=AllocateCase.objects.filter(id=id).first()
    b.statisfied_Sts=1
    b.save()
    return redirect("User:caseviewmore")


def CancelCase(request,id):
    b=AllocateCase.objects.filter(id=id).first()
    b.statisfied_Sts=0
    b.save()
    return redirect("User:caseviewmore")


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
             user_type=4,
             password=password,
             address=address
            )
            teacher.save()
        except Exception as e:
            print(e)
    user=request.session['gmail']
    a=registrationtable.objects.filter(user_type=4,email=user).first()
    return render(request,"User/profile.html",{"data":a})

