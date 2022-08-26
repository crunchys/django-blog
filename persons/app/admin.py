from django.contrib import admin
from django.utils.safestring import mark_safe

from app.models import *


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'bio')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'category', 'years_live', 'bio', 'photo', 'get_html_photo')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=40>")

    get_html_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Person, PersonAdmin)
admin.site.register(Category, CategoryAdmin)
