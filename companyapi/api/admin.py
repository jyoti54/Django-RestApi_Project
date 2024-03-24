from django.contrib import admin
from .models import Company,Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','location','type')
    list_filter = ('location',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','company')
    search_fields = ('name',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)