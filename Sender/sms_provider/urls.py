from django.urls import path
from sms_provider.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home')
]
