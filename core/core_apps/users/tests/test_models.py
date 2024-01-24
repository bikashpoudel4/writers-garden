import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_normal_user(normal_user):
    assert normal_user.first_name
    assert normal_user.last_name
    assert normal_user.email
    assert normal_user.password
    assert normal_user.pkid
    assert not normal_user.is_staff
    assert not normal_user.is_superuser
    assert normal_user.is_active


@pytest.mark.django_db
def test_create_superuser(super_user):
    assert super_user.first_name
    assert super_user.last_name
    assert super_user.email
    assert super_user.password
    assert super_user.pkid
    assert super_user.is_staff
    assert super_user.is_superuser
    assert super_user.is_active


@pytest.mark.django_db
def test_get_full_name(normal_user):
    full_name = normal_user.get_full_name()
    expected_full_name = f"{normal_user.first_name.title()} {normal_user.last_name.title()}"
    assert full_name == expected_full_name

@pytest.mark.django_db
def test_get_short_name(normal_user):
    short_name = normal_user.get_short_name()
    assert short_name == normal_user.first_name


@pytest.mark.django_db
def test_update_user(normal_user):
    new_first_name = "John"
    new_last_name = "Doe"
    normal_user.first_name = new_first_name
    normal_user.last_name = new_last_name
    normal_user.save()

    update_user = User.objects.get(pk=normal_user.pk)
    assert update_user.first_name == new_first_name
    assert update_user.last_name == new_last_name


@pytest.mark.django_db
def test_delete_user(normal_user):
    user_pk = normal_user.pk
    normal_user.delete()

    with pytest.raises(User.DoesNotExist):
        User.objects.get(pk=user_pk)


@pytest.mark.django_db
def test_user_str(normal_user):
    user_str = str(normal_user)
    assert user_str == f"{normal_user.first_name}"


@pytest.mark.django_db
def test_normal_user_email_is_normalized(normal_user):
    email = normal_user.email
    assert email == email.lower()


@pytest.mark.django_db
def test_super_user_email_is_normalized(super_user):
    email = super_user.email
    assert email == email.lower()


@pytest.mark.django_db
def test_user_email_incorrect(user_factory):
    with pytest.raises(ValueError, match="You must provide a valid email address."):
        user_factory.create(email="saras.soft@gmail.com")


@pytest.mark.django_db
def test_create_user_with_no_firstname(user_factory):
    with pytest.raises(ValueError, match="Users must have a first name."):
        user_factory.create(first_name=None)


@pytest.mark.django_db
def test_create_user_with_no_lastname(user_factory):
    with pytest.raises(ValueError, match="Users must have a last name."):
        user_factory.create(last_name=None)


@pytest.mark.django_db
def test_create_user_with_no_email(user_factory):
    with pytest.raises(ValueError, match="Users must have an email."):
        user_factory.create(email=None)


@pytest.mark.django_db
def test_create_superuser_with_no_email(user_factory):
    with pytest.raises(ValueError, match="Superuser must have an email address."):
        user_factory.create(email=None, is_superuser=True, is_staff=True)


@pytest.mark.django_db
def test_create_superuser_with_no_password(user_factory):
    with pytest.raises(ValueError, match="Superuser must have a password."):
        user_factory.create(password=None, is_superuser=True, is_staff=True)


@pytest.mark.django_db
def test_super_user_is_not_staff(user_factory):
    with pytest.raises(ValueError, match="Superuser must have is_staff=True."):
        user_factory.create(is_superuser=True, is_staff=False)


@pytest.mark.django_db
def test_super_user_is_not_superuser(user_factory):
    with pytest.raises(ValueError, match="Superuser must have is_superuser=True."):
        user_factory.create(is_superuser=False, is_staff=True)
