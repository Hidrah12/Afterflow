from .models import TypeCategory, Category, Cover

def get_categorys(request):
	all_types_of_categories = TypeCategory.objects.all()
	framework = all_types_of_categories.get(name = 'framework')
	database = all_types_of_categories.get(name = 'database')
	language = all_types_of_categories.get(name = 'language')
	tutorial = all_types_of_categories.get(name = 'tutorial')

	all_categorys = Category.objects.all()
	frameworks = all_categorys.filter(type_category = framework.id)
	databases = all_categorys.filter(type_category = database.id)
	languages = all_categorys.filter(type_category = language.id)
	tutorials = all_categorys.filter(type_category = tutorial.id)

	context_data = {
		'frameworks': frameworks,
		'databases': databases,
		'languages': languages,
		'tutorials': tutorials
	}
	
	return context_data

def get_image_cover(requets):
	image_ = Cover.objects.first()
	return {'image': image_}