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

# =============================================================================
# Define functions
# =============================================================================
def main():
    # print splash
    general.start_splash('SCARVS Setup')
    # get parameters
    params = startup.get_params(yaml_required=False, from_file=False,
                                description=__description__, name='SETUP')
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
