from django.db import models

class Subcategory(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self) -> str:
        return f'{self.name}'

class TypeCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.name}'

class Category(models.Model):
    name = models.CharField(max_length = 30)
    subcategorys = models.ManyToManyField(Subcategory, blank = True)
    type_category = models.ForeignKey(TypeCategory, on_delete = models.PROTECT, null = True)

    def __str__(self) -> str:
        return f'{self.name}'

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null = True, blank = True, db_index = True)
    minute_of_reading = models.CharField(max_length=10, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    category_for_development = models.CharField('Category Development', max_length=30)
    summary = models.TextField()
    publication_date = models.DateTimeField(auto_now_add = True)
    last_modification = models.DateTimeField(auto_now = True)

    template_name = models.CharField(max_length = 50, null = True, blank = True)
    featured = models.BooleanField(null = True, blank = True)
    image = models.ImageField(upload_to = 'featured', null = True)
    
    def __str__(self) -> str:
        return f'{self.title}'

# 1 Django [Vistas, Templates, Forms, Models] framework
# 2 Python null language
# 3 MySQL null database
# 4 PostgreSQL null database