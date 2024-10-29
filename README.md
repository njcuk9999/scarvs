# The uprv module

## Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)

[Back to top](#contents)

---

## Introduction

Insert text here

## Installation

#### Step 1: Clone the repository

```bash
git clone git@github.com:njcuk9999/uprv.git
```

#### Step 2: Install python 3.10 

Create a conda or python environment

e.g.

```bash 
conda create --name uprv-env python=3.10
conda activate uprv-env
```

#### Step 3: Install uprv

```bash
cd {UPRV_ROOT}
pip install -U -e .
```

Note on can also use venv (instead of conda)

Note `{UPRV_ROOT}` is the path to the cloned github repository (i.e. /path/to/uprv)

[Back to top](#contents)

---

## Setup

First [install uprv](#installation).
Once you've done this activate the environment you installed uprv in.
(e.g. `conda activate uprv-env`)

To setup UPRV, you need to run the following command:

```bash
uprv_setup {yaml_file}
```

where `yaml_file` is the yaml file you wish to create (if left blank you 
will be asked for one).


[Back to top](#contents)

---

## Usage


### Command line

To run UPRV, you need activate the environemnt you installed uprv in.
(e.g. `conda activate uprv-env`)

Then you need to run the following command:

```bash
uprv_run {yaml_file}
```

[Back to top](#contents)

---

### Inside Python/Notebooks

To run UPRV inside python, you need to import the uprv module:

```python
from uprv.recipes import uprv_run

# define the path to your yaml file
yaml_file = '/path/to/yaml_file.yaml'

# run uprv
uprv_run.main(yaml_file)
```

### Overriding parameters

If you wish to override the yaml file, you can do so by passing in a dictionary
as follows:

```python

from uprv.core import startup
from uprv.core import general

# define the path to your yaml file
yaml_file = '/path/to/yaml_file.yaml'
# get parameters
params = startup.get_params(yaml_file)

# Define data path
params['DATA_DIR'] = '/path/to/data'

# Define plot path
params['PLOT_DIR'] = '/path/to/plots'

# --------------------------------------------------------------
# Then use the following to run uprv
# ---------------------------------------------------------------
    # run science functions
    for science_func in params['SCIFUNCS']:
        # check whether we should run this function then run it
        if general.check_run(params, science_func, 'SCIENCE'):
            # log the we are running a function
            general.log_run(params, science_func, 'SCIENCE')
            # run the science function
            params['SCIFUNCS'][science_func](params)
    # run plotting functions
    for plot_func in params['PLOTFUNCS']:
        # check whether we should run this function then run it
        if general.check_run(params, plot_func, 'PLOTTING'):
            # log the we are running a function
            general.log_run(params, plot_func, 'PLOTTING')
            # run the plotting function
            params['PLOTFUNCS'][plot_func](params)


```
### Running invidual function


To run an individual function, you can call the dictionary and run the function

```python
from uprv.core import startup

# define the path to your yaml file
yaml_file = '/path/to/yaml_file.yaml'
# get parameters
params = startup.get_params(yaml_file)

# run the science "TEST" function
params['SCIFUNCS']['TEST'](params)

# run the plotting "TEST" function
params['PLOTFUNCS']['TEST'](params)
```

A note book and yaml example are provided in the uprv/docs directory.


[Back to top](#contents)

---