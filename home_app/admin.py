from django.contrib import admin
from .models import boy,classes,techers,absence,Transport,driver,masrof,Profile, mawad, darajat,Monthly_exams,Teachers_absence,Staff,Staff_absence
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.site_header = 'Proma'
admin.site.site_title = 'Proma'



class classs(ImportExportModelAdmin):
    pass
class techer(ImportExportModelAdmin):
    pass
class custom(ImportExportModelAdmin):
    pass
class Transports(ImportExportModelAdmin):
    pass
@admin.register(boy)
class boys(ImportExportModelAdmin):
    pass
admin.site.register(classes, classs)
admin.site.register(techers, techer)
admin.site.register(absence, custom)
admin.site.register(Transport, Transports)
admin.site.register(Monthly_exams)
admin.site.register(Staff_absence)
admin.site.register(Staff)
admin.site.register(Teachers_absence)

@admin.register(driver)
class drivers(ImportExportModelAdmin):
    pass
@admin.register(masrof)
class masrofs(ImportExportModelAdmin):
    pass
@admin.register(Profile)
class Profiles(ImportExportModelAdmin):
    pass
@admin.register(mawad)
class mawads(ImportExportModelAdmin):
    pass
@admin.register(darajat)
class darajats(ImportExportModelAdmin):
    pass
