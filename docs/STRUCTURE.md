# Structure
Created by Yuan-Ming Hsu on 2023/11/26.

## Overview

```
AstroDataLab/
│
├── README.md
├── GITFLOW.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── environment.yml
│
├── astrodatalab/
│   ├── __init__.py
│   ├── core/
│   ├── io/
│   ├── manager/
│   ├── process/
│   ├── history/
│   └── utils/
│
├── docs/
│
├── tests/
│
├── examples/
│
├── dev/
│
├── assets/
│
└── configs/
```

## astrodatalab
The main package of AstroDataLab.

### core
Classes for core data structure.

#### Picture
The astrophotography image that you will post on the social media.
Attributes:
- `id`: The unique id of the picture.
- `name`: The name of the picture.
- `images`: A dictionary of Frame objects for the final products. For versioning purpose, the key is the name of the frame.
- `data`: A list of a Group objects for the raw data.

#### Group
The set of frames that you will use to create the final product. In a Group, all of the configurations (e.g. exp_time, and gain of light frames) are the same. And they share the same calibration frames.
Attributes:
- `light`: A list of Sequence objects for the light frames.
- `dark`: A list of Sequence objects for the dark frames.
- `flat`: A list of Sequence objects for the flat frames.
- `bias`: A list of Sequence objects for the bias frames.
- `telecope`: A Telescope object containing the information of the telescope.
- `filter`: A Filter object containing the information of the filter.
- `insturment`: An Insturment object containing the information of the insturment (camera).
- `total_exp_time`: The total exposure time of the light frames.

#### Sequence
A sequence of frames that obtained in a sequence of time at the same location. In a Sequence, all of the Frame objects must be stored in the same directory.
Attributes:
- `path`: The path of the directory containing the frames.
- `frames`: A pandas.DataFrame object containing the information of the frames.
- `type`: The type of the frames. It can be `light`, `dark`, `flat`, or `bias`.
- `exp_time`: The exposure time of the frames.
- `gain`: The gain (or ISO) of the frames.
- `location`: A Location object containing the information of the location where the frames were obtained.
- `telecope`: A Telescope object containing the information of the telescope.
- `filter`: A Filter object containing the information of the filter.

Note:
- Consider create LightSequence, DarkSequence, FlatSequence, and BiasSequence classes for a better structure.

#### Frame
A single frame.
Attributes:
- `path`: The path of the frame.
- `type`: The type of the frame. It can be `light`, `dark`, `flat`, or `bias`.
- `header`: A dictionary containing some header information of the frame.

#### Telescope
A telescope.
Attributes:
- `name`: The name of the telescope.
- `diameter`: The diameter of the telescope.
- `focal_length`: The focal length of the telescope.

#### Filter
A filter.
Attributes:
- `name`: The name of the filter.
- `band`: The band of the filter.

#### Insturment
An insturment.
Attributes:
- `name`: The name of the insturment.
- `pixel_size`: The pixel size of the insturment.

#### Location
A location.
Attributes:
- `name`: The name of the location.
- `latitude`: The latitude of the location.
- `longitude`: The longitude of the location.
- `elevation`: The elevation of the location.

### io
Classes for supporting input/output.

### manager
Classes for managing data.

### process
Classes for processing data.

### history
Classes for presenting history.

### utils
Classes for utilities.

## docs
Documentation.

## tests
Tests for intergration, installation, etc.

## examples
Examples for using AstroDataLab.

## dev
Scripts and Jupyter notebooks for development purpose.

### EasyImport.py
A script for importing data from the device to the computer.

### ConstureStacking.py
A script for copy the data to a working directory for other software to do the stacking process.

## assets
Necessary assets for front-end.

## configs
Configuration files for users.
