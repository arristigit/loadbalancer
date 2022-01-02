from django.urls import path
from sms_app.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home')
]
