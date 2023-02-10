import factory
from factory import Faker
from ..models import Account
from config.utils import randomStrig


class AccountAnonymousFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    is_firebase_anonymous = True
    uid = Faker('name')
    username = randomStrig(12)


class AccountLogedInFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    is_firebase_anonymous = False
    uid = Faker('name')
    username = randomStrig(12)
    email = 'a@test.jp'
    provider_id = 'google'
