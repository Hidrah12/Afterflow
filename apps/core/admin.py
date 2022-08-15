from django.contrib import admin
from .models import Subcategory, Category, TypeCategory, Article, Cover

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

class TypeCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'minute_of_reading', 
    'category_for_development', 'publication_date', 'last_modification']
    list_display_links = ['id', 'title']
    list_filter = ['category']

admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TypeCategory, TypeCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Cover)