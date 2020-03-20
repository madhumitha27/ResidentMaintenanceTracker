
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
    gender = models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
    vehNumber = models.CharField(max_length=100,blank=True)
    is_Primary = models.CharField ( max_length=200 , choices=PRIMARY , default='no' )
    unitID = models.ForeignKey(UnitDetail, on_delete=models.SET_NULL,blank=True,null=True, related_name='units')
    phone_number = models.PositiveIntegerField ()
    moveInDate= models.DateField(max_length=100)
    moveOutDate = models.DateField ( max_length=100 )
    rent = models.PositiveIntegerField ()
    occupation = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
    modifiedBy=models.CharField(max_length=200)

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
    status = models.CharField (max_length=100,choices=STATUS )
    accessInstructions=models.CharField(max_length=200)
    perToEnter = models.CharField (max_length=50, choices=PERMISSION , default='no' )
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
    modifiedBy=models.CharField(max_length=200)

    def created(self):
        self.created_date = timezone.now()
        self.save()

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
