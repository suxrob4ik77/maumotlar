from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','photo', 'context')
    list_display_links = ['title']
    search_fields = ['title']
    list_editable = ['title']


admin.site.register(News)
admin.site.register(Category)