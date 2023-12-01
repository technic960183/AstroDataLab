class Location:
    """
    Represents a geographical location where astrophotography frames are captured.

    Attributes
    ----------
    name : str
        The name of the location.
    latitude : float
        The latitude of the location in degrees.
    longitude : float
        The longitude of the location in degrees.
    elevation : float
        The elevation of the location in meters.
    """
    def __init__(self, name, latitude, longitude, elevation):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
