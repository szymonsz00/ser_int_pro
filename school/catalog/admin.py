from django.contrib import admin

# Register your models here.

from .models import Subject, Teacher, Information, Language

admin.site.register(Subject)
admin.site.register(Language)


class InformationInline(admin.TabularInline):
    model = Information


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'display_subject')
    inlines = [InformationInline]


admin.site.register(Teacher, TeacherAdmin)

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'status', 'student', 'to_date', 'id')
    list_filter = ('status', 'to_date')

    fieldsets = (
        (None, {
            'fields': ('teacher', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'to_date', 'student')
        }),
    )