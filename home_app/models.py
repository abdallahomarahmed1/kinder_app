# from typing import Reversible
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime
# Create your models here.
kind_of_Transport = {
    ('اتوبيس','اتوبيس'),
    ('سيارة','سيارة'),
    ('تكتك', 'تكتك'),
    ('ميكروباس','ميكروباس'),
}

Semester = {
    ('first','الفصل الدراسي الاول'),
    ('second','الفصل الدراسي الثاني'),
}
academic_years = {
    ('2021','2021-2022'),
    ('2022','2022-2023'),
    ('2023','2023-2024'),
    ('2024','2024-2025'),
}
kinds = {
    ('ذكر','ذكر'),
    ('انثى','انثى'),
}
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name="اسم الروضة", blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name="العنوان", blank=True, null=True)
    name_of_admin = models.CharField(max_length=50, verbose_name="اسم المشرف", blank=True, null=True)
    phone_number = models.IntegerField(verbose_name="رقم الهاتف", blank=True, null=True)
    img = models.ImageField(upload_to="user_img/", verbose_name="شعار الروضة", blank=True, null=True)
    working_months = models.IntegerField(verbose_name="عدد اشهر العمل", blank=True, null=True)
    year_expenses = models.IntegerField(verbose_name="سعر الاشتراك السنوي", blank=True, null=True)
    semester = models.CharField(max_length=50, choices=Semester, verbose_name="الفصل الدراسي")

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
class boy(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="الاسم")
    age = models.IntegerField(verbose_name="السن",null=True,blank=True, default=0)
    boy_class = models.ForeignKey("classes", verbose_name=("الفصل"), on_delete=models.PROTECT)
    number_kawme = models.IntegerField(verbose_name="الرقم القومي", blank=True, null=True)
    number_phone = models.IntegerField(verbose_name="رقم ولي الامر", blank=True, null=True)
    other_number = models.IntegerField(verbose_name="رقم أخر", blank=True, null=True)
    image = models.ImageField(upload_to="boys_images/", verbose_name="صورة الطفل", blank=True, null=True)
    Date_of_Birth = models.DateField(verbose_name="تاريخ الميلاد",null=True)
    bus_subscriber = models.BooleanField(verbose_name="مشترك بالاتوبيس", default=False)
    price_of_bus = models.IntegerField(verbose_name="سعر اشتراك الاتوبيس", default=0)
    addres = models.CharField(max_length=50, verbose_name="العنوان", blank=True, null=True)
    kind = models.CharField(max_length=50, choices=kinds, verbose_name="النوع",default='1')
    allergy = models.BooleanField(verbose_name="لديه حساسية", default=False,blank=True)
    sick = models.BooleanField(verbose_name="يعناي الطفل من امراض اخرى", default=False,blank=True)
    kind_of_sick = models.CharField(max_length=50, verbose_name="المرض", blank=True, null=True)
    paid = models.IntegerField(verbose_name='المبلغ المدفوع')
    Remaining_amount = models.IntegerField(verbose_name='المبلغ المتبقي', blank=True, null=True)
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    paids = models.BooleanField(verbose_name="تم الدفع", null=True, default=False)
    year = models.CharField(max_length=50,choices=academic_years,blank=True,null=True)
    add_date = models.DateField(auto_now=False,auto_now_add=False,verbose_name="التاريخ",null=True,blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.profile.year_expenses:
            self.Remaining_amount = self.profile.year_expenses - self.paid
        self.semester = self.profile.semester
        if self.add_date is None:
            self.add_date = timezone.now()
        self.year = self.add_date.year
        self.age = datetime.now().year - self.Date_of_Birth.year
        if self.Remaining_amount == 0:
            self.paids = True
        else:
            self.paids = False
        return super().save(*args, **kwargs)

class classes(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="اسم الفصل")
    techer = models.ForeignKey("techers", verbose_name=("المعلمة"), on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    year = models.CharField(max_length=50,choices=academic_years,blank=True,null=True)
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)

    def __str__(self):
        return self.name
    def nesba(self):
        return darajat.objects.filter(name__boy_class=self)
    def all_darajat(self):
        draja = darajat.objects.filter(name__boy_class=self).aggregate(Sum('ejamly_darajat'))
        return draja['ejamly_darajat__sum']
    def all_total(self):
        draja = darajat.objects.filter(name__boy_class=self).aggregate(Sum('ejamly_total'))
        return draja['ejamly_total__sum']
    def get_nesba(self):
        return (self.all_darajat() / self.all_total()) * 100
    def save(self, *args, **kwargs):
        if self.add_date is None:
            self.add_date = timezone.now()
        self.year = self.add_date.year
        return super().save(*args, **kwargs)
class techers(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="الاسم")
    age = models.IntegerField(verbose_name="السن")
    qualification = models.CharField(max_length=50, verbose_name="المؤهل")
    number_kawme = models.IntegerField(verbose_name="الرقم القومي")
    Salary = models.IntegerField(verbose_name="المرتب الشهري")
    number_phone = models.IntegerField(verbose_name="رقم هاتف المعلمة")
    rateb = models.IntegerField(verbose_name="الراتب السنوي", null=True ,blank=True)
    Reward = models.IntegerField(verbose_name="المكافأة السنوية", null=True ,blank=True)
    year = models.CharField(max_length=50,choices=academic_years,blank=True,null=True)
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)
    def save(self, *args, **kwargs):
        if self.profile.working_months:
            self.rateb = self.Salary * self.profile.working_months
        if self.add_date is None:
            self.add_date = timezone.now()
        self.year = self.add_date.year
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'techers'

