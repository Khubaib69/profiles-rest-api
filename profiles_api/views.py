from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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
