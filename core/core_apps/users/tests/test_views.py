import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core_apps.users.models import User
from core_apps.users.views import CustomUserDetailsView


@pytest.mark.django_db
def test_authentication_requiremet(normal_user):
    client = APIClient()
    url = reverse("user_details")
    response = client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user=normal_user)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_retrieve_user_details(normal_user):
    client = APIClient()
    client.force_authenticate(user=normal_user)
    url = reverse("user_details")

    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == normal_user.email
    assert response.data["first_name"] == normal_user.first_name
    assert response.data["last_name"] == normal_user.last_name


@pytest.mark.django_db
def test_update_details(normal_user):
    client = APIClient()
    client.force_authenticate(user=normal_user)
    url = reverse("user_details")

    new_first_name = "UpdatedFirstName"
    new_last_name = "UpdatedLastName"
    upated_data = {
        "first_name":new_first_name,
        "last_name":new_last_name
    }

    response = client.patch(url, upated_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["first_name"] == new_first_name
    assert response.data["last_name"] == new_last_name

    upated_user = User.objects.get(pk=normal_user.pk)
    assert upated_user.first_name == new_first_name
    assert upated_user.last_name == new_last_name


def test_get_queryset_empty(normal_user):
    client = APIClient()
    client.force_authenticate(user=normal_user)
    url = reverse("user_details")
    response = client.get(url)

    view = CustomUserDetailsView()
    view.request = response.wsgi_request

    queryset = view.get_queryset()

    assert queryset.count() == 0
    
# from django.test import RequestFactory

# def test_get_queryset_empt(normal_user):
#     client = APIClient()
#     client.force_authenticate(user=normal_user)
#     url = reverse("user_details")
#     response = client.get(url)

#     view = CustomUserDetailsView()

#     # Create a request instance using RequestFactory
#     request = RequestFactory().get(url)
#     request.user = normal_user  # Set the user for authentication
#     view.request = request

#     queryset = view.get_queryset()

#     assert queryset.count() == 0
