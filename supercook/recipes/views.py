from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def test_swagger(request):
  testobj = {'message':'this is from swagger'}
  return Response(testobj)
  
