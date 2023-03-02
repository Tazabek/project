from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class CategoryPortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1
    readonly_fields = ('get_image',)
    prepopulated_fields = {'slug': ('name_on_image',)}

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}"')

class AdvertisementAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]

class ReviewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Slides)
admin.site.register(Block1)
admin.site.register(CategoryPortfolio, CategoryPortfolioAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Contacts)
admin.site.register(About)
admin.site.register(Posts)
