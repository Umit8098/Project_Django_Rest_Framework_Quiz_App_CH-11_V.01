from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer
from .models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required = True,
        validators = [
            UniqueValidator(queryset=User.objects.all())
        ],
    )
    
    password = serializers.CharField(
        write_only = True,  # GET methods can not return the password
        required = True,
        validators = [
            validate_password
        ],
        style = {
            'input_type':'password',
        }
    )
    
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {
            'input_type':'password',
        }
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'password2',
        )
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def validate(self, data):
        if data.get('password') != data.get('password2'):
            data = {
                "password": "Password fields does not match!!!"
            }
            raise serializers.ValidationError(data)
        return data
    
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email', 
        )

class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta(TokenSerializer.Meta):
        fields = (
            'key',
            'user',
        )


class ProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = (
            'id',
            'image',
            'about',
            'user',
        )
