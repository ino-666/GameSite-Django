from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Comment

class CustomUserAdmin(UserAdmin):
    # 追加するフィールドを指定
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('stage_cleart',)}),
    )
    # 変更するフィールドを指定
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('stage_cleart',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Comment)