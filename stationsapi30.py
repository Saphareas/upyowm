import requests as urequests

def register_station(api_key, eid, name, lat, long, alt):
    """HTTP 201 if successful"""
    url = "http://api.openweathermap.org/data/3.0/stations"
    url += "?appid={}".format(api_key)
    header = { "Content-Type": "application/json" }
    payload = {
        "external_id": eid,
        "name": name,
        "latitude": lat,
        "longitude": long,
        "altitude": alt
    }
    response = urequests.post(url, json=payload, headers=header)
    return response

def get_stations(api_key, station_id=None):
    url = "http://api.openweathermap.org/data/3.0/stations"
    if station_id is not None:
        url += "/{}".format(station_id)
    url += "?appid={}".format(api_key)
    response = urequests.get(url)
    return response

def update_station(api_key, station_id, **kwargs):
    """HTTP 200 if successful"""
    url = "http://api.openweathermap.org/data/3.0/stations"
    url += "/{}".format(station_id)
    url += "?appid={}".format(api_key)
    header = { "Content-Type": "application/json" }
    response = urequests.put(url, data=kwargs)
    return response

def delete_station(api_key, station_id):
    """HTTP 204 if successful"""
    url = "http://api.openweathermap.org/data/3.0/stations"
    url += "/{}".format(station_id)
    url += "?appid={}".format(api_key)
    response = urequests.delete(url)
    return response

def upload_measurement(api_key, data):
    """HTTP 204 if successful
    :param data: should be a dict, for all parameters refer to https://openweathermap.org/stations#measurement
    """
    url = "http://api.openweathermap.org/data/3.0/measurements"
    url += "?appid={}".format(api_key)
    header = { "Content-Type": "application/json" }
    response = urequests.post(url, json=data, headers=header)
    return response

def get_aggregated_measurements(api_key, _station_id, _type, _limit, _from, _to):
    url = "http://api.openweathermap.org/data/3.0/measurements"
    url += "?appid={}".format(api_key)
    for param in ["station_id", "type", "limit", "from", "to"]:
        url += "&{}={}".format(param, eval("_"+param))
    response = urequests.get(url)
    return response
