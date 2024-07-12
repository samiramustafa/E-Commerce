import logging
from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

class CustomErrorMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        logger.error(f'Error occurred: {exception}', exc_info=True)
        return Response({
            "error": "An unexpected error occurred."
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
