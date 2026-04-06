from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError({"email": "User with this email does not exist."})

            # authenticate requires username
            user = authenticate(username=user.username, password=password)
            if not user:
                raise serializers.ValidationError({"password": "Incorrect password."})

            attrs['user'] = user
        else:
            raise serializers.ValidationError({"detail": "Email and password are required."})

        return attrs