from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = get_user_model()
        fields = ('title', 'password', 'description', 'image')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
            'title': {'required': True},
            'image': {'required': True}
        }
    
    def create(self, validated_data):
        user = self.Meta.model.objects.create(
            email=validated_data['title'],
            first_name=validated_data['description'],
            last_name=validated_data['image'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'title', 'password', 'description', 'image','is_admin')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }