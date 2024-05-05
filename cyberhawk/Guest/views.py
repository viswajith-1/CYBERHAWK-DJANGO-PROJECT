from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from website.models import *
# Create your views here.


def home(request):
    return render(request,"GeneralHome.html",{})

def faq(request):
    return render(request,"generalfaq.html",{})

def contactus(request):
    return render(request,"generalcontactus copy.html",{})

def generallearningcorner(request):
    return render(request,"generallearningcorner.html",{})

def newsUpdates(request):
    c=contenttable.objects.all().order_by("-content_id")
    return render(request,"newsUpdates.html",{"posts":c})


@csrf_exempt
def Login(request):    
    if request.method == 'POST':
        print("------ Login Request Processing -------")
        userid=request.POST.get('userid')
        password=request.POST.get('password')
        type=request.POST.get('type')
        print(request.POST)
        try:
            if type=="Admin":
                    ob=registrationtable.objects.get(email=userid,password=password,user_type=1)
                    return JsonResponse({'status': 1})
            elif type=="Manager":
                ob=registrationtable.objects.get(email=userid,password=password,user_type=2)
                request.session['gmail']=ob.email
                return JsonResponse({'status': 2})
            elif type=="Staff":
                ob=registrationtable.objects.get(email=userid,password=password,user_type=3)
                request.session['gmail']=ob.email
                return JsonResponse({'status': 3})

            elif type=="User":
                ob=registrationtable.objects.get(email=userid,password=password,user_type=4)
                request.session['gmail']=ob.email
                return JsonResponse({'status': 4})

            else:
                ob=UserRegTbl.objects.get(email=userid,password=password)
                request.session['gmail']=ob.email
                return JsonResponse({'status': 5})
        except Exception as e:
            print(e)
            return JsonResponse({'status': "failed"})
    return render(request,"login.html")



def UserRegister(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('username')
            mobile_no = request.POST.get('userphone')
            email = request.POST.get('useremail')
            district = request.POST.get('userdistrict')
            address =request.POST.get('useraddress')

            user_type = 4
            password = request.POST.get('userpassword')
            # Create and save the Teacher instance
            teacher = registrationtable.objects.create(
             name=name,
             mobile_no=mobile_no,
             email=email,
             district=district,
             user_type=user_type,
             address=address,
             password=password
            )
            
            data={"data":"Guest:UserRegister"}
            return render(request,"savedpage.html",data)
        except Exception as e:
            print(e)
            data={"data":"Guest:UserRegister"}
            return render(request,"failed_page.html",data)            


    return render(request,"UserRegister.html",{})


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
    c=crimetable.objects.get(case_id=id)
    try:
        print(id)
        plan=CaseFlow.objects.create(case_id=c,description=description,findings=finding)
    except Exception as e:
        print(e)
    data={}
    return JsonResponse(data,safe=False)