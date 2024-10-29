#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# CODE NAME HERE

# CODE DESCRIPTION HERE

Created on 2024-10-29 at 09:49

@author: cook
"""
from aperocore.constants import param_functions
from aperocore.core import drs_log

from uprv.core import base

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
def test(params: ParamDict):
    """
    First argument must be params

    :param params: ParamDict, the parameter dictionary of constants
    :return:
    """
    # print a message for this function
    WLOG(params, 'info', 'This is a test function')
    # loop around keys in params and print them
    for key in params:
        if key in ['SCIFUNCS', 'PLOTFUNCS']:
            msg = 'Current defined {0} functions are:\n\t'.format(key)
            msg += '\n\t'.join(list(params[key].keys()))
            WLOG(params, '', msg, wrap=False)
        else:
            msg = 'Key = {0}, Value = {1}, Source = {2}'
            margs = [key, params[key], params.sources[key]]
            WLOG(params, '', msg.format(*margs), wrap=False)
    # return nothing
    return


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
