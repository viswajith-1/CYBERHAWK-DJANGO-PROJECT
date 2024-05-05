from django.shortcuts import render,redirect
from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from website.models import *
# Create your views here.


def home(request):
    return render(request,"Staff/home.html",{})




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
             user_type=3,
             password=password,
             address=address
            )
            teacher.save()
        except Exception as e:
            print(e)
    user=request.session['gmail']
    a=registrationtable.objects.filter(user_type=3,email=user).first()
    return render(request,"Staff/profile.html",{"data":a})


@csrf_exempt
def Assign(request):
    user=request.session['gmail']
    a=registrationtable.objects.filter(email=user,user_type=3).first()
    a=AllocateCase.objects.filter(office=a,casestatus=0)
    return render(request,"Staff/caseviewmore.html",{"cases":a})


@csrf_exempt
def Assign1(request,id):
    a=crimetable.objects.filter(case_id=id).first()
    b=CaseFlow.objects.filter(case_id=a)
    return render(request,"Staff/casereport.html",{"data":a,"developments":b})



import json
@csrf_exempt
def deleteplan(request):
    id=json.loads(request.body)["id"]
    a=CaseFlow.objects.get(id=id)
    a.delete()
    return JsonResponse(data,safe=False)



@csrf_exempt
def saveplan(request):
    id=json.loads(request.body)["bookid"]
    description=json.loads(request.body)["workoutDesc"]
    finding=json.loads(request.body)["workoutName"]
    try:
        print(id)
        plan=CaseFlow.objects.create(case_id=id,description=description,findings=finding)
    except Exception as e:
        pass
    data={}
    return JsonResponse(data,safe=False)

@csrf_exempt
def SubmitCase(request,id):
    a=crimetable.objects.filter(case_id=id).first()
    return render(request,"Staff/submitcase.html",{"data":a})    


@csrf_exempt
def SubmitCase1(request,id):
    if request.method == 'POST':
        case_title = request.POST.get('case_title')
        case_description = request.POST.get('case_description')
        a=crimetable.objects.filter(case_id=id).first()
        a=AllocateCase.objects.get(case_id=a)
        a.description=case_description
        a.title=case_title
        a.casestatus=1
        a.save()
    return redirect("Staff:home")

@csrf_exempt
def finished(request):
    user=request.session['gmail']
    a=registrationtable.objects.filter(email=user,user_type=3).first()
    a=AllocateCase.objects.filter(office=a,casestatus=1)
    return render(request,"Staff/finished.html",{"cases":a})    