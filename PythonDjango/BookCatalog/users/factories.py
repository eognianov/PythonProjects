from faker import Factory
from django.contrib.auth.models import User
import factory

faker = Factory.create()


class UserFactory(factory.DjangoModelFactory):
    username = factory.LazyAttribute(lambda user: '{}_{}@{}'.format(user.first_name, user.last_name, faker.domain_name))
    first_name = factory.LazyFunction(lambda: faker.first_name())
    last_name = factory.LazyFunction(lambda: faker.last_name())

    class Meta:
        model = User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        return model_class.objects.create_user(*args, **kwargs)
