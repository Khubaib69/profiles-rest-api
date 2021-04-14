from rest_framework.views import APIView
from rest_framework.response import Response



class HelloAPIView(APIView):
    """TEST API VIEW"""

    def get(self,request,format=None):
        "Returns A List Of API Features"
        an_apiview=[
        'Uses the http methods as funcions (get,post,patch,put,delete)'
        'is similer to a tradishional django view'
        'gives you the most control of over your application logic'
        'is mapped manually to urls'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
