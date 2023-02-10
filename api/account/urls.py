from django.urls import path
from account.views import account

app_name = 'accounts'
urlpatterns = [
    path('', account.ListView.as_view(), name='account_list')
]
