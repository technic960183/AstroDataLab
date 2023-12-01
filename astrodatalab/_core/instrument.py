class Instrument:
    """
    Represents an instrument (typically a camera) used in astrophotography.

    Attributes
    ----------
    name : str
        The name of the instrument.
    pixel_size : float
        The pixel size of the instrument's sensor in micrometers.
    """
    def __init__(self, name, pixel_size):
        self.name = name
        self.pixel_size = pixel_size
