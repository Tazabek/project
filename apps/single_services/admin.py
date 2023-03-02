from django.contrib import admin
from .models import *

class OtherServsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class OtherServsInline(admin.TabularInline):
    model = OtherServs
    extra = 1

class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 1

class SingleService1Admin(admin.ModelAdmin):
    inlines = [OtherServsInline ,CommentsInline]

class InculedesInline(admin.TabularInline):
    model = Includes
    extra = 1

class PlanAdmin(admin.ModelAdmin):
    inlines = [InculedesInline]

class ContactsInline(admin.TabularInline):
    model = Contacts
    extra = 1

class SingleService2Admin(admin.ModelAdmin):
    inlines = [ContactsInline]


admin.site.register(SingleService1, SingleService1Admin)
admin.site.register(OtherServs, OtherServsAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(SingleService2, SingleService2Admin)

