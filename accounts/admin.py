from django.contrib import admin
from .models import User
# Register your models here.



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_active',)
    list_filter = ('email', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'user_type', 'first_name', 'last_name', 'image')}),
        ('Permissions', {'fields': ('is_active', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'user_type', 'first_name', 'last_name', 'image')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)





admin.site.register(User, CustomUserAdmin)
