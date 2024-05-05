from django.shortcuts import render,redirect
from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from website.models import *
# Create your views here.


def home(request):
    user=request.session['gmail']
    a=registrationtable.objects.filter(email=user,user_type=2).first()
    return render(request,"Manager/home.html",{"name":a.name})

def CaseStatus(request):
    user=request.session['gmail']
    a=registrationtable.objects.filter(email=user,user_type=2).first()
    b=AllocateCase.objects.filter(office__district=a.district,AdminApproval=0)

    return render(request,"Manager/CaseStatus.html",{"cases":b})


def Finished(request):
    user=request.session['gmail']
    a=registrationtable.objects.filter(email=user,user_type=2).first()
    b=AllocateCase.objects.filter(office__district=a.district,AdminApproval=1)

    return render(request,"Manager/Finished.html",{"cases":b})


def Finished2(request,id):
    b=AllocateCase.objects.filter(id=id).first()
    c=CaseFlow.objects.filter(case_id=b.case_id)      
    return render(request,"Manager/CaseStatus2C.html",{"data":b,"c":c})


def CaseStatus2(request,id):
    b=AllocateCase.objects.filter(id=id).first()
    c=CaseFlow.objects.filter(case_id=b.case_id)    
    return render(request,"Manager/CaseStatus2.html",{"data":b,"c":c})


def SubmitCase(request,id):
    b=AllocateCase.objects.filter(id=id).first()
    b.ManagerApproval=1
    b.save()
    return redirect("Manager:CaseStatus")


def CancelCase(request,id):
    b=AllocateCase.objects.filter(id=id).first()
    b.casestatus=0
    b.save()
    return redirect("Manager:CaseStatus")

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
             user_type=2,
             password=password,
             address=address
            )
            teacher.save()
        except Exception as e:
            print(e)
    user=request.session['gmail']
    a=registrationtable.objects.filter(user_type=2,email=user).first()
    return render(request,"Manager/profile.html",{"data":a})



@csrf_exempt
def ViewEmployees(request):
    user=request.session['gmail']
    k=registrationtable.objects.filter(email=user,user_type=2).first()
    a=registrationtable.objects.filter(district=k.district,user_type=3)
    return render(request,"Manager/ViewEmploye.html",{"cases":a,"d":k.district})

@csrf_exempt
def Assign(request):
    user=request.session['gmail']
    a=registrationtable.objects.filter(email=user,user_type=2).first()
    a=crimetable.objects.filter(district=a.district,case_progress=0)
    return render(request,"Manager/caseviewmore.html",{"cases":a})




@csrf_exempt
def Assign1(request,id):
    user=request.session['gmail']
    ob=registrationtable.objects.filter(email=user,user_type=2).first()
    a=registrationtable.objects.filter(district=ob.district,user_type=3)
    l=crimetable.objects.filter(case_id=id).first()
    return render(request,"Manager/assign1.html",{"case":l,"officers":a})


@csrf_exempt
def Assign2(request,id):
    user=request.POST.get("officer")
    a=registrationtable.objects.filter(email=user).first()
    l=crimetable.objects.filter(case_id=id).first()
    AllocateCase.objects.create(case_id=l,office=a)
    l.case_progress=2
    l.save()
    return redirect("Manager:Assign")


