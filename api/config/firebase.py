from account.models import Account
from rest_framework import authentication
import firebase_admin.auth as auth


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')

        if not token:
            return None

        deceded_token = None
        try:
            deceded_token = auth.verify_id_token(token)
        except Exception:
            raise PermissionError("Invalid Token")

        if not token or not deceded_token:
            return None

        try:
            uid = deceded_token.get('uid')
            user_profile = auth.get_user(uid)
            provider_id = user_profile.provider_id
            email = user_profile.email

            # TODO: (get account)
            account = Account.objects.get(
                uid=uid,
                provider_id=provider_id
            )
            return account

        except Account.DoesNotExist:
            # TODO: (create account):
            print('account none')
            return None
        except Exception:
            return None
