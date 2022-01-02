from rest_framework import serializers
from sms_provider.models import SmsProvider

class SmsProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsProvider
        fields = '__all__'