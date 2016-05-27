#!/usr/bin/env python
# −*− coding: UTF−8 −*−

from httmock import urlmatch, response
import os

JSON_HEADER = {'Content-Type': 'application/json'}
JSON_FIXTURES = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures")

@urlmatch()
def api_endpoint(url, request):
    # TODO: Debug why os.path.join not working here
    json_path = JSON_FIXTURES + url.path
    try:
        with open(json_path, 'r') as j:
            content = j.read()
    except EnvironmentError:
        return response(404, {}, JSON_HEADER, None, 5, request)
    else:
        return response(200, content, JSON_HEADER, None, 5, request)
