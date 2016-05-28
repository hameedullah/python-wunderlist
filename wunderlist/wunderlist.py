#!/usr/bin/env python
# −*− coding: UTF−8 −*−
"""Wunderlist class

Quick hack to migrate my wunderlist data

TODO: Add OAuth Support
"""

__author__ = "Hameedullah Khan <h@hameedullah.com>"
__version__ = "0.1"

import requests

WUNDERLIST_API_VERSION = "v1"
WUNDERLIST_API_URL = "a.wunderlist.com/api"

# TODO: Write classes to represent Wunderlist API objects

class Wunderlist:
    def __init__(self, client_id, client_secret=None, api_url=None,
            api_version=None):
        """Setups the wunderlist client

        Args:
           clinet_id: Client ID from Wunderlist is required
           client_secret: 
                (Optional) Client secret is not required for standalone apps
        """
        self._client_id = client_id
        self._client_secret = client_secret
        if not api_url:
            self._api_url = WUNDERLIST_API_URL
        else:
            self._api_url = api_url

        if not api_version:
            self.api_version = WUNDERLIST_API_VERSION
        else:
            self.api_version = api_version

        self._api = "http://%s/%s" % (self._api_url, self.api_version)

    def _get(self, url, data={}, auth=False):
        if auth:
            headers = {}
            headers['X-Client-ID'] = self._client_id
            headers['X-Access-Token'] = self._access_token
        else:
            headers = {}

        _api_url = "%s/%s" % (self._api,url)

        print("API URL: %s" % (_api_url,))

        response = requests.get(_api_url, params=data, headers=headers)
        return response

    def setAccessToken(self, access_token):
        """Set Access Token to be used in subsequent API Calls

        For non web usage the Access token can be generated from the Wunderlist developer page.
        For web based usage the access code will be returned by Wunderlist
        after successful OAuth authorization.
        """
        self._access_token = access_token

    def GetAvatar(self, user_id=None, size=None, fallback=None):
        """Gets user Avatar

        Args:
            user_id: (Required) User ID of the user for which the avatar is
                      requested.

            size: (Optional) values: 25, 28, 30, 32, 50, 54, 56, 60, 64, 108,
            128, 135, 256, 270, 512 and original

            fallback: (Optional) true or false

        Returns:
            Avatar Image
        """
        _url = "avatar"
        data = {}
        data['user_id'] = user_id
        if size: data['size'] = size
        if type(fallback) != type(None): data['fallback'] = fallback
        response = self._get(_url, data=data, auth=False)
        # TODO: Add more options to manipulate the binary data returned for
        # this request
        return response

    def GetFolders(self, folder_id=None):
        """Gets list of all Folders"""
        if folder_id:
            # TODO: Error checking for folder_id param?
            _url = "folders/%s" % folder_id
        else:
            _url = "folders"
        response = self._get(_url, auth=True)
        return response.json()

    def GetLists(self, list_id=None):
        """Get List(s) from Wunderlist"""
        _url = "lists"
        data = {}
        if list_id:
            # TODO: Add data validation on all params
            data['id'] = list_id
        response = self._get(_url, data=data, auth=True)
        return response.json()

    def GetUser(self):
        _url = "user"
        response = self._get(_url, auth=True)
        return response.json()

if __name__ == "__main__":
    pass


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
