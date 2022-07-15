from django import forms
import django_filters
from .models import boy,classes,techers,absence,Transport,driver,masrof,Profile, mawad,darajat,Monthly_exams,Staff,Staff_absence,Teachers_absence,Staff,Staff_absence,Teachers_absence
# from .views import custom_filter
def custom_boy_filter(request):
    return boy.objects.filter(user=request.user)
def custom_filter_class(request):
    return classes.objects.filter(user=request.user)

def custom_filter_teacher(request):
    return techers.objects.filter(user=request.user)

def custom_filter_driver(request):
    return driver.objects.filter(user=request.user)
def teachers(request):
    return techers.objects.filter(user=request.user)
def staffs(request):
    return Staff.objects.filter(user=request.user)

class BoyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',lookup_expr='icontains',label='الإسم:')
    boy_class = django_filters.ModelMultipleChoiceFilter(queryset=custom_filter_class,
        widget= forms.CheckboxSelectMultiple()
    )
    class Meta:
        model = boy
        fields = ['name', 'age', 'boy_class', 'number_kawme', 'number_phone','paid','Remaining_amount','paids','kind','allergy']

class classFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='الإسم:')
    techer = django_filters.ModelChoiceFilter(queryset=custom_filter_teacher)
    class Meta:
        model = classes
        fields = ['name', 'techer']
class techersFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='الإسم:')
    class Meta:
        model = techers
        fields = ['name', 'age', 'qualification', 'number_kawme','Salary','number_phone']
class absenceFilter(django_filters.FilterSet):
    name = django_filters.ModelChoiceFilter(queryset=custom_boy_filter,label='الإسم:')
    created = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    class Meta:
        model = absence
        fields = ['name', 'excuse','created']
class masrofFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='الإسم:')
    class Meta:
        model = masrof
        fields = ['name', 'price']

class driverFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='الإسم:')
    class Meta:
        model = driver
        fields = ['name', 'number_kawme', 'number_phone', 'Salary']

class transportFilter(django_filters.FilterSet):
    driver = django_filters.CharFilter(lookup_expr='icontains',label='الإسم:')
    class Meta:
        model = Transport
        fields = ['kind', 'driver', 'number']

class mawadFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='الإسم:')
    # date = django_filters.DateFilter(widget=django_filters.(attrs={'type': 'date'}))
    class Meta:
        model = mawad
        fields = '__all__'
        exclude = ('user','date')

class darajatFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='الإسم:')
    class Meta:
        model = darajat
        fields = ['name']
class Transport_Filter(django_filters.FilterSet):
    driver = django_filters.ModelChoiceFilter(queryset=custom_filter_driver)
    class Meta:
        model = Transport
        fields = '__all__'
        exclude = ('user','date', 'add_date')

class StaffFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='الإسم:')
    class Meta:
        model = Staff
        fields = ['name', 'the_jop', 'Monthly_Salary', 'annual_salary']
# staff absence filter
class Staff_absenceFilter(django_filters.FilterSet):
    add_date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    staff_name = django_filters.ModelChoiceFilter(queryset=staffs,label='الإسم:')

    class Meta:
        model = Staff_absence
        fields = '__all__'
        exclude = ('user','profile','the_reason','year','month')
# teacher absence filter
class Teachers_absenceFilter(django_filters.FilterSet):
    teacher_name = django_filters.ModelChoiceFilter(queryset=teachers,label='الإسم:')
    add_date  = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    class Meta:
        model = Teachers_absence
        fields = '__all__'
        exclude = ('user','profile','the_reason','year','month')
class Monthly_examsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='الإسم:')
    class Meta:
        model = Monthly_exams
        fields = ['name', 'year']