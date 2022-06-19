from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

from .models import Article
# Create your views here.
class ArticleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        articles = Article.objects.filter(user=user)
        titles = [article.title for article in articles]

        return Response({"article_list": titles})


