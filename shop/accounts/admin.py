from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    list_display = ('full_name','email','is_admin')
    list_filter = ('is_admin',)
    search_fields = ('email',)
    ordering = ('id',)
    filter_horizontal = ()
    
    form = UserChangeForm
    fieldsets = (
        (None, {'field':('full_name','email','password')}) ,
        ('Status', {'field':('is_active',)}) ,
        ('Permissions', {'field':('is_admin',)}) ,
    )

    add_form = UserCreationForm
    fieldsets = (
        (None, {'field':('full_name','email','password1','password2')}) ,
    )




admin.site.register()
admin.site.unregister(Group)







