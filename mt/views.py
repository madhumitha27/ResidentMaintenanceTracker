from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import render , get_object_or_404 , redirect

# Create your views here.
from django.template.loader import get_template
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User , Group
from reportlab.pdfgen import canvas
import calendar
from .forms import RequestsForm , RequestsEditForm , ResUnitForm , ResProfileForm , UnitEditForm , RegisterForm , \
    PackageForm , SubmissionExportForm , \
    EmailForm , LoginForm , UserEditForm , ReservationForm , ReservationEditForm , PackageEditForm
from .models import RequestDetail , ResidentDetail , UnitDetail , EventsDetail,PackageDetail
from .utils import render_to_pdf , StaffCalendar
from django.views import generic

def index(request):
    return render(request, 'mt/index.html')
def home(request):
    #Below code for inserting in Nurse Table if the user registered as Nurse role and also if there is no entry alredy
    print(request.path)
    if(request.path=='/home/'):
        user = User.objects.get ( pk=request.user.id )
        print(user.username)
        if(user.groups.filter(name = "resident").exists()):
          print("its resident")
          count = ResidentDetail.objects.filter ( username_id=request.user.id ).count ( )
          print('count',count)
          if (count == 0) :
             nurse = ResidentDetail.objects.create ( username_id=request.user.id ,email=request.user.email)
    #End
    return render(request, 'mt/appHome.html')

def userList(request):
    users = User.objects.all ( )
    # print(users)
    return render ( request , 'mt/users_list.html' , {'users' : users} )


@login_required
def user_edit(request, pk):
   user = get_object_or_404(User, pk=pk)
   if request.method == "POST":
       # update
       form = UserEditForm(request.POST, instance=user)
       if form.is_valid():
           user = form.save(commit=False)
           user.updated_date = timezone.now()
           user.save()
           users = User.objects.filter()
           return render(request, 'mt/users_list.html',
                         {'users': users})
   else:
        # edit
       form = UserEditForm(instance=user)
       return render(request, 'mt/user_edit.html', {'form': form})


def user_delete(request, username):
    users = User.objects.get(username=username)
    users.delete()
    allUsers = User.objects.all ( )
    # print(users)
    return render ( request , 'mt/users_list.html' , {'users' : allUsers} )

def register(request):
    print("entered into register view method")
    if request.method == 'POST':
        print("entered into register view method entered if method")
        form = RegisterForm(request.POST)
        if form.is_valid():
            userObj =form.save()
            my_group = Group.objects.get ( name=form.cleaned_data['group'])
            userObj.groups.add ( my_group )
            userObj.save()
            return render(request,
                          'registration/registerdone.html',
                          {'form': form})
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def request_list(request):
    print(request.user.username)
    print ( request.user.id )
    ResidentObject = ResidentDetail.objects.get ( username_id=request.user.id )
    print('username--',ResidentObject.username)
    MainRrequests =RequestDetail.objects.filter(username_id=ResidentObject.id)
    print(MainRrequests)
    return render(request, 'mt/request_list.html',
                 {'requests': MainRrequests})

@login_required
def booking_list(request):

    user = User.objects.get ( pk=request.user.id )
    if user.groups.filter ( name='resident' ).exists ( ) :
        print ( 'resident' )
        ResidentObject = ResidentDetail.objects.get ( username_id=request.user.id )
        EventsDetailList = EventsDetail.objects.filter ( username_id=ResidentObject.id )

    else :
       EventsDetailList = EventsDetail.objects.all()
    return render(request, 'mt/BookingList.html',
                 {'EventsDetailList': EventsDetailList})

@login_required
def package_list(request):
    PackageDetailList = PackageDetail.objects.all()

    return render(request, 'mt/packageList.html',
                 {'PackageList': PackageDetailList})

def request_new(request):
   print('inside')
   if request.method == "POST":
       form = RequestsForm(request.POST)
       if form.is_valid():
           requestObject = form.save(commit=False)
           requestObject.status = "new"
           requestObject.modifiedBy = request.user.username
           ResidentObject = ResidentDetail.objects.get ( username_id=request.user.id )

           requestObject.username_id=ResidentObject.id
           requestObject.save()
           print('saved')
           requestList = RequestDetail.objects.filter(username_id=ResidentObject.id)
           return render(request, 'mt/request_list.html',
                         {'requests': requestList})
   else:
       form = RequestsForm()
       # print("Else")
   return render(request, 'mt/request_new.html', {'form': form})

