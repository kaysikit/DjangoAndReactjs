from rest_framework import viewsets

from .serializers import BlogPostSerializer, BlogPostListRetrieveSerializer
from ..models import BlogCategory, BlogPost


class BlogCategoryViewSet(viewsets.ModelViewSet):

    queryset = BlogCategory.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    action_to_serializer= {
        "List": BlogPostListRetrieveSerializer,
        "retrieve": BlogPostListRetrieveSerializer
    }

    def get_serializer_class(self):
        return  self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )