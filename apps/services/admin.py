from django.contrib import admin
from .models import *

class CategoryPortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class InculedesInline(admin.TabularInline):
    model = Includes
    extra = 1

class PlanAdmin(admin.ModelAdmin):
    inlines = [InculedesInline]


class IncludesServInline(admin.TabularInline):
    model = IncludesServ
    extra = 1

class Service5Admin(admin.ModelAdmin):
    inlines = [IncludesServInline]



admin.site.register(Service2)
admin.site.register(Service3)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Service5, Service5Admin)
admin.site.register(CategoryPortfolio, CategoryPortfolioAdmin)
