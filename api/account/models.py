from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    '''
uidとprovider_idの複合ユニークにしている。
例えば、
1. ユーザーAがGoogleでログイン
2. ユーザーBがFacebookでログイン
このとき1,2は区別するという認識の実装
'''

    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    username = models.CharField('username', max_length=150, unique=True)
    email = models.EmailField('email address', null=True, default=None)
    # firebaseで渡されるuid
    uid = models.CharField('uid', max_length=191, null=True)
    # ソーシャルログインに使用したプロバイダ名
    provider_id = models.CharField('provider_id', max_length=50)
    # firebaseでanonymousかどうか
    is_firebase_anonymous = models.BooleanField(verbose_name='匿名', default=False)
    is_active = models.BooleanField(verbose_name='有効', default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'uid',
                    'provider_id'
                ],
                name='uid_provider_id'
            )
        ]

    def __str__(self):
        return self.username