class absence(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, verbose_name=("المستخدم"), on_delete=models.CASCADE,blank=True,null=True)
    name = models.ForeignKey("boy", verbose_name="الاسم", on_delete=models.CASCADE)
    excuse = models.BooleanField(default=True, verbose_name=("بعذر ام لا"))
    semester = models.CharField(max_length=50, choices=Semester, verbose_name="الفصل الدراسي", blank=True, null=True)
    year = models.CharField(max_length=50,choices=academic_years,blank=True,null=True)
    created = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = ("absence")
        verbose_name_plural = ("absences")


    def save(self, *args, **kwargs):
        self.semester = self.profile.semester
        if self.add_date is None:
            self.add_date = timezone.now()
        self.year = self.add_date.year
        return super().save(*args, **kwargs)

class Transport(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    kind = models.CharField(max_length=50, choices=kind_of_Transport, verbose_name=("نوع وسيلة النقل"))
    driver = models.OneToOneField("driver", verbose_name=("السائق"), on_delete=models.CASCADE)
    number = models.CharField(max_length=20, verbose_name="الرقم التعريفي")
    year = models.CharField(max_length=50,choices=academic_years,blank=True,null=True)
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)
    class Meta:
        verbose_name = ("Transport")
        verbose_name_plural = ("Transports")

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        if self.add_date is None:
            self.add_date = timezone.now()
        self.year = self.add_date.year
        return super().save(*args, **kwargs)

class driver(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="الاسم")
    number_kawme = models.IntegerField(verbose_name="الرقم القومي")
    number_phone = models.IntegerField(verbose_name="رقم الهاتف")
    Salary = models.IntegerField(verbose_name="المرتب الشهري")
    image = models.ImageField(upload_to="boys_images/", verbose_name="صورة السائق", blank=True, null=True)
    rateb = models.IntegerField(verbose_name="الراتب السنوي", null=True ,blank=True)
    year = models.CharField(max_length=50,choices=academic_years,blank=True,null=True)
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)
    def save(self, *args, **kwargs):
        if self.profile.working_months:
            self.rateb = self.Salary * self.profile.working_months
        if self.add_date is None:
            self.add_date = timezone.now()
        self.year = self.add_date.year
        return super().save(*args, **kwargs)
    def __str__(self):
       return self.name

    class Meta:
        verbose_name = 'driver'
        verbose_name_plural = 'drivers'
class masrof(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, verbose_name=("المستخدم"), on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50, verbose_name="المصروف")
    price = models.IntegerField(verbose_name="السعر")
    year = models.CharField(max_length=50,choices=academic_years,blank=True,null=True)
    date = models.DateTimeField(auto_now=True, verbose_name="التاريخ")
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)
    class Meta:
        verbose_name = ("masrof")
        verbose_name_plural = ("masrofs")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.add_date is None:
            self.add_date = timezone.now()
        self.year = self.add_date.year
        return super().save(*args, **kwargs)
class mawad(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='اسم المادة')
    daraja = models.IntegerField(verbose_name='الدرجة النهائية')
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.date is None:
            self.date = timezone.now()
        return super().save(*args, **kwargs)

