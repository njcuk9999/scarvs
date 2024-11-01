# Plotting directory

This directory contains any science codes.

To be able to use them please add them to the sciece.__init__.py file as follows:

```python
from uprv.plotting import test

# a dictionary of science functions
PLOT_FUNCS = dict()

# Test science function
PLOT_FUNCS['TEST'] = test.test
```

Make sure the function name (`TEST`) is unique.

You can add as many function as you like from a single file or from multiple files

Please add a comment to the function to describe what it does.

You must also add a `RUNPLOT_{MYFUNC}` to the `uprv.constants.constants.py` file.

e.g.

```python
# Add test function to science functions
CDict.add('RUNPLOT_TEST', value=False, dtype=bool,
          source=__NAME__, user=True,
          active=True, group=cgroup,
          description='Run test science function')
```

---

## Saving and showing plots

We want to do this in a uniform way. Please use functions similar to the following:

```python
import matplotlib.pyplot as plt

from aperocore.constants import param_functions
from uprv.plotting import core

# =============================================================================
# Define variables
# =============================================================================
# get parameter dictionary
ParamDict = param_functions.ParamDict


def test(params: ParamDict):
    """
    First argument must be params

    :param params: ParamDict, the parameter dictionary of constants
    :return:
    """
    # make a graph
    fig, frame = plt.subplots(ncols=1, nrows=1)
    # plot the frame
    frame.plot([1, 2, 3, 4], [1, 4, 9, 16])
    # -------------------------------------------------------------------------
    # deal with saving (do not remove)
    core.save(params, outname='test_plot.pdf')
    core.show(params)
    core.close()
```


You can import the plotting directory in science functions but never import 
any science functions into the plotting directory.