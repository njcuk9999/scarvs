#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# CODE NAME HERE

# CODE DESCRIPTION HERE

Created on 2024-10-29 at 09:29

@author: cook
"""
from scarvs.science import test
from scarvs.science import test, radial_velocity


# =============================================================================
# Define variables
# =============================================================================
# a dictionary of science functions
SCIENCE_FUNCS = dict()

# Test science function
SCIENCE_FUNCS['TEST'] = test.test

# Radial velocity fitting functions
SCIENCE_FUNCS['FIT_KEPLERIAN_ONLY'] = radial_velocity.fit_keplerian_only
# =============================================================================
# End of code
# =============================================================================
