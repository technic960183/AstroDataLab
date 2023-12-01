class Filter:
    """
    Represents a filter used in astrophotography.

    Attributes
    ----------
    name : str
        The name of the filter.
    band : str
        The band of the filter.
    """
    def __init__(self, name, band):
        self.name = name
        self.band = band
