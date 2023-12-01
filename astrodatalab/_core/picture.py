class Picture:
    """
    Represents an astrophotography image that will be posted on social media.

    Attributes
    ----------
    id : int
        The unique id of the picture.
    name : str
        The name of the picture.
    images : dict
        A dictionary of Frame objects for the final products. The key is the name of the frame.
    data : list
        A list of Group objects for the raw data.
    """
    def __init__(self, id, name, images, data):
        self.id = id
        self.name = name
        self.images = images
        self.data = data
