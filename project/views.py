from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def custom_404(request, exception=None):
    return Response({
        "error": "The resource was not found."
    }, status=status.HTTP_404_NOT_FOUND)

def custom_500(request):
    return Response({
        "error": "An unexpected error occurred."
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
