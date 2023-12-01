class Group:
    """
    Represents a set of frames used to create the final astrophotography product.

    In a Group, all of the configurations (e.g. exp_time, and gain of light frames) 
    are the same. And they share the same calibration frames.

    Attributes
    ----------
    light : list
        A list of Sequence objects for the light frames.
    dark : list
        A list of Sequence objects for the dark frames.
    flat : list
        A list of Sequence objects for the flat frames.
    bias : list
        A list of Sequence objects for the bias frames.
    telescope : Telescope
        A Telescope object containing the information of the telescope.
    filter : Filter
        A Filter object containing the information of the filter.
    instrument : Instrument
        An Instrument object containing the information of the instrument.
    total_exp_time : float
        The total exposure time of the light frames.
    """
    def __init__(self, light, dark, flat, bias, telescope, filter, instrument, total_exp_time):
        self.light = light
        self.dark = dark
        self.flat = flat
        self.bias = bias
        self.telescope = telescope
        self.filter = filter
        self.instrument = instrument
        self.total_exp_time = total_exp_time
