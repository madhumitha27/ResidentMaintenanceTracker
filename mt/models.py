from datetime import datetime
import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone

PRIORITY = (
    ('standard','STANDARD'),
    ('urgent', 'URGENT'),
)
PERMISSION = (
    ('yes','YES'),
    ('no', 'NO'),
)
STATUS = (
    ('new','NEW'),
    ('in-progress', 'IN-PROGRESS'),
    ('completed', 'COMPLETED'),
)
PRIMARY = (
    ('yes','YES'),
    ('no', 'NO'),
)
LOCATION = (
    ('PARTY HALL','PARTY HALL'),
    ('SWIMMING POOL', 'SWIMMING POOL'),
    ('KIDS PLAYING AREA', 'KIDS PLAYING AREA'),
)
EVENTSTATUS = (
    ('APPROVED','APPROVED'),
    ('DECLINED', 'DECLINED'),
    ('NEW' , 'NEW')
)
GENDER = (
    ('FEMALE','FEMALE'),
    ('MALE', 'MALE'),
    ('OTHERS' , 'OTHERS')
)
class UnitDetail(models.Model):
    unitID = models.PositiveIntegerField()
    aptNo = models.PositiveIntegerField ()
    street = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.PositiveIntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.unitID)

class ResidentDetail(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,related_name='residents')
    gender = models.CharField(max_length=100,choices=GENDER,blank=True,null=True)
    email=models.CharField(max_length=200,blank=True,null=True)
    dob = models.DateField(max_length=100,blank=True,null=True)
    vehNumber = models.CharField(max_length=100,blank=True,null=True)
    is_Primary = models.CharField ( max_length=200 , choices=PRIMARY , default='no' ,blank=True,null=True)
    unitID = models.ForeignKey(UnitDetail, on_delete=models.SET_NULL,null=True, blank=True,related_name='units')
    phone_number = models.CharField(max_length=200,blank=True,null=True)
    moveInDate= models.DateField(max_length=100,blank=True,null=True)
    moveOutDate = models.DateField ( max_length=100 ,blank=True,null=True)
    rent = models.PositiveIntegerField (blank=True,null=True)
    occupation = models.CharField(max_length=200,blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
    modifiedBy=models.CharField(max_length=200,blank=True,null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.username)


class Category(models.Model):
    catID = models.PositiveIntegerField()
    type = models.CharField ( max_length=200 )
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.type)

class RequestDetail(models.Model):
    username=models.ForeignKey(ResidentDetail, on_delete=models.CASCADE, related_name='residents')
    priority = models.CharField (max_length=50,choices=PRIORITY , default='standard' )
    type = models.ForeignKey ( Category, on_delete=models.SET_NULL,blank=True,null=True, related_name='categories')
    status = models.CharField (max_length=100,choices=STATUS,blank=True,null=True )
    accessInstructions=models.CharField(max_length=200,blank=True,null=True)
    desc = models.CharField ( max_length=200 , blank=True , null=True )
    perToEnter = models.CharField (max_length=50, choices=PERMISSION , default='no' )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    modifiedBy=models.CharField(max_length=200,blank=True,null=True)

    #def created(self):
        #self.created_date = default=datetime.date.today
       # self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.username)

class EventsDetail(models.Model):
    username=models.ForeignKey(ResidentDetail, on_delete=models.CASCADE, related_name='users')
    eventDate =models.DateField( auto_now=False, auto_now_add=False)
    eventStartTime =models.TimeField(auto_now=False, auto_now_add=False)
    eventEndTime = models.TimeField (auto_now=False, auto_now_add=False)
    description=models.CharField(max_length=200)
    amount = models.PositiveIntegerField ( blank=True , null=True )
    advAmtPaid = models.PositiveIntegerField (blank=True , null=True )
    location = models.CharField (max_length=50, choices=LOCATION )
    status = models.CharField ( max_length=50 , choices=EVENTSTATUS, blank=True)
    reason = models.CharField ( max_length=200 , blank=True , null=True )
    participantCount = models.CharField ( max_length=200  )
    created_date = models.DateTimeField ( default=timezone.now )
    updated_date = models.DateTimeField ( default=timezone.now  )
    modifiedBy = models.CharField ( max_length=200)

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.username)

class PackageDetail(models.Model):
    username=models.ForeignKey(ResidentDetail, on_delete=models.CASCADE, related_name='user')
    description =  models.CharField (max_length=200 )
    pickupDateTime =  models.DateTimeField(max_length=100, blank=True , null=True )
    pickupPerson = models.CharField ( max_length=200 , blank=True , null=True )
    created_date = models.DateTimeField ( default=timezone.now )
    updated_date = models.DateTimeField ( auto_now_add=True )
    modifiedBy = models.CharField ( max_length=200  )

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.username)

class Communication(models.Model):
    mail_id=models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField ( auto_now_add=True )

    def created(self):
        self.created_date = timezone.now()
        self.save()
    def __str__(self):
        return str(self.subject)

    def updated(self):
        self.updated_date = timezone.now()
        self.save()


