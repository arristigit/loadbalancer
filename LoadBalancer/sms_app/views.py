from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sms_app.serializer import SmsSerializer
import pandas as pd
import requests


from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

class Home(APIView):
    serializer_class = SmsSerializer

    def get(self, request):
        return Response({'details': "Welcome to VARINDER's Load Balancer"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SmsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Getting the path and reading *.csv file using Pandas, which uploaded via API 
            file_path = os.path.join(BASE_DIR,  f"/0.Varinder/Technologies/Django/12_MyPaisaaa/loadbalancer/LoadBalancer{serializer.data['file']}")
            file = pd.read_csv(file_path) 
            
            loadBalancer(file)

            return Response({"message": "Success! The SMS has been created."}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def loadBalancer(file):
    print("Length of the file:", len(file))

    # Checking health of the SMS providers
    provider1, provider2, provider3 = CheckHealth()

    # All providers are healthy with equal throughput
    if provider1 and provider2 and provider3:
        print("Condition met:", 1, 1, 1)
        no_of_sms_per_provider = int(len(file) / 3)
        print("no_of_sms_per_provider:", no_of_sms_per_provider)

        for index in range(0, no_of_sms_per_provider):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider1(data)
            print("sms by provider 1")
            print(index, "=>", file['phone numbers'][index], file['text'][index])

        for index in range(no_of_sms_per_provider , no_of_sms_per_provider*2):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider2(data)
            print("sms by provider 2")
            print(index, "=>", file['phone numbers'][index], file['text'][index])

        for index in range(no_of_sms_per_provider*2, no_of_sms_per_provider*3):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider3(data)
            print("sms by provider 3")
            print(index, "=>", file['phone numbers'][index], file['text'][index])
    
    if provider1 and provider2 and provider3 == False:
        print("Condition met:", 1, 1, 0)
        no_of_sms_per_provider = int(len(file) / 2)
        print("no_of_sms_per_provider:", no_of_sms_per_provider)

        for index in range(0, no_of_sms_per_provider):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider1(data)
            print("sms by provider 1")
            print(index, "=>", file['phone numbers'][index], file['text'][index])

        for index in range(no_of_sms_per_provider , no_of_sms_per_provider*2):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider2(data)
            print("sms by provider 2")
            print(index, "=>", file['phone numbers'][index], file['text'][index])

    if provider1 and provider2 == False and provider3:
        print("Condition met:", 1, 0, 1)
        no_of_sms_per_provider = int(len(file) / 2)
        print("no_of_sms_per_provider:", no_of_sms_per_provider)

        for index in range(0, no_of_sms_per_provider):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider1(data)
            print("sms by provider 1")
            print(index, "=>", file['phone numbers'][index], file['text'][index])

        for index in range(no_of_sms_per_provider , no_of_sms_per_provider*2):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider3(data)
            print("sms by provider 3")
            print(index, "=>", file['phone numbers'][index], file['text'][index])

    if provider1 == False and provider2 and provider3:
        print("Condition met:", 0, 1, 1)
        no_of_sms_per_provider = int(len(file) / 2)
        print("no_of_sms_per_provider:", no_of_sms_per_provider)

        for index in range(0, no_of_sms_per_provider):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider2(data)
            print("sms by provider 2")
            print(index, "=>", file['phone numbers'][index], file['text'][index])

        for index in range(no_of_sms_per_provider , no_of_sms_per_provider*2):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider3(data)
            print("sms by provider 3")
            print(index, "=>", file['phone numbers'][index], file['text'][index])

    if provider1 and provider2 == False and provider3 == False:
        print("Condition met:", 1, 0, 0)
        print("no_of_sms_per_provider:", len(file))

        for index in range(0, len(file)):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider1(data)
            print("sms by provider 1")
            print(index, "=>", file['phone numbers'][index], file['text'][index])

    if provider1 == False and provider2 and provider3 == False:
        print("Condition met:", 0, 1, 0)
        print("no_of_sms_per_provider:", len(file))

        for index in range(0, len(file)):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider2(data)
            print("sms by provider 2")
            print(index, "=>", file['phone numbers'][index], file['text'][index])

    if provider1 == False and provider2 == False and provider3:
        print("Condition met:", 0, 0, 1)
        print("no_of_sms_per_provider:", len(file))

        for index in range(0, len(file)):
            data = {'phone': file['phone numbers'][index], 'text': file['text'][index]}
            postProvider3(data)
            print("sms by provider 3")
            print(index, "=>", file['phone numbers'][index], file['text'][index])

def CheckHealth():
    try: 
        req1 = requests.get('http://127.0.0.1:8001/sms/')
        if req1.status_code == 200:
            provider1 = True
        print("\nProvider-1 is healthy :)")
    except Exception as e:
        provider1 = False
        print("\nProvider-1 is unhealthy!")

    try: 
        req2 = requests.get('http://127.0.0.1:8002/sms/')
        if req2.status_code == 200:
            provider2 = True
        print("Provider-2 is healthy :)")
    except Exception as e:
        provider2 = False
        print("Provider-2 is unhealthy!")

    try: 
        req3 = requests.get('http://127.0.0.1:8003/sms/')
        if req3.status_code == 200:
            provider3 = True
        print("Provider-3 is healthy :)\n")
    except Exception as e:
        provider3 = False
        print("Provider-3 is unhealthy!\n")
    
    return (provider1, provider2, provider3)

def postProvider1(data):
    url = 'http://127.0.0.1:8001/sms/'
    rProvider1 = requests.post(url, data=data)
    print(rProvider1.text)
    
def postProvider2(data):
    url = 'http://127.0.0.1:8002/sms/'
    rProvider2 = requests.post(url, data=data)
    print(rProvider2.text)

def postProvider3(data):
    url = 'http://127.0.0.1:8003/sms/'
    rProvider3 = requests.post(url, data=data)
    print(rProvider3.text)