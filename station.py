from . import stationsapi30
import ujson
import time

class Station(object):
    def __init__(self, eid, name, lat, long, alt, station_id=None):
        """Creates a new Station object

        :param eid: the external ID of the station, e.g. "SF_TEST001"
        :param name: the name of the station, e.g. "San Francisco Test Station"
        :param lat: the latitude of the station, e.g. 37.76
        :param long: the longitude of the station, e.g. -122.43
        :param alt: the altitude of the station, e.g. 150
        """
        self.external_id = eid
        self.name = name
        self.latitude = lat
        self.longitude = long
        self.altitude = alt
        self.station_id = station_id

    @classmethod
    #TODO: get by eid
    def from_owm(cls, api_key, station_id=None ):
        """Gets information about a station from OWM and creates a new Station object from it

        :param id: the id of the station that should be "mirrored"
        """
        if station_id is not None:
            r = stationsapi30.get_stations(api_key, station_id=station_id)
        else:
            r = stationsapi30.get_stations(api_key)
        if r.status_code == 200:
            print("Successful!")
            r = ujson.loads(r.text)
            if station_id is not None:
                return cls(r["external_id"], r["name"], r["latitude"], r["longitude"], r["altitude"], station_id=r["ID"])
            else:
                stations = []
                for sta in r:
                    stations.append(cls(sta["external_id"], sta["name"], sta["latitude"], sta["longitude"], sta["altitude"], station_id=sta["id"]))
                return stations
        else:
            print("Something went wrong:\n" + r.text)

    def register(self, api_key):
        """Register the station in the OWM service

        :param api_key: OWMs API key the Station should be registered for
        """
        r = stationsapi30.register_station(api_key, self.external_id, self.name, self.latitude, self.longitude, self.altitude)
        if r.status_code == 201:
            print("Successful!")
            self.station_id = ujson.loads(r.text)["ID"]
        else:
            print("Something went wrong:\n" + r.text)

    def measure(self, api_key, data):
        """Sets or updates the weather data of the Station

        :param data: dict with weather data; refer to https://openweathermap.org/stations#measurement for a list of possible parameters
        """
        r = stationsapi30.upload_measurement(api_key, data)
        if r.status_code == 204:
            print("Successful!")
        else:
            print("Something went wrong:\n" + r.text)

    def update(self, api_key):
        """Update the station in the OWM service
        :param api_key: OWMs API key the Station should be registered for
        """
        r = stationsapi30.update_station(api_key, self.station_id, new_data={
            "external_id": self.external_id,
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "altitude": self.altitude
        })
        if r.status_code == 200:
            print("Successful!")
        else:
            print("Something went wrong:\n" + r.text)

    def get_measurements(self, api_key, measure_type, limit, interval_from=0, interval_to=int(time.time())):
        m = stationsapi30.get_aggregated_measurements(api_key, self.station_id, measure_type, limit, interval_from, interval_to)
        if m.status_code == 200:
            print("Successful!")
            m = ujson.loads(m.text)
            return m
        else:
            print("Something went wrong:\n" + m.text)

    def delete(self, api_key):
        """Deletes/unregisters the station on owm.org"""
        stationsapi30.delete_station(api_key, self.station_id)
