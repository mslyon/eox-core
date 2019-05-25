#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pre-enrollment public function definitions
"""

from importlib import import_module
from django.conf import settings


def create_pre_enrollment(*args, **kwargs):
    """
    Create a pre-enrollment for an existing or future user
    """

    backend_function = settings.EOX_CORE_PRE_ENROLLMENT_BACKEND
    backend = import_module(backend_function)

    return backend.create_pre_enrollment(*args, **kwargs)


def validate_pre_enrollment(*args, **kwargs):
    """ Validate CourseEnrollmentAllowed fields """

    backend_function = settings.EOX_CORE_PRE_ENROLLMENT_BACKEND
    backend = import_module(backend_function)

    return backend.validate_pre_enrollment(*args, **kwargs)
