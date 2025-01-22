#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# CODE NAME HERE

# CODE DESCRIPTION HERE

Created on 2024-10-29 at 10:16

@author: cook
"""
from aperocore.constants import param_functions
from aperocore.core import drs_log

from scarvs.core import base

# =============================================================================
# Define variables
# =============================================================================
__NAME__ = 'scarvs.core.general.py'
__PACKAGE__ = base.__PACKAGE__
__version__ = base.__version__
__authors__ = base.__authors__
__date__ = base.__date__
__release__ = base.__release__
# get parameter dictionary
ParamDict = param_functions.ParamDict
# get the logger
WLOG = drs_log.wlog


# =============================================================================
# Define functions
# =============================================================================
def check_run(params: ParamDict, func_name: str, func_kind: str) -> bool:
    """
    Check whether to run a function

    :param params: ParamDict, the parameter dictionary of constants
    :param func_name: str, the name of the function to check
    :param func_kind: str, the kind of function (SCIENCE or PLOT)

    :return: bool, True if we should run the function, False otherwise
    """
    # deal with science function
    if func_kind == 'SCIENCE':
        dictname = 'SCIFUNCS'
        prefix = 'RUNSCI'
        path = 'science.__init__'
        parent = 'SCIENCE'
    # deal with plotting function
    elif func_kind == 'PLOTTING':
        dictname = 'PLOTFUNCS'
        prefix = 'RUNPLOT'
        path = 'plotting.__init__'
        parent = 'PLOTTING'
    else:
        emsg = f'Function kind "{func_kind}" not recognized'
        raise base.SCARVSException(emsg)
    # deal with func name not in dictionary (shouldn't happen)
    if func_name not in params[dictname]:
        wmsg = f'Function "{func_name}" not found in {path}.{dictname}'
        wmsg += f'\n\t Skipping {func_name}'
        WLOG(params, 'warning', wmsg)
        return False
    # deal with prefix+func_name not in constants (poor definition - can happen)
    if f'{parent}.{prefix}_{func_name}' not in params:
        wmsg = f'Parameter "{prefix}_{func_name}" not found in constants'
        wmsg += f'\n\t Skipping {func_name}'
        WLOG(params, 'warning', wmsg)
        return False
    # if we've got to here we can check whether to run
    return params[f'{parent}.{prefix}_{func_name}']


def log_run(params: ParamDict, func_name: str, func_kind: str):
    """
    Check whether to run a function

    :param params: ParamDict, the parameter dictionary of constants
    :param func_name: str, the name of the function to check
    :param func_kind: str, the kind of function (SCIENCE or PLOT)

    :return: bool, True if we should run the function, False otherwise
    """
    WLOG(params, 'info', params['DRS_HEADER'])
    WLOG(params, 'info', f'Running {func_kind.lower()} function: {func_name}')
    WLOG(params, 'info', params['DRS_HEADER'])


def start_splash(name: str):
    """
    Print the start splash

    :return: None, prints to screen
    """
    WLOG(None, 'info', drs_log.MPARAMS['DRS_HEADER'], colour='magenta')
    WLOG(None, 'info', name, colour='magenta')
    vargs = [__version__, __date__]
    WLOG(None, 'info', 'v{0} [{1}]'.format(*vargs), colour='magenta')
    WLOG(None, 'info', drs_log.MPARAMS['DRS_HEADER'], colour='magenta')


def end_splash():
    """
    Print the end splash

    :return: None, prints to screen
    """
    WLOG(None, 'info', drs_log.MPARAMS['DRS_HEADER'], colour='magenta')
    WLOG(None, 'info', 'End of code', colour='magenta')
    WLOG(None, 'info', drs_log.MPARAMS['DRS_HEADER'], colour='magenta')


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
