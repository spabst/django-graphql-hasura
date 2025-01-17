from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from api.models import profile, company

# Register your models here.
# Inline + descriptor
class AdminProfileInline(admin.StackedInline):
    model = profile
    can_delete = False
    verbose_name_plural = 'profiles'

# Register your models here.
# Inline + descriptor
class AdminCompanyInline(admin.StackedInline):
    model = company
    can_delete = False
    verbose_name_plural = 'companies'

# Define new admin with inline
class ProfileUserAdmin(BaseUserAdmin):
    inlines = (AdminProfileInline,AdminCompanyInline)



# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, ProfileUserAdmin,)

admin.site.site_header= "LumRisk Admin Page"