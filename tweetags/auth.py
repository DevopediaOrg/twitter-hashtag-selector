#!/usr/bin/env python


"""Python inteerface to access twitter api."""
from future.standard_library import install_aliases # To clear the python2/python3 dependancy.
install_aliases()

import os
import base64
import requests
from urllib.parse import quote_plus
from api import tweetags_api
from rest import TweetagsRestAPI
from exceptions import AccessTokenError


class AuthenticationAPI(object):
    
    """Authentication using twitter account secret keys, access token."""

    def __init__(self, api_key=None, api_secret_key=None, access_token=None, access_token_key=None):
        """Initialization of authentication objects.
        
        api_key: twitter user/develper account api key.
        api_secret_key: twitter user/developer account api secret key.
        access_token: twitter user/developer account access key.
        access_token_key: twitter user/developer account access key.
        """
        self.api_key = api_key if api_key else os.environ.get('API_KEY', None)
        self.api_secret_key = api_secret_key if api_secret_key else os.environ.get('API_SECRET_KEY', None)
        self.access_token = access_token if access_token else os.environ.get('ACCESS_TOKEN', None)
        self.access_token_key = access_token_key if access_token_key else os.environ.get('ACCESS_TOKEN_KEY', None)

    @staticmethod
    def app_only_auth_token(api_key, api_secret_key):
        """Application only authentication requests.

        URL encode the consumer key and the consumer secret according to RFC1378.

        api_key: twitter user/developer account api key.
        api_secret_key: twitter user/developer account secret key.
        """
        bearer = base64.b64encode(bytes(f"{api_key}:{api_secret_key}", "utf-8"))
        headers = {"Authorization": f"Basic {bearer.decode('utf-8')}",
                  "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        uri = tweetags_api['app_only_auth_token']
        with TweetagsRestAPI(uri=uri, method="POST", headers=headers) as resp:
            pass
        return resp

