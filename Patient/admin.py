from django.contrib import admin

# Register your models here.
from .models import Genre, LookupRegion, LookupRajon, Patient

#admin.site.register(Genre)
# admin.site.register(Region)
# admin.site.register(Rajon)
# admin.site.register(patient)

# Register the Admin classes for Bosok using the decorator

@admin.register(LookupRegion)
class LookupRegionAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator

@admin.register(LookupRajon)
class LookupRajonAdmin(admin.ModelAdmin):
    list_display = ('rajons', 'region_id')
    list_filter = ['region_id']
    search_fields = ['rajons']


class PatientAdmin(admin.ModelAdmin):
  # form = MyPatientForm
   list_display = ('first_name', 'last_name', 'date_birthday','region_id', 'purpose_medical_examination')
   list_filter = ['last_name', 'first_name','region_id']
   search_fields = ['first_name']
   autocomplete_fields = ['rajon_id']
   # Register the admin class with the associated model

admin.site.register(Patient, PatientAdmin)

