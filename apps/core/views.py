from django.shortcuts import render
from .models import Category, TypeCategory, Article
from django.views.generic import ListView

def get_type_categorys():
    all_type_category = TypeCategory.objects.all()
    framework = all_type_category.get(name = 'framework')
    database = all_type_category.get(name = 'database')
    language = all_type_category.get(name = 'language')
    tutorial = all_type_category.get(name = 'tutorial')
    
    return (framework, database, language, tutorial)
    

def home_view(request):
    (framework, database, language, tutorial) = get_type_categorys()

    all_categorys = Category.objects.all()
    frameworks = all_categorys.filter(type_category = framework.id)
    databases = all_categorys.filter(type_category = database.id)
    languages = all_categorys.filter(type_category = language.id)
    tutorials = all_categorys.filter(type_category = tutorial.id)

    articles = Article.objects.all().order_by('-id')

    context_data = {
        'frameworks': frameworks, 
        'databases': databases,
        'languages': languages,
        'tutorials': tutorials,
        'articles': articles,
    }

    return render(request, 'index.html', context_data)

class HomeView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    (framework, database, language, tutorial) = get_type_categorys()

    all_categorys = Category.objects.all()
    frameworks = all_categorys.filter(type_category = framework.id)
    databases = all_categorys.filter(type_category = database.id)
    languages = all_categorys.filter(type_category = language.id)
    tutorials = all_categorys.filter(type_category = tutorial.id)

    extra_context = {
        'frameworks': frameworks, 
        'databases': databases,
        'languages': languages,
        'tutorials': tutorials,
    }
    def get_queryset(self):
        return Article.objects.all().order_by('-id')