#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# CODE NAME HERE

# CODE DESCRIPTION HERE

Created on 2024-10-29 at 09:49

@author: cook
"""
import matplotlib.pyplot as plt

from aperocore.constants import param_functions
from aperocore.core import drs_log

from uprv.core import base
from uprv.plotting import core

# =============================================================================
# Define variables
# =============================================================================
__NAME__ = 'uprv.plotting.test.py'
__PACKAGE__ = base.__PACKAGE__
__version__ = base.__version__
__authors__ = base.__authors__
__date__ = base.__date__
__release__ = base.__release__
# get parameter dictionary
ParamDict = param_functions.ParamDict
# get the logger
WLOG = drs_log.wlog
# -----------------------------------------------------------------------------

# =============================================================================
# Define functions
# =============================================================================
def test(params: ParamDict) -> ParamDict:
    """
    First argument must be params

    :param params: ParamDict, the parameter dictionary of constants

    :return params: ParamDict, the parameter dictionary of constants
    """
    # make a graph
    fig, frame = plt.subplots(ncols=1, nrows=1)
    # plot the frame
    frame.plot([1, 2, 3, 4], [1, 4, 9, 16])
    # -------------------------------------------------------------------------
    # deal with saving (do not remove)
    core.save(params, outname='test_plot')
    core.show(params)
    core.close()
    # -------------------------------------------------------------------------
    # always return params (for use elsewhere)
    return params


# =============================================================================
# Start of code
# =============================================================================
# Main code here
if __name__ == "__main__":
    # ----------------------------------------------------------------------
    # print 'Hello World!'
    print("Hello World!")

# =============================================================================
# End of code
# =============================================================================
