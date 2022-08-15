from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Cover(models.Model):
    image = models.ImageField(upload_to='cover_images/', blank=True)

    def __str__(self) -> str:
        return f'{self.image}'
    
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

    def get_absolute_url(self):
        return reverse('core:articles-from-category', args=[self.name])

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null = True, blank = True, db_index = True, unique = True)
    minute_of_reading = models.CharField(max_length=10, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    category_for_development = models.CharField('Category Development', max_length=30)
    summary = models.TextField()
    publication_date = models.DateTimeField(auto_now_add = True)
    last_modification = models.DateTimeField(auto_now = True)
    template_name = models.CharField(max_length = 50, null = True, blank = True)
    featured = models.BooleanField(null = True, blank = True)
    main_image = models.ImageField(upload_to = 'article_image/', blank = True)
    
    def __str__(self) -> str:
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('core:articles-from-category', args=[self.category])

def create_slug(instance, new_slug = None):
    slug = slugify(instance.title)
    if new_slug != None:
        slug = new_slug
    article = Article.objects.filter(slug = slug).order_by('-id')
    if article.exists():
        new_slug = '%s-%s' % (slug, article.first().id)
        return create_slug(instance, new_slug = new_slug)
    return slug

def pre_save_article(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_article, sender = Article)

# 1 Django [Vistas, Templates, Forms, Models] framework
# 2 Python null language
# 3 MySQL null database
# 4 PostgreSQL null database