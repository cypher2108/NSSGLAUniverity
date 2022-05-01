from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined',
                    'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', )
    readonly_fields = ('date_joined', 'last_login')

    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name' ,'password1', 'password2'),
        }),
    )

admin.site.register(Account, AccountAdmin)