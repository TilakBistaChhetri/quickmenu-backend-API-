


from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,  # hide in api response
        required=True,  # make it mandatory
        validators=[validate_password]  # before saving password validate it with Django's build in password validater
    )
    password2 = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = User # User model is build in model of Django which is used for authentication and authorization
        fields = ('id', 'username', 'email', 'password', 'password2')

    def validate(self, attrs):

        if attrs['password'] != attrs['password2']:
        
    
            raise serializers.ValidationError({
                "password": "Password fields didn't match."
            })
        return attrs  # if password and password2 are same then return the validated data 
    



    def create(self, validated_data):
        validated_data.pop('password2')  # remove password 2 from the data dictionary 


         # user is created in database but password is not set yet, becuase we need to hash the password before saving it in database
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )



        user.set_password(validated_data['password']) # This converts password into secure hash
        user.save() # Now everything is stored permanently in database and use is created successfully 
        return user # send created user data in response after successfully registration 
    







    