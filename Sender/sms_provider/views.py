from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sms_provider.serializer import SmsProviderSerializer
from twilio.rest import Client

class Home(APIView):
    serializer_class = SmsProviderSerializer

    def get(self, request):
        return Response({'details': "SMS provider is working"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SmsProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data['phone'], serializer.data['text'])
            sendSMS(serializer.data['phone'], serializer.data['text'])
            return Response({"message": "Success! The SMS has been sent."}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def sendSMS(number, msg):
    print(number, msg)
    # client = Client("ssid", "auth token")
    client = Client("AC9d1e5f516b6a02ae71c93812c795df17", "96ff6cc87705475212c4c1fc0adb1b31")    
    # client.messages.create(to=[f"{number}"],
    client.messages.create(to=["+916280234712"],
        from_ = "+13202976065",
        body = f' {msg}'
    )