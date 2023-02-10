from django.test import TestCase
from .factory import (
    AccountAnonymousFactory,
    AccountLogedInFactory
)
from ..services.account import AccountService
from ..models import Account


class AccountTest(TestCase):

    @classmethod
    def setUp(self):
        print('account test setup')
        self.anonymous_account = AccountAnonymousFactory.create()
        self.loged_in_account = AccountLogedInFactory.create()

    def test_create_anonymous_account(self):
        manual_uid = 'test'
        anonymous = AccountService().create_anonymous_account(manual_uid)
        self.assertEqual(anonymous.uid, manual_uid)
        self.assertTrue(anonymous.is_firebase_anonymous)

        # 一度使われたことのあるuidが再度実行できないことのテスト
        account = Account.objects.first()
        uid = account.uid
        anonymous_cant_create = AccountService().create_anonymous_account(uid)
        self.assertIsNone(anonymous_cant_create)

    def test_create_loged_in_account(self):
        manual_uid = 'logedIn'
        manual_email = 'logedIn@test.com'
        manual_provider = 'google'

        loged_in = AccountService().create_loged_in_account(
            manual_uid,
            manual_provider,
            manual_email
        )
        self.assertEqual(loged_in.uid, manual_uid)
        self.assertFalse(loged_in.is_firebase_anonymous)

        # 同じuidでprovider_idが違うときに作成できるかのテスト
        manual_uid = 'logedIn'
        manual_email = 'logedIn@test.com'
        manual_provider = 'Facebook'

        loged_in2 = AccountService().create_loged_in_account(
            manual_uid,
            manual_provider,
            manual_email
        )
        self.assertIsNotNone(loged_in2)
