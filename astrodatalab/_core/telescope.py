class Telescope:
    """
    Represents a telescope used in astrophotography.

    Attributes
    ----------
    name : str
        The name of the telescope.
    diameter : float
        The diameter of the telescope in millimeters.
    focal_length : float
        The focal length of the telescope in millimeters.
    """
    def __init__(self, name, diameter, focal_length):
        self.name = name
        self.diameter = diameter
        self.focal_length = focal_length
