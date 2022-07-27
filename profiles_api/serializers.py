from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):      # serializes a name field for testing api view
    name = serializers.CharField(max_length=10)


# creating serializer for our profiles api
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:     # we have to create meta class to specify the model which we will be targeting to.
        model = models.UserProfile
        fields = ("id", "email", 'name', 'password')    # specifying the list of fields which I want to be accessible in my API
        extra_kwargs = {        # providing excpetional cases here (we want password only when we create user)
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # After validation we can create our user
    def create(self, validated_data):
        email = validated_data['email']
        name = validated_data['name']
        password = validated_data['password']
        user = models.UserProfile.objects.create_user(email=email, name=name, password=password)
        return user