def reservation_new(request):
   print('inside')
   if request.method == "POST":
       form = ReservationForm(request.POST)
       if form.is_valid():
           reservationObject = form.save(commit=False)
           today = date.today ( )
           reservationObject.created_date =today
           reservationObject.status = "NEW"
           reservationObject.reason = "-"
           reservationObject.amount = "0"
           reservationObject.advAmtPaid = "0"
           reservationObject.modifiedBy = request.user.username

           ResidentObject = ResidentDetail.objects.get ( username_id=request.user.id )
           EventsDetailList = EventsDetail.objects.filter ( username_id=ResidentObject.id )

           reservationObject.username_id=ResidentObject.id
           reservationObject.save()
           print('saved')

           return render(request, 'mt/BookingList.html',
                         {'EventsDetailList': EventsDetailList})
   else:
       form = ReservationForm()
       # print("Else")
   return render(request, 'mt/reservation_new.html', {'form': form})


def sendEmail(subject,content,email_from,recList):
    email = EmailMessage ( subject , content , email_from , recList )
    email.send ( )


def package_new(request):
   print('inside')
   if request.method == "POST":
       form = PackageForm(request.POST)
       if form.is_valid():
           packageObject = form.save(commit=False)
           today = date.today ( )
           packageObject.created_date =today
           packageObject.modifiedBy = request.user.username
           packageObject.save ( )
           print('saved')
           subject = "A Package Received!!!!"
           content = "You have received package from "+packageObject.description
           recList = [packageObject.username.email]
           email_from = settings.EMAIL_HOST_USER
           sendEmail(subject,content,email_from,recList)
           return render(request, 'mt/packageSentEmail.html')
   else:
       form = PackageForm()
       # print("Else")
   return render(request, 'mt/packageNew.html', {'form': form})



def staffrequest_list(request):
    print ( request.user.username )
    # get_object_or_404 ( Nurse , nurse_name=request.user.username )
    MainRrequests = RequestDetail.objects.filter ( )
    print ( MainRrequests )
    return render ( request , 'mt/staffReqList.html' ,
                    {'requests' : MainRrequests} )
def res_unit(request):
    print ( request.user.username )
    # get_object_or_404 ( Nurse , nurse_name=request.user.username )
    resident = ResidentDetail.objects.filter ( created_date__lte=timezone.now ( ) )

    return render ( request , 'mt/residentUnit.html' ,
                    {'resList' : resident} )

class CalendarStaffView(generic.ListView):
    model = EventsDetail
    template_name = 'mt/viewCalendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = StaffCalendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['staffcalendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def unit_list ( request ) :
    print ( request.user.username )
    # get_object_or_404 ( Nurse , nurse_name=request.user.username )
    unitList= UnitDetail.objects.filter ( created_date__lte=timezone.now ( ) )

    return render ( request , 'mt/UnitList.html' ,
                    {'unitList' : unitList} )
def adminUnit_list ( request ) :
    print ( request.user.username )
    # get_object_or_404 ( Nurse , nurse_name=request.user.username )
    unitList= UnitDetail.objects.filter ( created_date__lte=timezone.now ( )   )

    return render ( request , 'mt/AdminUnitList.html' ,
                    {'unitList' : unitList} )
def res_profile(request):
    print('test');
    userObject = User.objects.get ( id=request.user.id )
    residentObject = ResidentDetail.objects.get ( username_id=request.user.id  )
    unitID=residentObject.unitID_id
    isPrimary=residentObject.is_Primary
    if(isPrimary=="yes"):
        tempVariable="no"
    else:
        tempVariable="yes"
    coResuserObject = ""
    unitDetail=""
    print(unitID)

    coResident =ResidentDetail.objects.filter(is_Primary=tempVariable , unitID_id=unitID)
    if(unitID):
        unitDetail = UnitDetail.objects.get ( id=unitID )
    if(coResident):
            coResident = ResidentDetail.objects.get ( is_Primary=tempVariable , unitID_id=unitID )
            coResuserObject = User.objects.get ( id=coResident.username_id )
    return render ( request , 'mt/residentProfile.html' ,
                    {'userDetail' : userObject ,
                     'residentDetail' : residentObject,
                     'unitDetail':unitDetail,
                     'coResidentDetail':coResuserObject} )

@login_required
def request_edit(request, pk):
   print('edit req')
   req = get_object_or_404(RequestDetail, pk=pk)
   if request.method == "POST":
       form = RequestsEditForm(request.POST, instance=req)
       if form.is_valid():
           service = form.save()
           service.updated_date = timezone.now()
           service.save()
           services = RequestDetail.objects.all()
           return render(request, 'mt/staffReqList.html', {'requests': services})
   else:
       # print("else")
       form = RequestsEditForm(instance=req)
   return render(request, 'mt/staffEditRequest.html', {'form': form})