class darajat(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, verbose_name=("profile"), on_delete=models.CASCADE)
    name = models.ForeignKey(boy, verbose_name=("اسم الطالب"), on_delete=models.CASCADE, null=True)
    mada = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE)
    daraja = models.IntegerField(verbose_name='درجة الطالب')
    mada1 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada1')
    daraja1 = models.IntegerField(verbose_name='درجة الطالب')
    mada2 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada2')
    daraja2 = models.IntegerField(verbose_name='درجة الطالب')
    mada3 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada3')
    daraja3 = models.IntegerField(verbose_name='درجة الطالب')
    mada4 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada4',null=True,blank=True)
    daraja4 = models.IntegerField(verbose_name='درجة الطالب' ,null=True, default='0')
    mada5 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada5',null=True,blank=True)
    daraja5 = models.IntegerField(verbose_name='درجة الطالب' ,null=True, default='0')
    mada6 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada6',null=True,blank=True)
    daraja6 = models.IntegerField(verbose_name='درجة الطالب',null=True, default='0')
    mada7 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='mada7',null=True,blank=True)
    daraja7 = models.IntegerField(verbose_name='درجة الطالب',null=True, default='0')
    nesba = models.IntegerField(blank=True,null=True)
    ejamly_darajat = models.IntegerField(blank=True,null=True)
    ejamly_total = models.IntegerField(blank=True,null=True)
    semester = models.CharField(max_length=50, choices=Semester, verbose_name="الفصل الدراسي", blank=True, null=True)
    year = models.CharField(max_length=50,choices=academic_years,blank=True,null=True)
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)

    def save(self, *args, **kwargs):
        total_ejmale = self.mada.daraja + self.mada1.daraja + self.mada2.daraja + self.mada3.daraja
        if self.mada4:
            total_ejmale += self.mada4.daraja
        if self.mada5:
            total_ejmale += self.mada5.daraja
        if self.mada6:
           total_ejmale += self.mada6.daraja
        self.ejamly_total = total_ejmale
        ejmale = self.daraja + self.daraja1 + self.daraja2 +self.daraja3
        if self.daraja4:
            ejmale += self.daraja4
        if self.daraja5:
            ejmale += self.daraja5
        if self.daraja6:
            ejmale += self.daraja6
        if self.daraja7:
            ejmale += self.daraja7
        self.ejamly_darajat = ejmale
        total = self.ejamly_total
        self.nesba = (100 * self.ejamly_darajat) / total
        self.semester = self.profile.semester
        if self.add_date is None:
            self.add_date = timezone.now()
        self.year = self.add_date.year
        return super().save(*args, **kwargs)
    def __str__(self):
        return str(self.name)


