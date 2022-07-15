from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import boy,classes,techers,absence,Transport,driver,masrof, darajat, mawad,Monthly_exams,Staff,Staff_absence,Teachers_absence,Profile
from django.core.paginator import Paginator
from .filters import BoyFilter, Monthly_examsFilter, mawadFilter, techersFilter, absenceFilter, masrofFilter, classFilter,driverFilter, darajatFilter,Transport_Filter,StaffFilter,Staff_absenceFilter,Teachers_absenceFilter
from django.contrib.auth.decorators import login_required
from .form import boy_form, class_form, mawad_form, month_darajat_form, techer_form,absence_form,Transport_form,driver_form,masrof_form, darajat_form,teacher_absence_form,staff_absence_form,staff_form
from django.db.models import Sum
from django.views.generic import UpdateView
# Create your views here.
@login_required
def home(request):
    boys = boy.objects.filter(user=request.user)
    teacher = techers.objects.filter(user=request.user)
    the_classes = classes.objects.filter(user=request.user)
    staffs = Staff.objects.filter(user=request.user)
    drivers = driver.objects.filter(user=request.user)
    transports = Transport.objects.filter(user=request.user)
    paid = boys.filter(paids=True)
    expenses = masrof.objects.filter(user=request.user)
    context = {
        'boys':boys.count(),
        'teachers': teacher.count(),
        'classes':the_classes.count(),
        'staffs':staffs.count(),
        'drivers':drivers.count(),
        'transports':transports.count(),
        'paids':paid.count(),
        'expenses':expenses.count(),
    }
    return render(request, 'home/home.html',context)
@login_required
def boys(request):
    boys = boy.objects.filter(user=request.user).order_by('date')
    filter = BoyFilter(request.GET, queryset=boys,request=request)
    # filter.fields['boy_class'] = classes.objects.filter(user=request.user)
    boys = filter.qs
    paginator = Paginator(boys,225)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    context = {'boys':page_pbj, 'filter':filter, 'count':boys.count()}
    return render(request, 'project/boys.html', context)
