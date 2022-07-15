from django import forms
from .models import boy,classes,techers,absence,Transport,driver,masrof, darajat, mawad,Monthly_exams,Staff,Staff_absence,Teachers_absence

class boy_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Date_of_Birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # boy_class = forms.ModelChoiceField()
    class Meta:
        model = boy
        fields = '__all__'
        exclude = ('user','profile','Remaining_amount','year','academic_year','paids','age')

class class_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = classes
        fields = '__all__'
        exclude = ('user','year')
class techer_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = techers
        fields = '__all__'
        exclude = ('user','profile','rateb','year',)

class absence_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = absence
        fields = '__all__'
        exclude = ('user','year','semester','year','profile')

class Transport_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Transport
        fields = '__all__'
        exclude = ('user',)

class driver_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = driver
        fields = '__all__'
        exclude = ('user','profile','rateb',)

class masrof_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = masrof
        fields = '__all__'
        exclude = ('user','profile','year')

class darajat_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = darajat
        fields = '__all__'
        exclude = ('user','profile','nesba','ejamly_darajat','ejamly_total','semester','year')

class mawad_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = mawad
        fields = '__all__'
        exclude = ('user','year')

class absence_search(forms.Form):
    serchname = forms.CharField(widget=forms.TextInput())
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # print('kgkgkgk____________________________________+++++++++++++++++++++')
class month_darajat_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Monthly_exams
        fields = '__all__'
        exclude = ('user','profile','nesba','ejamly_darajat','ejamly_total','month','year')

# staff form
class staff_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ('user','profile','annual_salary')
# staff absence form
class staff_absence_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Staff_absence
        fields = '__all__'
        exclude = ('user','profile','month','year')
# teacher absence form
class teacher_absence_form(forms.ModelForm):
    add_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Teachers_absence
        fields = '__all__'
        exclude = ('user','profile','month','year')