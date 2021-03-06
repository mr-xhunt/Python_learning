# Request Module for HTTP

#!/usr/bin/env python

from urllib.request import urlopen


import certifi
import json

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/api/v3/search?query=AA&limit=10&exchange=NASDAQ&apikey=YOUR_API_KEY")
print(get_jsonparsed_data(url))

#orrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

import requests
r = requests.get("https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=Your api Key")
print(r.content)
print(r.status_code)
