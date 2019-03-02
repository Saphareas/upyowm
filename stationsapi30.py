import requests as urequests

def __combine_params(api_key, params=None):
    """TODO: docstring
    """
    combined = "?appid={}".format(api_key)
    if params not None:
        for key, value in params.items():
            url_params += "&{}={}".format(key, value)
    return combined

def post(api_key, json_payload, url="http://api.openweathermap.org/data/3.0/stations", params=None, header={"Content-Type": "application/json"}):
    """Makes a POST request

    :param url: the URL that is requested
    TODO: docstring
    """
    url += __combine_params(api_key, params=params)
    response = urequests.post(url, json=json_payload, headers=header)
    return response

def get(api_key, url="http://api.openweathermap.org/data/3.0/stations/", params=None):
    """TODO: docstring
    """
    url += __combine_params(api_key, params=params)
    response = urequests.get(url)
    return response
