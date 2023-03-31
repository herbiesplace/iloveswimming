from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Article, ArticleSeries, Contact

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
        'publish',
        'title',
        'subtitle',
        'slug',
        'author',
        'image',
        #'published',
    ]
 
class ArticleAdmin(admin.ModelAdmin):
    fieldsets =  [
        ("Header", {"fields": ['publish','title','subtitle','article_slug','series','author','image']}),
        ("Content", {"fields": ['content', "notes"]}),
        ("Date", {"fields": ['modified']})
    ]

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ("firstname","lastname","reden" )

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleSeries, ArticleSeriesAdmin)

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)
