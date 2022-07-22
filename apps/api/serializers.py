from rest_framework import serializers
from apps.core.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'category_for_development',
            'summary', 'publication_date', 'template_name']
