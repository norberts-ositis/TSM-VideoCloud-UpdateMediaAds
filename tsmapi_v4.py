# TSM Video Cloud API library
# install requests package in addition to standard Python packages
from hashlib import sha256
import hmac
import json
import requests
import time
import urllib.parse


class TSMAPI:
    VERSION = "1.2"
    PREFIX = "auth_"

    def __init__(self, uri, key, secret, timestamp=int(time.time())):
        """
        Prepare the request data
        :param str uri: Telia Video Cloud API URI
        :param str key: API key from Settings page
        :param str secret: API secret from Settings page
        :param int timestamp: UNIX timestamp of the request, default = current time
        """
        self.uri = uri
        self.key = key
        self.secret = secret
        self.timestamp = timestamp

    # Generate payload
    @staticmethod
    def payload(auth, params):
        if isinstance(auth, dict) and isinstance(params, dict):
            return dict([(k, v) for k, v in auth.items()] + [(k, v) for k, v in params.items()])

    # Generate signature
    def signature(self, payload, action="GET"):
        payload_list = []
        for payload_item in sorted(payload.keys()):
            payload_list.append((payload_item, payload.get(payload_item)))
        payload = '\n'.join([action, "cdnapi", urllib.parse.unquote_plus(urllib.parse.urlencode(payload_list))])
        return hmac.new(bytearray(self.secret, 'ascii'), payload.encode(), sha256).hexdigest()

    # Sign the Request with a Token
    def sign(self, data, action="GET", prefix=PREFIX):
        auth = {prefix + "version": self.VERSION, prefix + "key": self.key, prefix + "timestamp": self.timestamp}
        params = {}
        for k, v in data.items():
            params[k.lower()] = json.dumps(v) if isinstance(v, dict) or isinstance(v, list) else v
        payload = self.payload(auth, params)
        auth[prefix + 'signature'] = self.signature(payload, action)
        return auth

    # Prepare parameters
    def prepare_params(self, data, action="GET"):
        auth = self.sign(data, action)
        params = {}
        for key, val in data.items():
            params[key.lower()] = json.dumps(val) if isinstance(val, dict) or isinstance(val, list) else val
        return dict([(k, v) for k, v in params.items()] + [(k, v) for k, v in auth.items()])

    # Send POST request
    def send_post(self, data):
        """
        Send the post action and parameters
        :param dict data: API request parameters
        :return dict: request response
        """
        return requests.post(self.uri, data=self.prepare_params(data, "POST"), headers={})
