




from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise serializers.ValidationError({
                    "detail": "Invalid username or password."
                })

            attrs['user'] = user
        else:
            raise serializers.ValidationError({
                "detail": "Username and password are required."
            })

        return attrs