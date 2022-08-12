from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin

@admin.register(Organization)
class OrganizationAdminP(admin.ModelAdmin):
    list_display = ['name','logo','info','instagram','youtube','telegram','tel','tel2','tel3','mail','address']
    search_fields = ["name__icontains"]

@admin.register(ServiceType)
class ServiceTypeAdminP(admin.ModelAdmin):
    pass

# @admin.register(Service)
# class ServiceAdminP(admin.ModelAdmin):
#     pass


@admin.register(Service)
class ServiceAdminP(admin.ModelAdmin):
    list_display = ['name','info','type','status_name']
    search_fields = ["name__icontains"]

@admin.register(Partners)
class PartnersAdminP(admin.ModelAdmin):
    pass
@admin.register(Region)
class RegionAdminP(ImportExportModelAdmin):
    pass
@admin.register(District)
class DistrictAdminP(ImportExportModelAdmin):
    pass
@admin.register(Customer)
class CustomerAdminP(ImportExportModelAdmin):
    list_display=('id','name','inn')
    pass
@admin.register(Substation)
class SubstationAdminP(ImportExportModelAdmin):
    pass
@admin.register(Meter_type)
class Meter_typeAdminP(ImportExportModelAdmin):
    pass
@admin.register(Fider)
class FiderAdminP(ImportExportModelAdmin):
    pass
@admin.register(Agreement)
class AgreementAdminP(ImportExportModelAdmin):
    pass
@admin.register(Conn_agre)
class Conn_agreAdminP(ImportExportModelAdmin):
    pass
@admin.register(New)
class NewAdminP(ImportExportModelAdmin):
    pass