@login_required
def package_edit(request, pk):
   print('edit req')
   req = get_object_or_404(PackageDetail, pk=pk)
   if request.method == "POST":
       form = PackageEditForm(request.POST, instance=req)
       if form.is_valid():
           package = form.save(commit=False)
           package.pickupDateTime = timezone.now ( )
           package.updated_date = timezone.now()
           package.modifiedBy = request.user.username

           pickupDate=package.pickupDateTime.strftime("%Y-%m-%d")
           pickupTime=package.pickupDateTime.strftime("%H:%M")
           package.save ( )
           subject = "Package PickedUP!!!!"
           content = "Your "+package.description+" package picked up by " + package.pickupPerson +" at "+pickupDate+" , "+pickupTime+"."
           recList = [package.username.email]
           email_from = settings.EMAIL_HOST_USER
           sendEmail ( subject , content , email_from , recList )
           return render ( request , 'mt/packageSentEmail.html' )
   else:
       # print("else")
       form = PackageEditForm(instance=req)
   return render(request, 'mt/packageEdit.html', {'form': form})

@login_required
def booking_edit(request, pk):
   print('edit req')
   evtDetail = get_object_or_404(EventsDetail, pk=pk)
   if request.method == "POST":
       form = ReservationEditForm(request.POST, instance=evtDetail)
       if form.is_valid():
           service = form.save()
           service.updated_date = timezone.now()
           service.modifiedBy = request.user.username
           service.save()
           evtList = EventsDetail.objects.all()
           return render(request, 'mt/BookingList.html', {'EventsDetailList': evtList})
   else:
       # print("else")
       form = ReservationEditForm(instance=evtDetail)
   return render(request, 'mt/reservation_new.html', {'form': form})

@login_required
def resUnit_edit(request, pk):
   print('edit req')
   res = get_object_or_404(ResidentDetail, pk=pk)
   if request.method == "POST":
       form = ResUnitForm(request.POST, instance=res)
       if form.is_valid():
           resunit = form.save()
           resunit.updated_date = timezone.now()
           resunit.save()
           resList = ResidentDetail.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mt/residentUnit.html', {'resList': resList})
   else:
       # print("else")
       form = ResUnitForm(instance=res)
   return render(request, 'mt/resUnitEdit.html', {'form': form})

@login_required
def resprofile_edit(request, pk):
   print('edit req')
   req = get_object_or_404(ResidentDetail, pk=pk)
   if request.method == "POST":
       form = ResProfileForm(request.POST, instance=req)
       if form.is_valid():
           service = form.save()
           service.updated_date = timezone.now()
           service.save()
           residentObject = ResidentDetail.objects.get ( username_id=request.user.id )
           userObject = User.objects.get ( id=request.user.id )
           userObject.email=residentObject.email
           userObject.save()
           return HttpResponseRedirect ( reverse ( 'mt:res_profile' ) )
   else:
       # print("else")
       form = ResProfileForm(instance=req)
   return render(request, 'mt/resProfileEdit.html', {'form': form})


def unit_add(request):
   print('inside')
   if request.method == "POST":
       form = UnitEditForm(request.POST)
       if form.is_valid():
         unitObject = form.save(commit=False)
         unitObject.save()
         print('saved')
         unitList = UnitDetail.objects.filter( created_date__lte=timezone.now ( )  )
         return render(request, 'mt/AdminUnitList.html',
                         {'unitList': unitList})
   else:
       form = UnitEditForm()
       print("Else")
   return render(request, 'mt/resUnitAdd.html', {'form': form})
   #return render ( request , 'mt/AdminUnitList.html' )


def search_form(request):
   if request.method == "POST":
       form = SubmissionExportForm ( request.POST )
       print ( form )
       reqList = RequestDetail.objects.filter (
           created_date__range=[form.cleaned_data['from_date'] , form.cleaned_data['to_date']] )
       context = {'requests' : reqList}
       template = get_template ( 'mt/RequestSummary.html' )
       html = template.render ( context )
       pdf = render_to_pdf ( 'mt/RequestSummary.html' , context )
       response = HttpResponse ( pdf , content_type='application/pdf' )
       response['Content-Disposition'] = 'attachment; filename="report.pdf"'
       p = canvas.Canvas ( pdf )
       p.setFont ( "Times-Roman" , 55 )
       p.showPage ( )
       p.save ( )
       return response
   else:
       context = {}
       today = date.today ( )
       first_day = today.replace ( day=1 )
       last_day =  first_day + relativedelta(months=+1, days=-1)
       context['form'] = SubmissionExportForm (initial={'from_date': first_day,'to_date':last_day} )
       return render ( request , "mt/searchForm.html" , context )

def resident_email(request):
    recipient_list = list ( ResidentDetail.objects.filter().values_list ( 'email' , flat=True ) )
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            subject = request.POST.get('subject')
            content = request.POST.get('content')
            recList=[request.POST.get('mail_id')]
            email_from = settings.EMAIL_HOST_USER
            email = EmailMessage ( subject , content , email_from ,recList)
            email.send( )
            return render(request, 'mt/sent.html')
    else:
        recList=', '.join(recipient_list)
        form = EmailForm(initial={'mail_id': recList})
        return render(request, 'mt/sendemail.html', {'form': form})










