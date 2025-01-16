#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# CODE NAME HERE

# CODE DESCRIPTION HERE

Created on 2024-10-29 at 09:32

@author: cook
"""
from aperocore.core import drs_log
from aperocore.constants import load_functions

from scarvs.constants.constants import CDict
from scarvs.core import base
from scarvs.core import general
from scarvs.core import startup

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
    general.start_splash('SCARVS Setup')
    # get parameters
    params = load_functions.get_all_params(name=__NAME__,
                                           description=__description__,
                                           inputargs=__inputs__,
                                           param_file_path='GLOBAL.YAML_FILE',
                                           config_list=[CDict],
                                           kwargs=kwargs)
    # setup using parameters
    startup.setup(params)
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
