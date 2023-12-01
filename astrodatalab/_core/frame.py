class Frame:
    """
    Represents a single frame in an astrophotography sequence.

    Attributes
    ----------
    path : str
        The path of the frame.
    type : str
        The type of the frame (e.g., 'light', 'dark', 'flat', 'bias').
    header : dict
        A dictionary containing some header information of the frame.
    """
    def __init__(self, path, type, header):
        self.path = path
        self.type = type
        self.header = header
