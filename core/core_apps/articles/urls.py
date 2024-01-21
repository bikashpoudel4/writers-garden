from django.urls import path

from .views import ArticleListCreateView, ArticleRetriveUpdateDestroyView

urlpatterns = [
    path("", ArticleListCreateView.as_view(), name="article-list-create"),
    path("<uuid:id>/", ArticleRetriveUpdateDestroyView.as_view(), name="article-retrieve-update-destroy"),
]
