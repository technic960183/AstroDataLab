class Sequence:
    """
    Represents a sequence of frames obtained consecutively at the same location.

    Attributes
    ----------
    path : str
        The path of the directory containing the frames.
    frames : pandas.DataFrame
        A DataFrame object containing the information of the frames.
    type : str
        The type of the frames (e.g., 'light', 'dark', 'flat', 'bias').
    exp_time : float
        The exposure time of the frames.
    gain : float
        The gain (or ISO) of the frames.
    location : Location
        A Location object containing the information of the location where the frames were obtained.
    telescope : Telescope
        A Telescope object containing the information of the telescope.
    filter : Filter
        A Filter object containing the information of the filter.
    """
    def __init__(self, path, frames, type, exp_time, gain, location, telescope, filter):
        self.path = path
        self.frames = frames
        self.type = type
        self.exp_time = exp_time
        self.gain = gain
        self.location = location
        self.telescope = telescope
        self.filter = filter

class LightSequence(Sequence):
    """ Represents a sequence of light frames. Inherits from Sequence. """
    pass

class DarkSequence(Sequence):
    """ Represents a sequence of dark frames. Inherits from Sequence. """
    pass

class FlatSequence(Sequence):
    """ Represents a sequence of flat frames. Inherits from Sequence. """
    pass

class BiasSequence(Sequence):
    """ Represents a sequence of bias frames. Inherits from Sequence. """
    pass
