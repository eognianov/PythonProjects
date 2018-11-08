from blog_app.models import Article
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import  PostArticleApoFrom


@csrf_exempt
def article(request):
    if request.method =='GET':
        a = Article.objects.all()
        data = [{'pk': a.pk, 'title': a.title, 'content': a.content}for a in Article.objects.all()]
        return JsonResponse(data, status=200, safe=False)
    elif request.method == 'POST':
        data = dict(request.POST)
        fields = ['content', 'tile']

        form = PostArticleApoFrom(data=data)
        if not form.is_valid():
            return JsonResponse(data={'error': form.errors}, status=400)

        article = Article.objects.create(**data)
        return JsonResponse(data={'pk': article.pk}, status=200)
