from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import  validate_password
from .models import Feedback

class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Passwords must match'})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        return user

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name')


class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id','name','email','message','created_at')
        read_only_fields = ('id','created_at',)