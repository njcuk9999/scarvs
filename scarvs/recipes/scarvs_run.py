#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# CODE NAME HERE

# CODE DESCRIPTION HERE

Created on 2024-10-29 at 09:32

@author: cook
"""
from typing import Optional

from scarvs.core import base
from scarvs.core import startup
from scarvs.core import general

# =============================================================================
# Define variables
# =============================================================================
__NAME__ = 'scarvs.constants.constants.py'
__PACKAGE__ = base.__PACKAGE__
__version__ = base.__version__
__authors__ = base.__authors__
__date__ = base.__date__
__release__ = base.__release__
# set description
__description__ = 'Setup the SCARVS recipes'
__inputs__ = ['GLOBAL.YAML_FILE']

# =============================================================================
# Define functions
# =============================================================================
def main(**kwargs):
    # print splash
    general.start_splash('SCARVS Run')
    # get parameters
    params = startup.get_params(name='run', description=__description__,
                                inputargs=__inputs__, kwargs=kwargs)
    # run science functions
    for science_func in params['SCIFUNCS']:
        # check whether we should run this function then run it
        if general.check_run(params, science_func, 'SCIENCE'):
            # log the we are running a function
            general.log_run(params, science_func, 'SCIENCE')
            # run the science function
            params = params['SCIFUNCS'][science_func](params)
    # run plotting functions
    for plot_func in params['PLOTFUNCS']:
        # check whether we should run this function then run it
        if general.check_run(params, plot_func, 'PLOTTING'):
            # log the we are running a function
            general.log_run(params, plot_func, 'PLOTTING')
            # run the plotting function
            params = params['PLOTFUNCS'][plot_func](params)
    # print splash
    general.end_splash()

def run():
    _ = main()

# =============================================================================
# Start of code
# =============================================================================
# Main code here
if __name__ == "__main__":
    # ----------------------------------------------------------------------
    _ = main()

# =============================================================================
# End of code
# =============================================================================
