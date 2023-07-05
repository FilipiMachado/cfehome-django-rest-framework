from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_framework.authtoken import Token


class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"
