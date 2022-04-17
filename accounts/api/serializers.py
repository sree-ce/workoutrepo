from rest_framework import serializers
from accounts.models import Trainer,Customer,User
from django.contrib.auth.hashers import make_password

class TrainerSerialiser(serializers.ModelSerializer):
     
    class Meta:
        model = Trainer
        fields = ['name','username', 'email', 'password', 'mobile','certification','stream','about']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    
    def create(self, validated_data):
        
        user = self.Meta.model(**validated_data)
        
        user.password = make_password('password')
        user.save()
        return user
    



class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name','username','email','password','mobile','age','weight','height','health_condition']
        extra_kwargs = { 
            'password':{'write_only':True}
        }

    def validate_name(self,value):
        if len(value) < 3:
            raise serializers.ValidationError("name is too short")
        else:
            return value
    def validate_description(self,value):
        if len(value) < 5:
            raise serializers.ValidationError("description is too short")
        else:
            return value
    def validate_password(self,value):
        if len(value) < 5:
            raise serializers.ValidationError("password is too short")
        else:
            return value

    def create(self, validated_data):
        
        user = self.Meta.model(**validated_data)
        
        user.password = make_password('password')
        user.save()
        return user
    
    
    # def save(self, **kwargs):
    #     user = Customer( 
    #         username = self.validated_data['username'],
    #         email = self.validated_data['email']
    #     )
    #     password = self.validated_data['password']
    #     if password is None:
    #         raise serializers.ValidationError({"error":"password cannot be null"})
    #     user.password = make_password('password')
    #     user.is_customer = True
    #     user.save()