from django.urls import path

from .views import RersponseListCreateView, ResponseUpdateDeleteView

urlpatterns = [
    path(
        "article/<uuid:article_id>/",
        RersponseListCreateView.as_view(),
        name="article_response",
    ),
    path("<uuid:id>/", ResponseUpdateDeleteView.as_view(), name="response_detail"),
]
