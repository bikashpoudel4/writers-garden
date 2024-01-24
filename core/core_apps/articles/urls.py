from django.urls import path

from .views import (
    ArticleListCreateView,
    ArticleRetriveUpdateDestroyView,
    ClapArticleView,
)

urlpatterns = [
    path("", ArticleListCreateView.as_view(), name="article-list-create"),
    path(
        "<uuid:id>/",
        ArticleRetriveUpdateDestroyView.as_view(),
        name="article-retrieve-update-destroy",
    ),
    path("<uuid:article_id>/clap/", ClapArticleView.as_view(), name="clap-article"),
]
