from ..models import Account
from config.utils import randomStrig
from rest_framework.exceptions import APIException


class AccountService():

    def get_account(self, uid, provider_id):

        try:
            account = Account.objects.get(
                uid=uid,
                provider_id=provider_id
            )
            return account
        except Exception:
            return None

    def create_anonymous_account(self, uid):
        random_username = randomStrig(12)

        try:
            account = Account.objects.create(
                uid=uid,
                username=random_username,
                is_firebase_anonymous=True,
            )
            return account
        except Exception:
            # すでに作成済み
            return None

    def create_loged_in_account(self, uid, provider_id, email):
        random_username = randomStrig(12)

        try:
            account = Account.objects.create(
                uid=uid,
                username=random_username,
                provider_id=provider_id,
                is_firebase_anonymous=False,
                email=email,
            )
            return account
        except Exception as e:
            print(e)
            # すでに作成済み
            raise None