@login_required
def classs(request):
    classs = classes.objects.filter(user=request.user).order_by('date')
    filter = classFilter(request.GET, queryset=classs,request=request)
    classs = filter.qs
    paginator = Paginator(classs,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    context = {'classes':page_pbj, 'filter':filter, 'count':classs.count()}
    return render(request, 'project/classes.html', context)
@login_required
def Boy(request, id):
    Boy = boy.objects.filter(id=id, user=request.user)
    return render(request, 'project/boy_details.html', context={'boy':Boy})
@login_required
def class_detail(request, id):
    class_detail = classes.objects.filter(id=id, user=request.user)
    class_boys = boy.objects.filter(boy_class=id,user=request.user)
    count_boy_class = class_boys.count()
    context={'class':class_detail, 'boy':class_boys,'count_boy_class':count_boy_class}
    return render(request, 'project/class_detail.html', context)
@login_required
def techeres(request):
    techeres = techers.objects.filter(user=request.user).order_by('date')
    filter = techersFilter(request.GET, queryset=techeres)
    techeres = filter.qs
    paginator = Paginator(techeres,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/teachers.html', context ={'teachers':page_pbj, 'filter':filter,'count': techeres.count()})
@login_required
def techer_detail(request, id):
    techer_detail = techers.objects.filter(id=id, user=request.user)
    return render(request, 'project/techer_detail.html', context={'techer':techer_detail})
@login_required
def absences(request):
    absences = absence.objects.filter(user=request.user).order_by('-add_date')
    filter = absenceFilter(request.GET, queryset=absences,request=request)
    absences = filter.qs
    paginator = Paginator(absences,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/absences.html', context ={'absences':page_pbj, 'filter':filter,'count':absences.count()})
@login_required
def absence_detail(request, id):
    absence_detail = absence.objects.filter(id=id, user=request.user)
    return render(request, 'project/absence_detail.html', context={'absence':absence_detail})
@login_required
def driveres(request):
    driveres = driver.objects.filter(user=request.user).order_by('date')
    filter = driverFilter(request.GET, queryset=driveres)
    driveres = filter.qs
    paginator = Paginator(driveres,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/driveres.html', context ={'driveres':page_pbj,'filter':filter, 'count':driveres.count()})
@login_required
def driver_detail(request, id):
    driver_detail = driver.objects.filter(id=id, user=request.user)
    return render(request, 'project/driver_detail.html', context={'driver':driver_detail})
@login_required
def masrofs(request):
    masrofs = masrof.objects.filter(user=request.user).order_by('date')
    filter = masrofFilter(request.GET, queryset=masrofs)
    masrofs = filter.qs
    paginator = Paginator(masrofs,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/masrofs.html', context ={'masrofs':page_pbj,'filter':filter, 'count':masrofs.count()})

@login_required
def masrof_detail(request, id):
    masrof_detail = masrof.objects.filter(id=id, user=request.user)
    return render(request, 'project/masrof_detail.html', context={'masrof':masrof_detail})

@login_required
def subject(request):
    mawads = mawad.objects.filter(user=request.user).order_by('date')
    filter = mawadFilter(request.GET, queryset=mawads)
    mawads = filter.qs
    paginator = Paginator(mawads,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/subjects.html', context ={'subjects':page_pbj,'filter':filter, 'count':mawads.count()})

@login_required
def subject_detail(request, id):
    subject_detail = mawad.objects.filter(id=id, user=request.user)
    return render(request, 'project/subject_detail.html', context={'subject':subject_detail})

@login_required
def darajats(request):
    darajats = darajat.objects.filter(user=request.user).order_by('add_date')
    filter = darajatFilter(request.GET, queryset=darajats)
    darajats =  filter.qs
    paginator = Paginator(darajats,20)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    context = {'darajat':page_pbj,'add':darajat.objects.get(id=5) , 'filter':filter, 'count':darajats.count()}
    return render(request, 'project/darajats.html', context)
@login_required
def print_all_darajat(request):
    darajats = darajat.objects.filter(user=request.user).order_by('add_date')
    filter = darajatFilter(request.GET, queryset=darajats)
    darajats =  filter.qs
    paginator = Paginator(darajats,200)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    context = {'darajat':page_pbj, 'filter':filter}
    return render(request, 'project/all_darajats.html', context)

@login_required
def darajat_detail(request, id,profile_id):
    darajat_detail = darajat.objects.filter(id=id, user=request.user,profile=profile_id)
    return render(request, 'project/darajat_detail.html', context={'darajat':darajat_detail})

@login_required
def Transports(request):
    Transports = Transport.objects.filter(user=request.user).order_by('date')
    filter = Transport_Filter(request.GET, queryset=Transports,request=request)
    Transports =  filter.qs
    paginator = Paginator(Transports,20)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    context = {'Transports':page_pbj, 'filter':filter, 'count':Transports.count()}
    return render(request, 'project/Transports.html', context)
@login_required
def staffs(request):
    staffs = Staff.objects.filter(user=request.user).order_by('add_date')
    filter = StaffFilter(request.GET, queryset=staffs,request=request)
    staffs = filter.qs
    paginator = Paginator(staffs,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/staffs.html', context ={'staffs':page_pbj,'filter':filter, 'count':staffs.count()})
# staff detail
@login_required
def staff_detail(request, id):
    staff_detail = Staff.objects.filter(id=id, user=request.user)
    return render(request, 'project/staff_detail.html', context={'staff':staff_detail})
# teacher absence
@login_required
def teacher_absence(request):
    teacher_absence = Teachers_absence.objects.filter(user=request.user).order_by('-add_date')
    filter = Teachers_absenceFilter(request.GET, queryset=teacher_absence,request=request)
    teacher_absence = filter.qs
    paginator = Paginator(teacher_absence,50)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/teacher_absence.html', context ={'teacher_absence':page_pbj,'filter':filter, 'count':teacher_absence.count()})
# teacher absence detail
@login_required
def teacher_absence_detail(request, id):
    teacher_absence_detail = Teachers_absence.objects.filter(id=id, user=request.user)
    return render(request, 'project/teacher_absence_detail.html', context={'teacher_absence':teacher_absence_detail})
# staff absence
@login_required
def staff_absence(request):
    staff_absence = Staff_absence.objects.filter(user=request.user).order_by('-add_date')
    filter = Staff_absenceFilter(request.GET, queryset=staff_absence,request=request)
    staff_absence = filter.qs
    paginator = Paginator(staff_absence,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request, 'project/staff_absence.html', context ={'staff_absence':page_pbj,'filter':filter, 'count':staff_absence.count()})
# staff absence detail
def staff_absence_detail(request, id):
    staff_absence_detail = Staff_absence.objects.filter(id=id, user=request.user)
    return render(request, 'project/staff_absence_detail.html', context={'staff_absence':staff_absence_detail})
@login_required
def all_month_exams(request):
    exams = Monthly_exams.objects.filter(user=request.user).order_by('-add_date')
    filter = Monthly_examsFilter(request.GET, queryset=exams)
    exams = filter.qs
    paginator = Paginator(exams,200)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    context = {'exams':page_pbj, 'filter':filter, 'count':exams.count()}
    return render(request, 'project/all_month_exams.html', context)
@login_required
#
def month_exams_detail(request, id):
    exams_detail = Monthly_exams.objects.filter(id=id, user=request.user)
    return render(request, 'project/month_exams_detail.html', context={'exams':exams_detail})

@login_required
def transports_detail(request, id):
    transports_detail = Transport.objects.filter(id=id, user=request.user)
    return render(request, 'project/transports_detail.html', context={'traansport':transports_detail})
@login_required
def add_boy(request):
    if request.method=='POST':
        form = boy_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:all_boys'))

    else:
        form = boy_form()
        form.fields['boy_class'].queryset = classes.objects.filter(user=request.user)
    return render(request, 'add/add_boy.html',{'form':form})
@login_required
def add_techer(request):
    if request.method=='POST':
        form = techer_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:techeres'))

    else:
        form = techer_form()
    return render(request, 'add/techer_form.html',{'form':form})

@login_required
def add_class(request):
    if request.method=='POST':
        form = class_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:class'))
    else:
        form = class_form()
        form.fields['techer'].queryset = techers.objects.filter(user=request.user)
    return render(request, 'add/class_form.html',{'form':form})

@login_required
def add_absence(request):
    boys = boy.objects.filter(user=request.user)
    if request.method=='POST':
        form = absence_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:absence'))
    else:
        form = absence_form()
        form.fields['name'].queryset = boy.objects.filter(user=request.user)
    return render(request, 'add/absence_form.html',{'form':form, 'boys':boys})

@login_required
def add_driver(request):
    if request.method=='POST':
        form = driver_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:driveres'))
    else:
        form = driver_form()
    return render(request, 'add/driver_form.html',{'form':form})

@login_required
def add_masrof(request):
    if request.method=='POST':
        form = masrof_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:masrofs'))
    else:
        form = masrof_form()
    return render(request, 'add/masrof_form.html',{'form':form})
@login_required
def add_mawad(request):
    if request.method=='POST':
        form = mawad_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:subjects'))
    else:
        form = mawad_form()
    return render(request, 'add/mawad_form.html',{'form':form})

@login_required
def new_darajat(request):
    if request.method == 'POST':
        form = darajat_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:darajats'))
    else:
        form = darajat_form()
        form.fields['name'].queryset = boy.objects.filter(user=request.user)
        form.fields['mada'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada1'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada2'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada3'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada4'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada5'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada6'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada7'].queryset = mawad.objects.filter(user=request.user)
    return render(request,'project/new_darajat.html',{'form':form})

@login_required
def add_month_darajat(request):
    if request.method == 'POST':
        form = month_darajat_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:darajats'))
    else:
        form = month_darajat_form()
        form.fields['name'].queryset = boy.objects.filter(user=request.user)
        form.fields['mada'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada1'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada2'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada3'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada4'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada5'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada6'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada7'].queryset = mawad.objects.filter(user=request.user)
    return render(request,'project/add_month_darajat.html',{'form':form})
# create new staff
@login_required
def add_staff(request):
    if request.method=='POST':
        form = staff_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:staffs'))
    else:
        form = staff_form()
    return render(request, 'add/staff_form.html',{'form':form})
# update staff
@login_required
def update_staff(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    if request.method == 'POST':
        form = staff_form(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:staffs'))
    else:
        form = staff_form(instance=staff)
    return render(request, 'edit/update_staff.html',{'form':form})
# new Staff_absence
@login_required
def add_staff_absence(request):
    if request.method=='POST':
        form = staff_absence_form(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:staff_absence'))
    else:
        form = staff_absence_form()
    return render(request, 'add/staff_absence_form.html',{'form':form})
# update staff absence
@login_required
def update_staff_absence(request, staff_absence_id):
    staff_absence = Staff_absence.objects.get(id=staff_absence_id)
    if request.method=='POST':
        form = staff_absence_form(request.POST,instance=staff_absence)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:staff_absence'))
    else:
        form = staff_absence_form(instance=staff_absence)
    return render(request, 'edit/update_staff_absence.html',{'form':form})
# new Teachers_absence
@login_required
def add_teachers_absence(request):
    if request.method=='POST':
        form = teacher_absence_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:teacher_absence'))
    else:
        form = teacher_absence_form()
        form.fields['teacher_name'].queryset = techers.objects.filter(user=request.user)
    return render(request, 'add/teachers_absence_form.html',{'form':form})
# update teacher absence
@login_required
def update_teachers_absence(request, id):
    my_absence = Teachers_absence.objects.get(id=id,user=request.user)
    if request.method == 'POST':
        form = teacher_absence_form(request.POST, instance=my_absence)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:teacher_absence'))
    else:
        form = teacher_absence_form(instance=my_absence)
        form.fields['teacher_name'].queryset = techers.objects.filter(user=request.user)
    return render(request, 'edit/teachers_absence_form.html',{'form':form})

@login_required
def add_transport(request):
    if request.method=='POST':
        form = Transport_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:Transports'))
    else:
        form = Transport_form()
        form.fields['driver'].queryset = driver.objects.filter(user=request.user)
    return render(request, 'add/transport_form.html',{'form':form})

@login_required
def paid(request):
    paid1 = boy.objects.filter(user=request.user).aggregate(Sum('paid'))
    paid =  paid1['paid__sum']
    paid2 = techers.objects.filter(user=request.user).aggregate(Sum('rateb'))
    rateb =  paid2['rateb__sum']
    paid3 = driver.objects.filter(user=request.user).aggregate(Sum('rateb'))
    rateb1 =  paid3['rateb__sum']
    paid4 = masrof.objects.filter(user=request.user).aggregate(Sum('price'))
    rateb2 =  paid4['price__sum']
    rebhs = rateb + rateb1 + rateb2
    rebh = paid - rebhs
    return render(request, 'paid.html', {'paid':paid,'rateb':rateb,'driver_rateb':rateb1,'masrof':rateb2,'rebh':rebh})
@login_required
def paid_chart(request):
    paid1 = boy.objects.filter(user=request.user)
    paids_bus = paid1.aggregate(Sum('price_of_bus'))
    the_bus = paids_bus['price_of_bus__sum']
    teacher = techers.objects.filter(user=request.user)
    drivers = driver.objects.filter(user=request.user)
    masrofs = masrof.objects.filter(user=request.user)
    paid4 = masrof.objects.filter(user=request.user).aggregate(Sum('price'))
    rateb2 =  paid4['price__sum']
    paid2 = techers.objects.filter(user=request.user).aggregate(Sum('rateb'))
    rateb =  paid2['rateb__sum']
    paid3 = driver.objects.filter(user=request.user).aggregate(Sum('rateb'))
    rateb1 =  paid3['rateb__sum']
    staffs = Staff.objects.filter(user=request.user)
    paid5 = staffs.aggregate(Sum('annual_salary'))
    rateb3 = paid5['annual_salary__sum']
    if rateb is not None and rateb1 is not None and rateb2 is not None:
        rebhs = rateb + rateb1 + rateb2
    elif rateb1 is not None and rateb2 is not None:
        rebhs =  rateb1 + rateb2
    elif rateb is not None and rateb2 is not None:
        rebhs = rateb  + rateb2
    elif rateb is not None and rateb1 is not None:
        rebhs = rateb + rateb1
    else:
        rebhs = 0
    paids = boy.objects.filter(user=request.user).aggregate(Sum('paid'))
    total =  paids['paid__sum']
    if the_bus is not None:
        total = total + the_bus
    if total is not None:
        profits = total - rebhs
    else:
        total = 0
        profits = total - rebhs
    context = {
        'boys':paid1,
        'techers':teacher,
        'drivers':drivers,
        'masrofs':masrofs,
        'total_masrofs':rateb2,
        'total_techers':rateb,
        'total_drivers':rateb1,
        'paids':rebhs,
        'total':total,
        'profits':profits,
        'the_bus':the_bus,
        'staffs':rateb3,
    }
    return render(request,'paid.html',context)
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request ,'profile.html', {'profile': profile})
@login_required
class BoyEdit(UpdateView):
    model = boy
    fields = ('name', 'age','boy_class','number_kawme','number_phone','image','paid',)
    template_name= 'edit/edit_boy.html'
    pk_url_kwarg= 'id'
    context_object_name = 'boy'
    def form_valid(self, form):
        boy = form.save(commit=False)
        boy.user = self.request.user
        boy.save()
        return redirect('app:all_boys')
@login_required
def edit_boy(request, id):
    boys = boy.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = boy_form(request.POST, request.FILES, instance=boys)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:all_boys'))

    else:
        form = boy_form(instance=boys)
        form.fields['boy_class'].queryset = classes.objects.filter(user=request.user)
    return render(request, 'edit/edit_boy.html',{'form':form})

@login_required
def edit_class(request, id):
    classe = classes.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = class_form(
            request.POST, request.FILES, instance=classe)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:class'))

    else:
        form = class_form(instance=classe)
        form.fields['techer'].queryset = techers.objects.filter(user=request.user)
    return render(request, 'edit/edit_class.html',{'form':form})

@login_required
def edit_techer(request,id):
    techer = techers.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = techer_form(request.POST, request.FILES, instance=techer)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:techeres'))

    else:
        form = techer_form(instance=techer)
    return render(request, 'edit/edit_teacher.html',{'form':form})

@login_required
def edit_absence(request,id):
    absences = absence.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = absence_form(request.POST, request.FILES, instance=absences)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:absence'))

    else:
        form = absence_form(instance=absences)
        form.fields['name'].queryset = boy.objects.filter(user=request.user)
    return render(request, 'edit/edit_absence.html',{'form':form})

@login_required
def edit_masrof(request,id):
    masrofs = masrof.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = masrof_form(request.POST, request.FILES, instance=masrofs)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:masrofs'))
    else:
        form = masrof_form(instance=masrofs)
    return render(request, 'edit/edit_masrof.html',{'form':form})

@login_required
def edit_driver(request,id):
    drivers = driver.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = driver_form(request.POST, request.FILES,instance=drivers)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.profile = request.user.profile
            myform.save()
            return redirect(reverse('app:driveres'))
    else:
        form = driver_form(instance=drivers)
    return render(request, 'edit/edit_driver.html',{'form':form})

@login_required
def edit_subject(request,id):
    subject = mawad.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = mawad_form(request.POST, request.FILES, instance=subject)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:techeres'))

    else:
        form = mawad_form(instance=subject)
    return render(request, 'edit/edit_subject.html',{'form':form})

@login_required
def edit_darajat(request,id):
    darajats = darajat.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = darajat_form(request.POST, request.FILES, instance=darajats)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:darajats'))

    else:
        form = darajat_form(instance=darajats)
        form.fields['name'].queryset = boy.objects.filter(user=request.user)
        form.fields['mada'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada1'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada2'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada3'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada4'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada5'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada6'].queryset = mawad.objects.filter(user=request.user)
        form.fields['mada7'].queryset = mawad.objects.filter(user=request.user)
    return render(request, 'edit/edit_darajat.html',{'form':form})

@login_required
def edit_transport(request,id):
    transportes = Transport.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = Transport_form(request.POST, request.FILES,instance=transportes)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('app:Transports'))
    else:
        form = Transport_form(instance=transportes)
        form.fields['driver'].queryset = driver.objects.filter(user=request.user)
    return render(request, 'edit/edit_transport.html',{'form':form})
@login_required
def delete_boy(request, id):
    boys = boy.objects.get(id=id, user=request.user)
    boys.delete()
    return redirect('app:all_boys')
@login_required
def delete_class(request, id):
    classe = classes.objects.get(id=id, user=request.user)
    classe.delete()
    return redirect('app:class')
@login_required
def delete_techer(request, id):
    techer = techers.objects.get(id=id, user=request.user)
    techer.delete()
    return redirect('app:techeres')
@login_required
def delete_absences(request, id):
    absences = absence.objects.get(id=id, user=request.user)
    absences.delete()
    return redirect('app:absence')
@login_required
def delete_subject(request, id):
    subject = mawad.objects.get(id=id, user=request.user)
    subject.delete()
    return redirect('app:subjects')
@login_required
def delete_driver(request, id):
    drivers = driver.objects.get(id=id, user=request.user)
    drivers.delete()
    return redirect('app:driveres')
@login_required
def delete_masrof(request, id):
    masrofs = masrof.objects.get(id=id, user=request.user)
    masrofs.delete()
    return redirect('app:masrofs')
@login_required
def delete_transport(request, id):
    delete_transport = Transport.objects.get(id=id, user=request.user)
    delete_transport.delete()
    return redirect('app:Transports')
@login_required
def delete_darajat(request, id):
    delete_darajat = darajat.objects.get(id=id, user=request.user)
    delete_darajat.delete()
    return redirect('app:darajats')
# delete staff
@login_required
def delete_staff(request, id):
    staff = Staff.objects.get(id=id, user=request.user)
    staff.delete()
    return redirect(reverse('app:staffs'))
#delete teacher_absence
@login_required
def delete_teacher_absence(request, id):
    teacher_absence = Teachers_absence.objects.get(id=id, user=request.user)
    teacher_absence.delete()
    return redirect(reverse('app:teacher_absence'))
#delete staff_absence
@login_required
def delete_staff_absence(request, id):
    staff_absence = get_object_or_404(Staff_absence,id=id,user=request.user)
    staff_absence.delete()
    return redirect(reverse('app:staff_absence'))
# delete Monthly_exams
@login_required
def delete_monthly_exams(request, id):
    monthly_exams = Monthly_exams.objects.get(id=id, user=request.user)
    monthly_exams.delete()
    return redirect(reverse('app:monthly_exams'))