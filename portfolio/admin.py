from django.contrib import admin
from .models import UserProfile, Experience, Education, Certificate, Project, Skill, Language, About

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'pronouns', 'dob', 'district', 'state', 'open_to_work')
    list_filter = ('state', 'open_to_work')
    fieldsets = (
        ('Personal Info', {
            'fields': ('user', 'name', 'pronouns', 'dob', 'profile_picture')
        }),
        ('Location', {
            'fields': ('district', 'state', 'zip_code')
        }),
        ('Career', {
            'fields': ('open_to_work', 'resume', 'bio')
        }),
    )

class AboutAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'title')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'title', 'company', 'start_date', 'end_date')
    list_filter = ('title', 'company')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'degree', 'school_name', 'grade')

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'title', 'issued_by', 'issued_on')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'title', 'start_date', 'end_date')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'skill', 'proficiency')

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'language', 'proficiency')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Language, LanguageAdmin)
# Register your models here.
