import factory
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from faker import Factory as FakerFactory

faker = FakerFactory.create()

User = get_user_model()


# @factory.django.mute_signals(post_save)
# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     first_name = factory.lazyAttribute(lambda x: faker.first_name())
#     last_name = factory.lazyAttribute(lambda x: faker.last_name())
#     email = factory.lazyAttribute(lambda x: faker.email())
#     password = factory.lazyAttribute(lambda x: faker.password())
#     is_active = True
#     is_staff = False

#     @classmethod
#     def _create(cls, model_class, *args, **kwargs):
#         manager = cls._get_manager(model_class)
#         if "is_superuser" in kwargs:
#             return manager.create_superuser(*args, **kwargs)
#         else:
#             return manager.create_user(*args, **kwargs)



@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
    is_active = True
    is_staff = False

    @classmethod
    def create_superuser(cls, *args, **kwargs):
        manager = cls._get_manager(User)
        return manager.create_superuser(*args, **kwargs)
    
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        if "email" in kwargs and not cls._is_valid_email(kwargs["email"]):
            raise ValueError("You must provide a valid email address.")
        return super()._create(model_class, *args, **kwargs)

    @staticmethod
    def _is_valid_email(email):
        # Simple validation: Check if the email contains "@"
        return "@" in email
