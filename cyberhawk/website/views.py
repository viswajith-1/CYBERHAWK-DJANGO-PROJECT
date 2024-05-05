from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from .forms import CaseRecordForm
from .models import contenttable, crimetable, registrationtable

def generalhome(request):
    return render(request, 'generalhome.html', {})

def generallearningcorner(request):
    return render(request, 'generallearningcorner.html', {})

def generalpost(request):
    return render(request, 'generalpost.html', {})

def generalcontactus(request):
    return render(request, 'generalcontactus.html', {})

def generalfaq(request):
    return render(request, 'generalfaq.html', {})

def generalregister(request):

    if request.method == 'POST':
             name = request.POST.get('username')
             mobile_no = request.POST.get('userphone')
             email = request.POST.get('useremail')
             district = request.POST.get('userdistrict')
             address = request.POST.get('useraddress')
             user_type = request.POST.get('usertype')
             password = request.POST.get('userpassword')
             try:
                registrationtable.objects.create(
                     name = name,
                     mobile_no = mobile_no,
                     email = email,
                     district = district,
                     address = address,
                     user_type = user_type,
                     password = password
                )
             except:
                return render(request,"generalregister.html",{})  
    
    return render(request, 'generalregister.html', {})

def adminpost(request):

    if request.method == 'POST':
        postname = request.POST.get('postname')
        postdesc = request.POST.get('postdescription')
        try:
                contenttable.objects.create(
                    content_name =postname,
                    content_desc = postdesc
                )
        except:
                return render(request,"adminregisteraccounts.html",{})

    return render(request, 'adminpost.html', {})

def adminregisteraccount(request):
     
     if request.method == 'POST':
             name = request.POST.get('username')
             mobile_no = request.POST.get('userphone')
             email = request.POST.get('useremail')
             district = request.POST.get('userdistrict')
             address = request.POST.get('useraddress')
             user_type = request.POST.get('usertype')
             password = request.POST.get('userpassword')
             try:
                registrationtable.objects.create(
                     name = name,
                     mobile_no = mobile_no,
                     email = email,
                     district = district,
                     address = address,
                     user_type = user_type,
                     password = password
                )
             except:
                return render(request,"adminregisteraccounts.html",{})  
    
     return render(request, 'adminregisteraccounts.html', {})
     
def generallogin(request):
     return render(request, 'generallogin.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, "You've logged out")
	return redirect('generalhome')

def registercase(request):
        
        if request.method == 'POST':
             victim_name = request.POST.get('victimname')
             victim_gender = request.POST.get('gender')
             victim_age = request.POST.get('victimage')
             victim_dob = request.POST.get('victimdob')
             victim_address = request.POST.get('victimaddress')
             incident_type = request.POST.get('incidenttype')
             description = request.POST.get('crimedescription')
             district = request.POST.get('district')
             incident_date = request.POST.get('incidentdate')
             mobile_no = request.POST.get('victimphone')

             try:
             
                crimetable.objects.create(
                victim_name = victim_name,
                victim_gender = victim_gender,
                victim_age = victim_age,
                victim_dob = victim_dob,
                victim_address = victim_address,
                incident_type = incident_type,
                description = description,
                district = district,
                incident_date =incident_date,
                mobile_no = mobile_no
                )
             
             except:
                return render(request,"registercase.html",{})


        return render(request, 'registercase.html', {})
    
