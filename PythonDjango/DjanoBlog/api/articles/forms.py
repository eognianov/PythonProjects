from django.forms import ModelForm
from blog_app.models import Article


class PostArticleApoFrom(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')