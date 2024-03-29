from django.contrib import admin
from django.contrib import admin
from custom_user.forms import MyUserChangeForm, MyUserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'phone','first_name', 'last_name', 'email',
            'gender', "about","profile_photo","usr_id","usr_mod","usr_status","usr_premium_expire","usr_public","usr_lastip",
            "usr_pay_email","usr_pay_type","usr_disk_space","usr_direct_downloads","usr_rapid_login","usr_rapid_pass","usr_points","usr_aff_id",
            "usr_maritial","usr_sex","birthdate","webpage","education","workplace","usr_money","aboutme","moved")}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("first_name", "last_name", 'username', 'password1', 'password2'),
        }),
    )
    # The forms to add and change user instances
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('username','email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    ordering = ('-date_joined',)
    filter_horizontal = ('groups', 'user_permissions',)
# Register your models here.
