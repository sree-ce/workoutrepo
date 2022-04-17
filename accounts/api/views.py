from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import TrainerSerialiser,RegistrationSerializer


# Create your views here.


@api_view(['POST'])
def trainer_registration(request):

    if request.method == 'POST':
        serializer = TrainerSerialiser(data=request.data)
        data = {}
        if serializer.is_valid():
            traineraccount = serializer.save()
            data['response'] = 'Registration successfull'
            data['username'] = traineraccount.username
            data['email'] = traineraccount.email

            refresh = RefreshToken.for_user(traineraccount)
            data['token'] = { 
                    'refresh':str(refresh),
                    'access':str(refresh.access_token),
                }

        else:
            return Response(serializer.errors)

        return Response(data)
@api_view(['POST'])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration successfull'
            data['username'] = account.username
            data['email'] = account.email
            
            refresh = RefreshToken.for_user(account)
            data['token'] = { 
                'refresh':str(refresh),
                'access':str(refresh.access_token),
            }


        else:
            return Response(serializer.errors)
        
        return Response(data)