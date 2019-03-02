class Station(object):
    def __init__(self, eid, name, lat, long, alt):
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

    @classmethod
    def from_owm(cls, id):
        """Gets information about a station from OWM and creates a new Station object from it

        :param id: the id of the station that should be "mirrored"
        """
        raise NotImplementedError
        response = {}
        return cls(response.text.eid, response.text.name, response.text.lat, response.text.long, response.text.alt)

    def register(self, api_key):
        """Register the station in the OWM service
        :param api_key: OWMs API key the Station should be registered for
        """
        raise NotImplementedError

    def measure(self, data):
        """Sets or updates the weather data of the Station

        :param data: dict with weather data; refer to https://openweathermap.org/stations#measurement for a list of possible parameters
        """
        raise NotImplementedError

    def update(self, api_key):
        """Update the station in the OWM service
        :param api_key: OWMs API key the Station should be registered for
        """
        raise NotImplementedError
