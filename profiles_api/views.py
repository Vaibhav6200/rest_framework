from rest_framework.views import APIView
from rest_framework.response import Response       # used to return responses from api view
from rest_framework import status
from profiles_api import serializers

from rest_framework import viewsets
from profiles_api import models

from rest_framework import filters

from profiles_api import permissions
from rest_framework.authentication import TokenAuthentication       # By this we authenticate our users itself
# NOTE: it works by generating a random token string when the user logs in then every request that we make to that API
# that request contains this token string


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer   # retrieving our serializers class

    def get(self, request):        # Returns a list of api view features
        an_apiview = ['apple', 'banana', 'grapes']
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        # Step1: Retrieve The serializer and pass in the data which comes in the request
        # NOTE: when we make post request to our api-view the data gets passed into request.data
        # we assign this data to our serializers class and then we create a new variable for our serializers class
        serializer = self.serializer_class(data=request.data)

        # Step2: Validate the serializer
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # NOTE: By default Response() - returns HTTP 200 OK request, But we got error so we return standard response
        # code for this type of error in our API

    def put(self, request, pk=None):    # used to update complete object that's why we take pk as input
        return Response({"message": "Put Method"})

    def patch(self, request, pk=None):  # partial update of an object, only update the fields provided in the request
        return Response({'message': 'Patch Method'})

    def delete(self, request, pk=None):     # deletes an object in our database
        return Response({'message': 'Delete Method'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = ['Uses actions (list, create, retrieve, update, partial update and destroy)',
                     'Automatically maps to URLs using Routers',
                     'Provides more functionality with less code']
        return Response({"message": "Hello Vaibhav", 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):      # retrieve specific object using pk
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):     # update an object using its pk
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):      # update a part of an object using pk
        return Response({"http_method": "PATCH"})

    def delete(self, request, pk=None):     # delete an object using its pk
        return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    # Step1: assign serializer class to a variable
    serializer_class = serializers.UserProfileSerializer

    # Step2: retrieve all data/objects from the database
    queryset = models.UserProfile.objects.all()

    # Step3: Add authentication classes
    authentication_classes = (TokenAuthentication,)
    # NOTE: it works by generating a random token string when the user logs in then
    # every request that we make to that API that request contains this token string

    # Step4: Add Permissions classes (These are the permissions which we give users to do certain things)
    permission_classes = (permissions.UpdateOwnProfile,)

    # Step5: Add Search filter to our API
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


