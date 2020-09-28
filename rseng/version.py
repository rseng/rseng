"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

__version__ = "0.0.17"
AUTHOR = "Vanessa Sochat"
AUTHOR_EMAIL = "vsochat@stanford.edu"
NAME = "rseng"
PACKAGE_URL = "https://github.com/rseng/rseng"
KEYWORDS = "rse,software,research software,criteria,taxonomy"
DESCRIPTION = "criteria and taxonomy for research software engineering"
LICENSE = "LICENSE"

################################################################################
# Global requirements


INSTALL_REQUIRES = (
    ("requests", {"min_version": "2.23.0"}),
    ("pyaml", {"min_version": "20.3.1"}),
    ("Jinja2", {"min_version": None}),
)
TESTS_REQUIRES = (("pytest", {"min_version": "4.6.2"}),)


ALL_REQUIRES = INSTALL_REQUIRES
