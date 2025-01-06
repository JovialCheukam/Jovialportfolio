from django.contrib import admin

# Register your models here.

from .models import Home, About, Skill, Category, Profile, Portfolio



admin.site.register(Home)


# About

class ProfileInline(admin.TabularInline):
      
      model = Profile
      
      extra = 1
      
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
        ]


# Skills
class SkillsInline(admin.TabularInline):
      
      model = Skill
      
      extra = 2


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
        ]

# Portfolio
admin.site.register(Portfolio)

