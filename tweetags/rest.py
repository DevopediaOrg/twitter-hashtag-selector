#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Twitter API request/response call."""


import json
import requests


class TweetagsRestAPI(object):

    """REST api for twitter request/response."""

    def __init__(self, uri=None, method="GET", payload={}, headers={},
                 grant_type="client_credentials", verify=True, timeout=10):
        """REST object initialization."""
        self._uri = uri
        self._method = method
        self._payload = payload
        self._headers = headers
        self._grant_type = grant_type
        self._verify = verify
        self._timeout = timeout
        self._payload.update({"grant_type": self._grant_type})

    @property
    def req_kwargs(self, ):
        """Collecting all the required request kwargs."""
        return {"headers": self._headers, "verify": self._verify,
                "timeout": self._timeout, "data": self._payload}
        
    def __enter__(self, ):
        """Define what the context manager should do at the begining of the block."""
        response = requests.request(self._method, self._uri, **self.req_kwargs)
        return response

    def __exit__(self, exc_type, exc_val, exc_trace):
        """Defines what the context manager should do after it's block has been executed."""
        return False