the_months = {
    ('1', 'يناير'),
    ('2', 'فبراير'),
    ('3', 'مارس'),
    ('4', 'أبريل'),
    ('5', 'مايو'),
    ('6', 'يونيو'),
    ('7', 'يوليو'),
    ('8', 'أغسطس'),
    ('9', 'سبتمبر'),
    ('10', 'أكتوبر'),
    ('11', 'نوفمبر'),
    ('12', 'ديسمبر'),
}
class Monthly_exams(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.ForeignKey(boy,on_delete=models.CASCADE,verbose_name='الاسم')
    month = models.CharField(max_length=50,choices=the_months,blank=True,null=True)
    year = models.CharField(max_length=50,choices=academic_years,blank=True,null=True)
    name = models.ForeignKey(boy, verbose_name=("اسم الطالب"), on_delete=models.CASCADE, null=True)
    mada = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE)
    daraja = models.IntegerField(verbose_name='درجة الطالب')
    mada1 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='month_mada1')
    daraja1 = models.IntegerField(verbose_name='درجة الطالب')
    mada2 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='month_mada2')
    daraja2 = models.IntegerField(verbose_name='درجة الطالب')
    mada3 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='month_mada3')
    daraja3 = models.IntegerField(verbose_name='درجة الطالب')
    mada4 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='month_mada4',null=True,blank=True)
    daraja4 = models.IntegerField(verbose_name='درجة الطالب' ,blank=True,null=True, default='0')
    mada5 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='month_mada5',null=True,blank=True)
    daraja5 = models.IntegerField(verbose_name='درجة الطالب' ,blank=True,null=True, default='0')
    mada6 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='month_mada6',null=True,blank=True)
    daraja6 = models.IntegerField(verbose_name='درجة الطالب',blank=True,null=True, default='0')
    mada7 = models.ForeignKey(mawad, verbose_name=("المادة"), on_delete=models.CASCADE,related_name='month_mada7',null=True,blank=True)
    daraja7 = models.IntegerField(verbose_name='درجة الطالب',blank=True,null=True, default='0')
    nesba = models.IntegerField(blank=True,null=True)
    ejamly_darajat = models.IntegerField(blank=True,null=True)
    ejamly_total = models.IntegerField(blank=True,null=True)
    semester = models.CharField(max_length=50, choices=Semester, verbose_name="الفصل الدراسي", blank=True, null=True)
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)

    def save(self, *args, **kwargs):
        total_ejmale = self.mada.daraja + self.mada1.daraja + self.mada2.daraja + self.mada3.daraja
        if self.mada4:
            total_ejmale += self.mada4.daraja
        if self.mada5:
            total_ejmale += self.mada5.daraja
        if self.mada6:
           total_ejmale += self.mada6.daraja
        self.ejamly_total = total_ejmale
        ejmale = self.daraja + self.daraja1 + self.daraja2 +self.daraja3
        if self.daraja4:
            ejmale += self.daraja4
        if self.daraja5:
            ejmale += self.daraja5
        if self.daraja6:
            ejmale += self.daraja6
        if self.daraja7:
            ejmale += self.daraja7
        self.ejamly_darajat = ejmale
        total = self.ejamly_total
        self.nesba = (100 * self.ejamly_darajat) / total
        if self.add_date is None:
            self.add_date = timezone.now()
        self.month = self.add_date.month
        self.year = self.add_date.year
        self.semester = self.profile.semester
        return super().save(*args, **kwargs)
    def __str__(self):
        return str(self.name)
class Teachers_absence(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    month = models.CharField(max_length=50,choices=the_months,blank=True,null=True)
    year = models.CharField(max_length=50,choices=academic_years,blank=True,null=True)
    teacher_name = models.ForeignKey(techers, verbose_name=("اسم المدرس"), on_delete=models.CASCADE, null=True)
    excuse = models.BooleanField(default=False,verbose_name='بعذر')
    the_reason = models.CharField(max_length=50,verbose_name='السبب',blank=True,null=True)
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)

    def save(self, *args, **kwargs):
        if self.add_date is None:
            self.add_date = timezone.now()
        self.month = self.add_date.month
        self.year = self.add_date.year
        return super().save(*args, **kwargs)
    def __str__(self):
        return str(self.teacher_name)

class Staff(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name=("اسم الموظف"),blank=True, null=True)
    age = models.IntegerField(verbose_name="السن",null=True,blank=True, default=0)
    number_kawme = models.IntegerField(verbose_name="الرقم القومي", blank=True, null=True)
    number_phone = models.IntegerField(verbose_name="رقم الهاتف", blank=True, null=True)
    the_jop = models.CharField(max_length=50,verbose_name='الوظيفة')
    Monthly_Salary = models.IntegerField(verbose_name='المرتب الشهري',)
    annual_salary = models.IntegerField(verbose_name='المرتب السنوي',blank=True,null=True)
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)

    def save(self, *args, **kwargs):
        if self.add_date is None:
            self.add_date = timezone.now()
        self.annual_salary = self.Monthly_Salary * self.profile.working_months
        return super().save(*args, **kwargs)
    def __str__(self):
        return str(self.name)

class Staff_absence(models.Model):
    user = models.ForeignKey(User, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, verbose_name=("المستخدم"), on_delete=models.CASCADE)
    month = models.CharField(max_length=50,choices=the_months,blank=True,null=True)
    year = models.CharField(max_length=50,choices=academic_years,blank=True,null=True)
    staff_name = models.ForeignKey(Staff, verbose_name=("اسم الموظف"), on_delete=models.CASCADE,blank=True,null=True)
    excuse = models.BooleanField(default=False,verbose_name='بعذر')
    the_reason = models.CharField(max_length=50,verbose_name='السبب',blank=True,null=True)
    add_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="التاريخ",null=True,blank=True)

    def save(self, *args, **kwargs):
        if self.add_date is None:
            self.add_date = timezone.now()
        self.month = self.add_date.month
        self.year = self.add_date.year
        return super().save(*args, **kwargs)
    def __str__(self):
        return str(self.staff_name)
