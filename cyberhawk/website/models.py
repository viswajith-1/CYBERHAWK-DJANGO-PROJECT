from django.db import models


class registrationtable(models.Model):
    name =models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=15)
    email = models.CharField(max_length=30,primary_key='true')
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20)  ##  1- admin , 2- manager ,3- staff , 4- user
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return (f"{self.name} {self.user_type} {self.email}")


class crimetable(models.Model):
    case_id = models.IntegerField(primary_key='true', auto_created="true")
    victim_name =models.CharField(max_length=30)
    victim_gender = models.CharField(max_length=50)
    victim_age =models.CharField(max_length=15)
    victim_dob = models.CharField(max_length=15)
    mobile_no = models.CharField(max_length=15)
    email = models.CharField(max_length=40)
    victim_address = models.CharField(max_length=50)
    incident_type = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    district = models.CharField(max_length=25)
    incident_date = models.CharField(max_length=20)
    case_progress = models.IntegerField(default=0) # 1- case closed , 0- registred , 2- case is on going
    userid=models.ForeignKey(registrationtable,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return (f"{self.case_id} {self.victim_name} {self.incident_type}") 

class contenttable(models.Model):
    content_id = models.IntegerField(primary_key='true', auto_created="true")
    content_name = models.CharField(max_length=50)
    content_img = models.ImageField(upload_to ='uploads/Post',null=True)
    content_desc = models.CharField(max_length=200)
    content_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.content_id} {self.content_name} {self.content_date}")


class AllocateCase(models.Model):
    case_id = models.ForeignKey(crimetable,on_delete=models.CASCADE)
    office=models.ForeignKey(registrationtable,on_delete=models.CASCADE)
    casestatus=models.IntegerField(default=0)  # 0- Started , 1- Submitted
    ManagerApproval=models.IntegerField(default=0)
    AdminApproval=models.IntegerField(default=0)
    title=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=1000,null=True)
    statisfied_Sts=models.IntegerField(default=0)

class CaseFlow(models.Model):
    date=models.DateField(auto_now=True)
    findings=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    case_id = models.ForeignKey(crimetable,on_delete=models.CASCADE)
    
