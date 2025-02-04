
"""
core views fo rapp
"""


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request):
    """returns successful response"""
    return Response({'healthy':True})

