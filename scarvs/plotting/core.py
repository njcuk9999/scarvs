#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Core plotting functions (i.e. general plotting functions used in multiple
other plotting functions)

Do not import individual plotting functions in here (i.e. do not import
functions defined in PLOT_FUNCS)

Created on 2024-10-29 at 09:57

@author: cook
"""
import os
from typing import Optional

import matplotlib.pyplot as plt

from aperocore.constants import param_functions
from aperocore.core import drs_log
from scarvs.core import base

# =============================================================================
# Define variables
# =============================================================================
__NAME__ = 'scarvs.plotting.core.py'
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
def save(params: ParamDict, outname: str, outdir: Optional[str] = None):
    """
    Save the plot to file(s)

    :param params: ParamDict, the parameter dictionary of constants
    :param outname: str, the name of the output file (no extension)
    :param outdir: str or None, if defined overrides PLOT_PATH

    :return: None, saves plot to file(s)
    """
    # define function name
    func_name = __NAME__ + '.save()'
    # deal with not saving plot
    if params['GLOBAL.PLOTTING'] not in [2, 3]:
        return
    # deal with no output direcory
    if outdir is None:
        outdir = params['GLOBAL.PLOT_PATH']
        # deal with still no output directory
        if params['GLOBAL.PLOT_PATH'] is None:
            wmsg = ('"GLOBAL.PLOT_PATH" is not defined cannot save plot.'
                    '\n\t Define either "GLOBAL.PLOT_PATH" or set "outdir" '
                    'before running {0}.'.format(func_name))
            WLOG(params, 'warning', wmsg)
            return
    # create file name
    filename = os.path.join(outdir, outname)
    # save the plots
    for extension in params['GLOBAL.PLOT_TYPES']:
        # log saving
        msg = 'Saving plot to file: {0}.{1}'
        margs = [filename, extension]
        WLOG(params, '', msg.format(*margs))
        # save the plot
        plt.savefig(filename + '.' + extension)


def show(params: ParamDict, block: bool = True):
    """
    Show the plot to screen

    :param params: ParamDict, the parameter dictionary of constants
    :param block: bool, if True will block until plot is closed

    :return: None, shows plot to screen
    """
    # deal with not showing plots
    if params['GLOBAL.PLOTTING'] not in [1, 3]:
        return
    # show the plot
    plt.show(block=block)



def close():
    """
    Close all plots
    :return:
    """
    plt.close('all')

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
