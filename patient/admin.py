from .models import Patient
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Patient
class PatientAdmin(UserAdmin):
    list_display = ['email', 'admin','name','gender','age']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2','gender','name','age')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()
    
admin.site.register(Patient,PatientAdmin)