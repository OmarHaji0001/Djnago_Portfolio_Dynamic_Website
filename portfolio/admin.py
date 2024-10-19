# portfolio/admin.py
from django.contrib import admin
from .models import PersonalInfo, Project, Skill, Experience, Testimonial, Banner


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'job_title')
    search_fields = ('fname', 'lname', 'email', 'job_title')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')
    search_fields = ('title', 'tech_stack')
    list_filter = ('date_added',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')
    search_fields = ('title', 'company')
    list_filter = ('start_date', 'end_date')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'date_given')
    search_fields = ('name', 'role')
    list_filter = ('date_given',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('page', 'alt_text')
    search_fields = ('page',)
