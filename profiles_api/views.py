from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


from profiles_api import models
from profiles_api import permissions


class HelloAPIView(APIView):
    """TEST API VIEW"""
    serializer_class=serializers.HelloSerializers

    def get(self,request,format=None):
        "Returns A List Of API Features"
        an_apiview=[
        'Uses the http methods as funcions (get,post,patch,put,delete)'
        'is similer to a tradishional django view'
        'gives you the most control of over your application logic'
        'is mapped manually to urls'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})


    def post(self,request):
        """Create A Hello Message With Our Name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



    def put(self,request,pk=None):
        """To Fully Update an object"""
        return Response({'method: PUT'})

    def patch(self,request,pk=None):
        """To Fully Update an Object"""
        return Response({'method:PATCH'})

    def delete(self,request, pk=None):
        """To Delete an Object"""
        return Response({'method:Delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewsets"""


    def list(self,request):
        """Return A Hello Message"""
        a_viewset=[
            "Uses action (list,create,retrive,update,partial_update)",
            "Automaticlly maps to URLs using Routers",
            "Provide More Functionality with less code",

        ]
        return Response({'message':'HELLO','a_viewset':a_viewset})


    def post(self,request):
        """Create A Hello Message With Our Name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle Updating An Object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle Updating part An Object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle Removing An Object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating And Updating Profiles"""

    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
