from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

class StaticAPIAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_secret = request.headers.get('API-Secret')
        if api_secret == settings.STATIC_API_SECRET:
            return ('admin', None)
        raise AuthenticationFailed('Invalid API secret')
