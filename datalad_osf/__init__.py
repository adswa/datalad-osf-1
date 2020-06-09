# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

command_suite = (
    'OSF support',
    [
        (
            'datalad_osf.get',
            'Get',
            'osf-get',
            'osf_get',
        ),
        (
            'datalad_osf.update',
            'Update',
            'osf-update',
            'osf_update',
        ),
    ]
)

from .utils import update_recursive, get_osf_recursive

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
